import React from "react";
import {BrowserView, MobileView} from 'react-device-detect';
import "../index.css"
import UploadComponent from "./UploadComponent"
import photoLogo from "../assets/photo_logo.png"
import { useNavigate } from "react-router-dom";
import Header from './Header';
import ServiceDropdown from "./ServiceDropdown";
import { useState } from "react";

function Home() {

    let navigate = useNavigate();

    const [lang, setLang] = useState("pl");

    const navigateCamera = () => {
        navigate(`camera`, {lang: lang});
    };

    return (
        <div className="mainLayout">
           <Header/>
            <div>
                <BrowserView>
                    <div className="browserWrapper shadow">
                        <div className="browserUpload">
                            <UploadComponent className="shadow" lang={lang}/>
                        </div>
                        <div className="serviceDropdownWrapper">
                            <ServiceDropdown setLang={setLang}/> 
                        </div>
                    </div>
                        
                </BrowserView>

                <MobileView>
                    <div className="mobileLayout">
                        <div className="fileContainer">
                            <img src={photoLogo} className="photoLogo"/>
                            <button className="takePhotoButton" onClick={navigateCamera}>
                                Take a photo
                            </button>
                        </div>
                        <p className="uploadMethodChoice">or</p>
                        <UploadComponent lang={lang}/>
                        <div className="serviceDropdownWrapperMobile">
                            <ServiceDropdown setLang={setLang}/> 
                        </div>
                    </div>
                </MobileView>
            </div>    
        </div>
    )
}

export default Home;