import React from "react";

function PastEvents() {
  return (
    <div className="ev">
      <div className="header ">
        <h1 className="h1">Past Events</h1>
        <p className="p text-secondary">
          Check out some of our previous events and their results.
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
                <h4>Winter Wonderland Swim</h4>
              </div>
              <div>
                <p>December 10, 2022 | 10am - 2pm | Aqua Swimmers Club Pool</p>
              </div>

              <p className="card-text">
                Our annual Winter Wonderland Swim event was a huge success, with
                swimmers of all ages enjoying the festive atmosphere and
                friendly competition.
              </p>
              <div>
                <button type="button" className="btn btn-primary">
                  View Results
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
                <h4>Spring Splash</h4>
              </div>
              <div>
                <p>April 22, 2023 | 9am - 3pm | Aqua Swimmers Club Pool</p>
              </div>
              <p className="card-text">
                Our Spring Splash event was a celebration of the new season,
                with swimmers showcasing their skills and enjoying the warm
                weather.
              </p>
              <div>
                <button type="button" className="btn btn-primary">
                  View Results
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
                <h4>Aqua Gala</h4>
              </div>
              <div>
                <p>
                  June 3, 2023 | 6pm - 10pm | Aqua Swimmers Club Banquet Hall
                </p>
              </div>
              <p className="card-text">
                Our annual Aqua Gala was a night to remember, celebrating the
                achievements of our swimmers and coaches with awards, dinner,
                and dancing.
              </p>
              <div>
                <button type="button" className="btn btn-primary">
                  View Results
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
export default PastEvents;
