import React from 'react';
import "/home/carlson/Desktop/code/phase-4/groupwork/SWIMMERS_CLUB_PROJECT/frontend/src/css/swimmers-reg.css";


function Swimmerslogin() {
  return (
    <div className="App">
      <div className="container">
        <div className="form-container login-container">
          <form>
            <h2>Login</h2>
            <input type="email" placeholder="Email" />
            <input type="password" placeholder="Password" />
            <button>Login</button>
          </form>
        </div>
        <div className="form-container register-container">
          <form>
            <h2>Register</h2>
            <input type="text" placeholder="Name" />
            <input type="email" placeholder="Email" />
            <input type="password" placeholder="Password" />
            <button>Register</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Swimmerslogin;