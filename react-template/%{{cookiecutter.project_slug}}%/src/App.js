import logo from './logo.svg';
import './App.css';
import {Component} from "react";

class App extends Component {
  state = {
    backend: {
      status: "Not Available",
      components: []
    }
  };

  async componentDidMount() {
    const response = await fetch(process.env.REACT_APP_BFF_URL + "/actuator/health");
    const body = await response.json();
    this.setState({backend: body});
  }

  render() {
    const {backend} = this.state;
    return (
        <div className="App">
          <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <div className="App-intro">
              <h2>Backend Status</h2>
              <div key={0} style={{textAlign: "left"}}>
                <span style={{fontWeight: "bold"}}>status: {backend?.status}</span>
                <hr/>
              </div>
              {
                  backend?.components && Object.keys(backend?.components)?.map((key, i) => (
                      <div key={i+1} style={{textAlign: "left", display: "table-row"}}>
                        <div style={{fontWeight: "bold", display: "table-cell"}}>{key}:</div>
                        <div style={{textAlign: "right", display: "table-cell"}}>{backend?.components?.[key]?.status}</div>
                      </div>
                  ))
              }
            </div>
          </header>
        </div>
    );
  }
}
export default App;
