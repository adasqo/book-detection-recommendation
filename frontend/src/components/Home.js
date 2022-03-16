import React from "react";
import {BrowserView, MobileView} from 'react-device-detect';
import "../index.css"
import UploadComponent from "./UploadComponent"
import photoLogo from "../assets/photo_logo.png"
import { useNavigate } from "react-router-dom";
import Header from './Header';

function Home() {

    let navigate = useNavigate();

    const navigateCamera = () => {
        navigate(`camera`);
    };

    return (
        <div className="mainLayout">
           <Header/>
            <div>
                <BrowserView>
                    <div className="browserWrapper shadow">
                        <div className="browserUpload">
                            <UploadComponent className="shadow"/>
                        </div>
                    </div>
                </BrowserView>

                <MobileView>
                    <div className="homeElementsLayout">
                        <div className="fileContainer">
                            <img src={photoLogo} className="photoLogo"/>
                            <button className="takePhotoButton" onClick={navigateCamera}>
                                Take a photo
                            </button>
                        </div>
                        <p className="uploadMethodChoice">or</p>
                        <UploadComponent/>
                    </div>
                </MobileView>
            </div>           
        </div>
    )
}

export default Home;