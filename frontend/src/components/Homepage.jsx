//homepage.js

import React from "react";

const Homepage = () => {
  return (
<div className="container-fluid">
      <div className="row div2">
        <div className = "col-md-4 bg-white">
          <div className="border m-4 mt-4"><h4 className="p-3 text-center display-7">Complaint Management System</h4></div>
          <div className="text text-center">Please checkout our system. This is a system provided to easily file a complaint. You can reach out and get an issue resolved today!</div>
          <hr></hr>
          <h5 className='text-center mt-2'>EST. 2023</h5>
        </div>
        <div className = "md-7">
          <span className='invisible'>cds</span>
          <div className='bg-white mr-4 ml-6 mt-4 mb-5'>
         <p className='pt-4 text-center fs-12'>Login as:</p>
         <hr className='mb-5 ml-5 mr-5'></hr>
         <div className='p-5'>
          <p><button type="button" className='btnorange btn btn-lg btnbloc p-3'>Student</button></p>
          <p><button type="button" className='btnorange btn btn-lg btnbloc p-3'>Staff</button></p>
          <p><button type="button" className='btnorange btn btn-lg btnbloc p-3'>Admin</button></p>
         </div>
         
          </div>
          </div>

      </div>
    </div>
  )};

export default Homepage;