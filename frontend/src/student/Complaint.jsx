// Student Complaint

import React from "react";


export const Add = () => {
    return (
        <div className="container-fluid">
            <h3 className="ml-5 mt-2 mb-2">Add complaint</h3>
            <div className="container div2 p-3 ml-5 mr-5 margin">
                <form className="margin col-8 pb-5 pt-5" action="">
                    <div className="row m-3">
                        <label className="col-2">Category</label>
                        <select className="form-control col-6 ml-5 mb-3">
                        <option value="Category">Category</option>
                        <option value="Category">Category</option>
                        </select>
                        
                    </div>
                    <div className="row m-3">
                        <label className="col-2">Subcategory</label>
                        <input className="form-control col-6 ml-5 mb-3" type="text" name="" id="" />
                    </div>
                    <div className="row m-3">
                        <label className="col-2">Complaint type</label>
                        <input className="form-control col-6 ml-5 mb-3" type="text" name="" id="" />
                    </div>
                    <div className="row m-3">
                        <label className="col-2 mr-4">Nature of complaint</label>
                        <input className="form-control col-6 ml-3 mb-3" type="text" name="" id="" />
                    </div>
                    <div className="row m-3">
                        <label className="col-2 mr-4">Complaint details</label>
                        <textarea className="form-control col-6 ml-3 mb-3" name="" id="" />
                    </div>
                    <button type="submit" class="btn btnorange margin rounded mt-4 mb-1 pl-5 pr-5">Change Password</button>
                </form>
            </div>
        </div>
    );
};

export const History = () => {
    return (
        <div className="container-fluid">
            <h3 className="ml-5 mt-2 mb-2">Add complaint</h3>
            <div className="container div3 p-3 ml-5 mr-5 margin">
                <table className="table">
                    <thead>
                        <tr>
                            <th>Complaint ID</th>
                            <th>Registeration Date</th>
                            <th>Status</th>
                            <th>Completion Date</th>
                            <th>Details</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <th>1</th>
                            <td>22/4/23</td>
                            <td>unprocessed</td>
                            <td>27/4/23</td>
                            <td>Bursary</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    );
};

