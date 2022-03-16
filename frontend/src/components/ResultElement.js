import React, { useState } from "react";

const ResultElement = (props) => {

    const [expand, setExpand] = useState(false);
    const prepareResultElement = () => {
        var elemSize = "Small"
        if(expand)
            elemSize = "Big"
                
        return <div className={"resultElement resultElement" + elemSize } onClick={() => {setExpand(!expand)}}>
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