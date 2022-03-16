import './App.css';
import axios from 'axios';
import Home from './components/Home';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import WebcamCapture from './components/WebcamCapture';
import ResultsView from './components/ResultsView';

function App() {

  function uploadImage(image) {
    const formData = new FormData();
    formData.append("image", image, image.name)

    axios.post("http://localhost:8080/api/v1/recommendations", formData)
      .then(res => {console.log(res)})
  }
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Home/>}/>
          <Route path='/camera' element={<WebcamCapture/>}/>
          <Route path='/results' element={<ResultsView/>}/>
        </Routes>
      </BrowserRouter>
       
    </div>
  );
}

export default App;
