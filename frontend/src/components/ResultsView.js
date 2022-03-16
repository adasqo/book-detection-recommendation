import React, { useState } from "react";
import { BrowserView, MobileView } from "react-device-detect";
import { useLocation } from "react-router-dom";
import imagePlaceholder from "../assets/image_placeholder.png"
import Header from './Header';
import ResultElement from './ResultElement';


const elements = [
    {
        "title": "Zbrodnia i kara",
        "author": "Fiodor Dostojewski",
        "rating": 7.9,
        "description": "Słynna powieść Fiodora Dostojewskiego, opowiadająca o losach byłego studenta Rodiona Raskolnikowa, który postanawia zamordować i obrabować bogatą lichwiarkę. \
        Pomysł na tę powieść narodził się w czasie, kiedy sam autor przebywał na katordze. Zainteresował się wtedy psychologią współwięźniów, wśród których byli i tacy, którzy zostali skazani za morderstwo. \
        Bohater powieści, 23-letni były student prawa jest półsierotą, ma jednak kochająca rodzinę. Jego matka i siostra darzą go głęboką miłością i wspierają finansowo. \
        Jednak bohater, zbuntowany przeciw porządkowi świata, decyduje się popełnić morderstwo. Jest przekonany, że jako jednostka wybitna, ma prawo zabijać, gdyż geniusz usprawiedliwia wszystkie zbrodnie na \
        „zwykłych” ludziach. Morderstwo ma stać się rodzajem sprawdzianu jego odwagi. Choć jednocześnie bezpośrednia pobudką tego czynu jest zła sytuacja finansowa Raskolnikowa…"
    },
    {
        "title": "Zabić drozda",
        "author": "Harper Lee",
        "rating": 8.1,
        "description": "Lata trzydzieste XX wieku, małe miasteczko na południu USA. Atticus Finch, adwokat i głowa rodziny, broni młodego Murzyna oskarżonego o zgwałcenie biednej białej dziewczyny Mayelli Ewell.\
         Prosta sprawa sądowa z powodu wszechpanującego rasizmu, urasta do rangi symbolu. W codziennej walce o równouprawnienie czarnych jak echo powraca pytanie o to, gdzie przebiegają granice ludzkiej tolerancji. \
         Zabić drozda to wstrząsająca historia o dzieciństwie i kryzysie sumienia. Poruszająca opowieść odwołuje się do tego, co o życiu człowieka najcenniejsze: miłości, współczucia i dobroci."
    },
    {
        "title": "Dżuma",
        "author": "Albert Camus",
        "rating": 7.0,
        "description": "Metaforyczny obraz świata walczącego ze złem, którego symbolem jest tytułowa dżuma, pustosząca Oran w 194… roku. Wybuch epidemii wywołuje różne reakcje u mieszkańców,\
         jednak stopniowo uznają słuszność postępowania doktora Rieux, który od początku aktywnie walczy z zarazą, uznając to za swój obowiązek jako człowieka i lekarza."
    }
]

function ResultsView(props) {

    const {state} = useLocation();
    const getImgSrc = () => { 
        if (state.image == undefined)
            return imagePlaceholder;
        return `data:image/jpeg;base64,${state.image}`
    }
    
    const imgSrc = getImgSrc();

    const [image, setImage] = useState(imgSrc);
    const [resultsList, setResultsList] = useState(elements);

    const createResultsList = () => {
        var results = []
        for (var i=0; i<resultsList.length; i++) {
            var elem = resultsList[i];
            results.push(
                <ResultElement 
                    title={elem.title}
                    author={elem.author}
                    rating={elem.rating}
                    description={elem.description}
                />
            )
        }
        return results;
    }
    console.log(image)   
    return (
        <div className="mainLayout">
            <Header/>
            <BrowserView >
                <div className="browserWrapper">
                    <div className="imagePlaceholder">
                        <img src={image} className="resultImageBrowser" />
                    </div>
                    <div className="resultsList">
                        {createResultsList()}
                    </div>
                </div>
            </BrowserView>
            <MobileView>
                
                <div className="imagePlaceholder">
                    <img src={image} className="resultImage" />
                </div>
                <div className="resultsList">
                    {createResultsList()}
                </div>
            </MobileView>
            
        </div>
    );
}

export default ResultsView;
      