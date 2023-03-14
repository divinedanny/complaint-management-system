// student/login.js

import React from "react";


const Login = () =>(
<div className="container-fluid div2">
    dvkvk
    <div className="col-md-7 bg-white centerDiv p-5 mt-5 mb-5">
        <h1 className="text-center">Student Login</h1>
        <div>
            <form>
                <div className="form-group ml-4 mr-4">
                     <input type="text" placeholder="Matric number" className="form-control"></input>
                </div>
                <div className="form-group ml-4 mr-4">
                    <input type="password" placeholder="Password" className="form-control"></input>
                    <small id="emailHelp" className ="form-text text-muted text-right">Forgot password?</small>
                </div>
                <button type="submit" class="btn btnorange btnbloc">Login</button>
                <small id="emailHelp" className ="form-text text-muted text-center">Don't have an account?</small>
                
            </form>
        </div>
    </div>
    dvkvk
</div>
);

export default Login;