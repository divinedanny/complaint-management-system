// Student Account

import React from "react";
import Sidebar from "../components/Sidebar";


export const Profile = () => {
    return (
        <div className="container-fluid">
            <h3 className="ml-5">Profile</h3>
            <div className="container div2 p-3 mb-4 ml-5 mr-5">       
            <form action="">
            <div className="row pb-3">
                <div className="col form-group pl-5 pr-5 pb-3">
                    <label htmlFor="">Fullname</label>
                    <input type="text" className="form-control" />
                </div>
                <div className="col form-group pl-5 pr-5 pb-3">
                <label htmlFor="">Email</label>
                    <input type="email" className="form-control" />
                </div>
            </div>
            <div className="row pb-3">
                <div className="col form-group pl-5 pr-5">
                    <label htmlFor="">Hall of residence</label>
                    <input type="text" className="form-control" />
                </div>
                <div className="col form-group pl-5 pr-5">
                <label htmlFor="">Department</label>
                    <input type="text" className="form-control" />
                </div>
            </div>
            <div className="row pb-3">
                <div className="col form-group pl-5 pr-5">
                    <label htmlFor="">Level</label>
                    <input type="text" className="form-control" />
                </div>
                <div className="col form-group pl-5 pr-5">
                <label htmlFor="">Worship center</label>
                    <input type="text" className="form-control" />
                </div>
            </div>
            <button type="submit" class="btn btnorange margin rounded mt-4 mb-1 pl-5 pr-5">Register</button>
        </form>
        </div>

        </div>
    );
};

export const Password = () => {
    return (
        <div className="container-fluid">
            <h3 className="ml-5 mt-2 mb-2">Change Password</h3>
            <div className="container div2 p-3 ml-5 mr-5 margin">
                <form className="margin col-8 pb-5 pt-5" action="">
                    <div className="row m-3">
                        <label htmlFor="">Old password</label>
                        <input className="form-control col-6 ml-5 mb-3" type="password" name="" id="" />
                    </div>
                    <div className="row m-3">
                        <label htmlFor="">New password</label>
                        <input className="form-control col-6 ml-5 mb-3" type="password" name="" id="" />
                    </div>
                    <div className="row m-3">
                        <label htmlFor="">Confirm password</label>
                        <input className="form-control col-6 ml-3 mb-3" type="password" name="" id="" />
                    </div>
                    <button type="submit" class="btn btnorange margin rounded mt-4 mb-1 pl-5 pr-5">Change Password</button>
                </form>
            </div>
        </div>
    );
};