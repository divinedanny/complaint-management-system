// Student dashboard

import React from "react";
import Sidebar from "../components/Sidebar";

const Dashboard = () => {
    return (
        <div className="container-fluid">
            <div className="mt-3"><button className="btn btn-outline-primary btn-lg btnbloc pt-5 pb-5"> 0 closed complaints</button></div>
            <div className="mt-3"><button className="btn btn-outline-primary btn-lg btnbloc pt-5 pb-5"> 0 pending complaints</button></div>
            <div className="mt-3"><button className="btn btn-outline-primary btn-lg btnbloc pt-5 pb-5"> 0 unprocessed complaints</button></div>
        </div>
    );
};
export default Dashboard;