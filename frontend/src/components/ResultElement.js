import React, { useState } from "react";

const ResultElement = (props) => {

    const getImgSrc = (img) => { 
        return `data:image/jpeg;base64,${img}`
    }
    const [originalImage, setOriginalImage] = useState(props.image)
    const [expand, setExpand] = useState(false);
    const [choosen, setChoosen] = useState(false);
    const serverUrl = process.env.REACT_APP_SERVER_SCHEME + "://" + 
                        process.env.REACT_APP_SERVER_URL + ":" + 
                        process.env.REACT_APP_SERVER_PORT; 
    const detectBook = () => {
        if(props.childClicked && !expand)
            return;
        if(!expand) {
            const requestOptions = {
                method: 'POST',
                headers: { 
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'},
                body: JSON.stringify({ 
                    task_id: props.task_id,
                    book_id: props.book_id})
            };
            fetch(serverUrl + process.env.REACT_APP_SERVER_DETECT_BOOK_ENDPOINT, requestOptions)
                .then(response => {return response.json();})
                .then(response => {
                    if(response.status == "200") {
                        props.setImage(getImgSrc(JSON.parse(response.response).image));
                    }
                })
                .then(() => { 
                    setExpand(true); 
                    setChoosen(true); 
                }).then(() => {props.setChildClicked(true); });
                
        } else {
            unClickElement();
        }
    }
    const unClickElement = () => {
        setChoosen(false); 
        setExpand(false); 
        props.setImage(originalImage);
        props.setChildClicked(false);
    }
    const prepareResultElement = () => {
        var elemSize = "Small";
        if(expand)
            elemSize = "Big";
        var resultElementStyle = "resultElement";
        if(choosen)
            resultElementStyle = "resultElementChoosen"
        return <div className={resultElementStyle + " " + elemSize} onClick={() => {detectBook();}}>
                <div className="resultDetailsRowSmall">
                    <div className="resultDetail title">{props.title}</div>
                    <div className="resultDetail author">{props.author}</div>
                    <div className="resultDetail rating">{props.rating}</div>
                </div>
                {expand && 
                <div className="resultDetailsRowBig">
                        <div className="description">{props.description}</div>
                </div>
            }
        </div>
    }
    return <div>
        {prepareResultElement()}
    </div>;
}

export default ResultElement;