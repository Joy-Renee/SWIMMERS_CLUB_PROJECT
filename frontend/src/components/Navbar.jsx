import React from "react";

function Navbar() {
  return (
    <nav class="navbar navbar-expand-lg navbar-light bg-primary">
      <div class="container-fluid">
        <a class="navbar-brand text-white" href="#">
          Aqua Swimming Club
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link active text-white" aria-current="page" href="#">
                Home
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link text-white" href="#">
                Events
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link text-white" href="#">
                Register
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link text-white" href="#">
                About
              </a>
            </li>
            
          </ul>
        </div>
      </div>
    </nav>
  );
}
export default Navbar;
