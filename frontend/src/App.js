import './App.css';
// import Homepage from './components/Homepage';
// import Register from './student/Register';
// import Login from './student/login';
// import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { StudentRouter } from './student/StudentRouter';



function App() {
  return (
  //  <Homepage />
    <StudentRouter />
  );
};

export default App;
