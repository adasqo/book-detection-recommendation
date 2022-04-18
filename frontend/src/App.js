
import Home from './components/Home';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import WebcamCapture from './components/WebcamCapture';
import ResultsView from './components/ResultsView';

function App() {

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
