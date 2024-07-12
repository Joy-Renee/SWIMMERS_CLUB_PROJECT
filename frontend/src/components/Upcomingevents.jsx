import React from "react";

function UpcomingEvents() {





    
  return (
    <div>
      <div className="header">
        <h1 className="h1">Upcoming Events</h1>
        <p className="p text-secondary">
          Check out our upcoming events and sign up to participate.
        </p>
      </div>
      <div>
        <div className="row ">
          <div className="card col-4 ">
            <img
              src="https://images.pexels.com/photos/1263425/pexels-photo-1263425.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
              className="card-img-top"
              alt="..."
            />
            <div className="card-body">
              <div>
                <h4>Summer Splash</h4>
              </div>
              <div>
                <p>July 27, 2024 | 10am - 4pm | Aqua Swimmers Club Pool</p>
              </div>

              <p className="card-text">
              Join us for a day of fun in the sun at our annual Summer Splash event. Enjoy swimming, games, and a BBQ lunch.
              </p>
              <div>
                <button type="button" className="btn btn-primary">
                  register
                </button>
              </div>
            </div>
          </div>
          <div className="card col-4">
            <img
              src="https://images.pexels.com/photos/1263425/pexels-photo-1263425.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
              className="card-img-top"
              alt="..."
            />
            <div className="card-body">
              <div>
                <h4>Swim-a-Thon</h4>
              </div>
              <div>
                <p>July 27, 2024 | 10am - 4pm | Aqua Swimmers Club Pool</p>
              </div>
              <p className="card-text">
              Participate in our annual Swim-a-Thon fundraiser and help support our club's programs and scholarships.
              </p>
              <div>
                <button type="button" className="btn btn-primary">
                  register
                </button>
              </div>
            </div>
          </div>
          <div className="card col-4">
            <img
              src="https://images.pexels.com/photos/1263425/pexels-photo-1263425.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
              className="card-img-top"
              alt="..."
            />
            <div className="card-body">
              <div>
                <h4>Competitive Swim Mee</h4>
              </div>
              <div>
                <p>July 27, 2024 | 10am - 4pm | Aqua Swimmers Club Pool</p>
              </div>
              <p className="card-text">
              Join us for our annual competitive swim meet, featuring swimmers from clubs across the region.
              </p>
              <div>
                <button type="button" className="btn btn-primary">
                  register
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
export default UpcomingEvents;
