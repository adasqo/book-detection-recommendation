import ImageUploader from "react-images-upload";
import { useNavigate } from "react-router-dom";

function UploadComponent() {

    const navigate = useNavigate();

    const onImageChange = async (_, successImages) => {
        const parts = successImages[0].split(';');
        var image = parts[2].split(',')[1];
        navigate('/results', { state: {image: image} })
    }
    return (
        <div className="imageUploadDiv">
            <ImageUploader
                key="image-uploader"
                withIcon={true}
                singleImage={true}
                buttonText="Upload an image"
                onChange={onImageChange}
                label=""
                imgExtension={[".jpg", ".jpeg", ".png"]}
            />
        </div>

    );
}

export default UploadComponent;