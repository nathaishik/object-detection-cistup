import './App.css';
import { useState } from 'react';
import axios from 'axios';

  
  export default function App() {
    const [img, setImg] = useState(null);

    function Form() {
      function handleUpload (e) {
        const form = document.getElementById('form');
        form.submit();
      }

      return (
        <form id="form" accept="image/*" action="http://127.0.0.1:8000" method="POST" encType='multipart/form-data'>
          <input type="file" accept="image/*" onChange={handleUpload} name="image"/>
        </form>
      )
    }

    return (
      <div className="App">
        <h1>Vehicle Detection</h1>
        <Form />
      </div>
    );
  }
