import './App.css';


function App() {
  return (
    <div className="container-fluid">
      <div className="row">
        <div className = "col-md-5">
          <div className="border m-5"><p className="p-5 text-center">complaint management system</p></div>
          <div className="text text-center">A system provided to easily file a complaint. You can reach out and get an issue resolved today!</div>
          <hr></hr>
          <p className='text-center'>EST. 2023</p>
        </div>
        <div className = "div2 col-md-7">
          <span className='invisible'>cds</span>
          <div className='bg-white mr-4 ml-3 mt-4 mb-4'>
         <p className='pt-5 text-center'>Login as:</p>
         <hr className='mb-5 ml-5 mr-5'></hr>
         <div className='btn-lg p-5'>
          <p><button type="button" className='btnorange btn btn-lg btnbloc p-3'>Student</button></p>
          <p><button type="button" className='btnorange btn btn-lg btnbloc p-3'>Staff</button></p>
          <p><button type="button" className='btnorange btn btn-lg btnbloc p-3'>Admin</button></p>
          <span className='invisible'>cds</span>
         </div>
         <span className='invisible'>cds</span>
          </div>
          <span className='invisible'>cds</span></div>

      </div>
    </div>
  );
}

export default App;
