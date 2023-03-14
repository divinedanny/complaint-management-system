// student/register.js

import React from "react";

function Register() {
    return(
<div className="container-fluid div2">
    dvkvk
    <div className="col-md-7 bg-white centerDiv p-5 mt-3 mb-2">
        <h1 className="text-center">User Registeration</h1>
        <div className="p-4 mt-5">
            <form>
                <div className="form-group ml-4 mr-4">
                     <input type="text" placeholder="Full name" className="form-control"></input>
                </div>
                <div className="form-group ml-4 mr-4">
                     <input type="text" placeholder="Matric number" className="form-control"></input>
                </div>
                <div className="form-group ml-4 mr-4">
                    <input type="email" placeholder="Email" className="form-control"></input>
                </div>
                <div className="form-group ml-4 mr-4 mb-5">
                    <input type="password" placeholder="Password" className="form-control"></input>
                    <small id="emailHelp" className ="form-text text-muted text-right mb-4">Already Registered?</small>
                </div>
                <button type="submit" class="btn btnorange btnbloc rounded mt-4">Register</button>
                
            </form>
        </div>
    </div>
    d
</div>
)};

export default Register;