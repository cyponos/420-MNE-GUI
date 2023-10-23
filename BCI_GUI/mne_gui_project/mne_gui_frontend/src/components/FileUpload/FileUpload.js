import './FileUpload.css';
import axios from 'axios';
import { useEffect, useState } from 'react';

function FileUpload() {

  const [ file, setFile ] = useState(null);
  const [ progress, setProgress ] = useState({ started: false, pc: 0 });
  const [ msg, setMsg ] = useState(null);

  function handleUpload() {
    if (!file) {
      setMsg("No file selected");
      return;
    }

    const fd = new FormData();
    fd.append('file', file);

    setMsg("Uploading...");
    setProgress(prevState => {
      return {...prevState, started: true}
    });
    axios.post('http://127.0.0.1:8000/', fd, {
      onUploadProgress: (progressEvent) => { setMsg(prevState => {
        return { ...prevState, pc: progressEvent.progress*100 }
      }) },
      headers: {
        "Custom-Header": "value",
      }
    })
    .then(res => {
      setMsg("Upload Successful");
      console.log(res.data);
    })
    .catch(err => {
      setMsg("Upload Failed");
      console.error(err);
    });
  };

  return (
    <div className="file-upload-container">
      <div className="file-upload">
        <form>
          <input 
            type="file"
            onChange={ (e) => { setFile(e.target.files[0]) } }
          />
          <button onClick={ handleUpload }>
            Submit
          </button>
        </form>
        { progress.started && <progress max="100" value={progress.pc}></progress> }
        { msg && <span>{msg}</span> }
      </div>
    </div>
  );
}

export default FileUpload;