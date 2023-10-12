import './FileUpload.css';
import axios from 'axios';
import { useEffect, useState } from 'react';

function FileUpload() {

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
    <div className="file-upload-container">
      <div className="file-upload">
        <form onSubmit={handleSubmit}>
          <input 
            type="file"
            name="file"
            value={formData.file}
            onChange={handleChange}
          />
          <button>
            Submit
          </button>
        </form>
      </div>
    </div>
  );
}

export default FileUpload;