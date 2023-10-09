import React from 'react';
import axios from 'axios';
import Header from './components/HeaderBar/Header.js'
import './App.css';

class App extends React.Component {

  state = { details: [], }

  componentDidMount() {

    let data;
    axios.get('http://localhost:8000')
    .then(res => {
      data = res.data;
      this.setState({
        details: data
      });
    })
    .catch(err => { })
  }

  render() {
    return (
      <div className="App">
        <div className="app-container">
          <Header />
          <div className="body-content">
            <div className="flex-column">
              <div className="flex-selection">
                File Selection

                {/* Temporary Test Data */}
                {this.state.details.map((output, id) =>
                  <div key={id}>
                    <div>
                      {output.name}
                      {output.detail}
                    </div>
                  </div>
                )}
                {/* Temporary Test Data */}

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
}

export default App;
