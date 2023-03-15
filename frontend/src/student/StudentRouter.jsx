import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Dashboard from './Dashboard';
import Account, { Password, Profile } from './Account';
import Complaint, { Add, History } from './Complaint';
import Sidebar from "../components/Sidebar";

export const StudentRouter = () => {
    return (
        <Router>
      <div className="">
        <Sidebar />
        <Routes>
          <Route exact path="/dashboard" element={<Dashboard />} />
          <Route path="/account-Setting" element={<Profile />} />
          <Route path="/account-Setting/password" element={<Password />} />
          <Route path="/complaints/add" element={<Add />} />
          <Route path="/complaints/history" element={<History />} />
        </Routes>
      </div>
  </Router>
    );
};