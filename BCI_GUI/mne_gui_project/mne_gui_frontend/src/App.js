import React from 'react';
import axios from 'axios';
import Header from './components/HeaderBar/Header.js';
import './App.css';

import { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState([]);
  const [formData, setFormData] = useState({ name: '', detail: '' });

  useEffect(() => {
    // Making a GET request to retrieve data
    axios.get('http://localhost:8000/')
      .then((response) => setData(response.data))
      .catch((error) => console.error('Error:', error));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();

    // Making a POST request to send data
    axios.post('http://localhost:8000/', formData)
      .then((response) => {
        console.log('Data sent successfully:', response.data);
        // Optionally, reset the form or update the state as needed
        setFormData({ name: '', detail: '' });
      })
      .catch((error) => console.error('Error:', error));
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleDelete = (itemId) => {
    // Making a DELETE request to delete an entry
    axios.delete(`http://localhost:8000/ReactView/${itemId}/`)
      .then((response) => {
        console.log('Response:', response);
        console.log('Entry deleted successfully:', response.data);
        // Optionally, update the state to remove the deleted entry
        setData((prevData) => prevData.filter((item) => item.id !== itemId));
      })
      .catch((error) => console.error('Error:', error));
  };

  return (
    <div className="App">
      <div className="app-container">
        <Header />
        <div className="body-content">
          <div className="flex-column">
            <div className="flex-selection">
              File Selection

              {/* TEST FUNC */}
              <form onSubmit={handleSubmit}>
                <input
                  type="text"
                  name="name"
                  placeholder="Name"
                  value={formData.name}
                  onChange={handleChange}
                />
                <input
                  type="text"
                  name="detail"
                  placeholder="Detail"
                  value={formData.detail}
                  onChange={handleChange}
                />
                <button type="submit">Submit</button>
              </form>

              {/* Render data from the API */}
              <ul>
                {data.map((item, index) => (
                  <li key={item.id}>
                    Name: {item.name}, Detail: {item.detail}
                    <button onClick={() => handleDelete(item.id)}>Delete</button>
                  </li>
                ))}
              </ul>
              {/* TEST FUNC */}
            
            </div>
            <div className="flex-selection">
              Filter Selection
            </div>
          </div>
          <div className="flex-column">
            <div className="flex-selection">
              Channel Selection
            </div>
            <div className="flex-selection">
              Output Selection
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
