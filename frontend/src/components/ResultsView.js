import React, { useState, useEffect } from "react";
import { BrowserView, MobileView } from "react-device-detect";
import { useLocation } from "react-router-dom";
import imagePlaceholder from "../assets/image_placeholder.png"
import SearchIcon from '@mui/icons-material/Search';
import Header from './Header';
import ResultElement from './ResultElement';
import { v4 as uuidv4 } from 'uuid';

const ResultsView = () => {

    const {state} = useLocation();

    const getImgSrc = (img) => { 
        if (img == undefined)
            return imagePlaceholder;
        return `data:image/jpeg;base64,${img}`
    }
    const [id, setId] = useState(uuidv4());
    const lang = state.lang;
    const serverUrl = process.env.REACT_APP_SERVER_SCHEME + "://" + 
                        process.env.REACT_APP_SERVER_URL + ":" + 
                        process.env.REACT_APP_SERVER_PORT; 
    const [image, setImage] = useState(getImgSrc(state.image));
    const [resultsListRender, setResultsListRender] = useState(
        <div className="loaderWrapper"><div className="loader"></div></div>);
    const [childClicked, setChildClicked] = useState(false);
    const [elementsOriginal, setElementsOriginal] = useState([]);
    const [elements, setElements] = useState([]);

    const searchElements = (event) => {
        const searchWord = event.target.value;
        const newElements = elementsOriginal.filter((value) => {
            return (value.title).toLowerCase().includes(searchWord);
        });
        setElements(newElements);
    }
    useEffect(async () => {
        var results = []
        const imageCopy = image.slice();
        elements.map((elem) => {
            if(elem == undefined) {
                return;
            }
            results.push(
                <ResultElement 
                    task_id={id}
                    book_id={elem.id}
                    title={elem.title}
                    author={elem.author}
                    rating={elem.rating}
                    description={elem.description}
                    image={imageCopy}
                    setImage={setImage}
                    childClicked={childClicked}
                    setChildClicked={setChildClicked}
                />
            )
        });
        if (results.length == 0) {
            results =  <div className="loaderWrapper"><div className="loader"></div></div>;
        }
        setResultsListRender(
            <div>
                <div className="searchWrapper">
                    <div className="loupe"><SearchIcon/></div>
                    <input
                        type="text"
                        className="search"
                        placeholder="Search"
                        onChange={searchElements}
                    />
                </div>
                <div>{results}</div>
            </div>
        );
    }, [elements, childClicked])

    useEffect(() => {
        const requestOptions = {
            method: 'POST',
            headers: { 
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'},
            body: JSON.stringify({ 
                id: id,
                image: state.image,
                lang: lang })
        };
        fetch(serverUrl + process.env.REACT_APP_SERVER_GET_RECOMMENDATIONS_ENDPOINT, requestOptions)
            .then(response => {return response.json();})
            .then(response => {
                if (response.status == 400) {
                    setResultsListRender(<div className="badRequest"><p>No books detected</p></div>)
                } else {
                    setImage(getImgSrc(JSON.parse(response.response).image));
                    prepareResponse(response.response)
                }
            })
            .catch((error) => {
                console.log(error)
              });
    }, []);

    const prepareResponse = (responseElements) => {
        var response = JSON.parse(responseElements);
        if(response.books == undefined || response.books.length == 0) {
            setResultsListRender(<div className="badRequest"><p>No books detected</p></div>);
            return;
        }
        const responseDetailsList = [].concat(response.books)
            .sort((a, b) => a.rating > b.rating ? -1 : 1);
        setElementsOriginal(responseDetailsList);
        setElements(responseDetailsList);
    }

    return (
        <div className="mainLayout">
            <Header/>
            <BrowserView >
                <div className="browserWrapper" id="browserWrapper">
                    <div className="imagePlaceholder">
                        <img src={image} className="resultImageBrowser" />
                    </div>
                    <div className="resultsList">
                        {resultsListRender}
                    </div>
                </div>
            </BrowserView>
            <MobileView>
                <div className="imagePlaceholder">
                    <img src={image} className="resultImage" />
                </div>
                <div className="resultsList">
                    {resultsListRender}
                </div>
            </MobileView>  
        </div>
    );
}

export default ResultsView;
      