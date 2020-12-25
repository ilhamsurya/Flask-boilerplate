import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect} from 'react';

function App() {
  const [initialData, setInitialData] = useState([{}])

  useEffect(() => {
    fetch('/').then(
      response => response.json()
    ).then(data => console.log(data))
  })

  return (
    <div className="App">
     
    </div>
  );
}

export default App;
