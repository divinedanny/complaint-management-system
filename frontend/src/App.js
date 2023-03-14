import './App.css';
import Homepage from './components/Homepage';
import Sidebar from './components/Sidebar';
import Register from './student/Register';
import Login from './student/login';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";



function App() {
  return (
    <Router>
      <div className="">
        <Sidebar />
        <Routes>
          <Route exact path="/" element={<Homepage />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </div>
  </Router>
  );
}

export default App;
