
import Camera, { FACING_MODES, IMAGE_TYPES } from 'react-html5-camera-photo';
import { useNavigate } from "react-router-dom";
import 'react-html5-camera-photo/build/css/index.css';
import React, { useState } from "react";

function WebcamCapture() {

    // const [image, setImage] = useState(null);

    function rotate(srcBase64, degrees, callback) {
        const canvas = document.createElement('canvas');
        let ctx = canvas.getContext("2d");
        let image = new Image();
        
        image.onload = function () {
            canvas.width = degrees % 180 === 0 ? image.width : image.height;
            canvas.height = degrees % 180 === 0 ? image.height : image.width;
        
            ctx.translate(canvas.width / 2, canvas.height / 2);
            ctx.rotate(degrees * Math.PI / 180);
            ctx.drawImage(image, image.width / -2, image.height / -2);
            callback(canvas.toDataURL());
        };
        image.src = srcBase64;
    }
    function handleTakePhoto (dataUri) {

        rotate(dataUri, 270, function(result) {
            const parts = result.split(';');
            const image = parts[1].split(',')[1];
            navigate('/results', { state: {image: image}})
        });
    }
    let navigate = useNavigate();
    const backHome = () => {
        navigate(`/`);
    };
    return (
        <div className="webcamView">
            <p className="takePhotoText">Take a photo horizontally!</p>
            <div className="webcamCapture">
                <Camera
                    onTakePhoto = { (dataUri) => { handleTakePhoto(dataUri); } }
                    idealFacingMode = {FACING_MODES.ENVIRONMENT}
                    isImageMirror = {false}
                    isSilentMode = {true}
                    imageType = {IMAGE_TYPES.JPG}
                    isFullscreen = {false}
                    imageCompression = {1}
                />
            </div>
        </div>
    );
}

export default WebcamCapture;