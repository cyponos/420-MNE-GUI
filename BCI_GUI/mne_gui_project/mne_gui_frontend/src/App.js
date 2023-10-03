import Header from './components/HeaderBar/Header.js'
import './App.css';

function App() {
  return (
    <div className="App">
      <div className="app-container">
        <Header />
        <div className="body-content">
          <div className="flex-column">
            <div className="flex-selection">
              File Selection
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
