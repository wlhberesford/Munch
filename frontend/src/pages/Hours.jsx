import React from 'react';

function Hours() {
  return (
    <div className="hours-of-operations">
      <h1>Dining Hours</h1>
      <div className="dining-location">
        <h3>BARH</h3>
        <p><strong>Breakfast:</strong> 7:00 AM - 10:00 AM</p>
        <p><strong>Lunch:</strong> 11:00 AM - 2:00 PM</p>
        <p><strong>Dinner:</strong> 5:00 PM - 8:00 PM</p>
      </div>
      <div className="dining-location">
        <h3>Commons</h3>
        <p><strong>Breakfast:</strong> 6:30 AM - 9:30 AM</p>
        <p><strong>Lunch:</strong> 11:30 AM - 1:30 PM</p>
        <p><strong>Dinner:</strong> 4:30 PM - 7:30 PM</p>
      </div>
      <div className="dining-location">
        <h3>Blitman</h3>
        <p><strong>Breakfast:</strong> 7:30 AM - 10:30 AM</p>
        <p><strong>Lunch:</strong> 12:00 PM - 3:00 PM</p>
        <p><strong>Dinner:</strong> 6:00 PM - 9:00 PM</p>
      </div>
      <div className="dining-location">
        <h3>Russel Sage</h3>
        <p><strong>Breakfast:</strong> 8:00 AM - 11:00 AM</p>
        <p><strong>Lunch:</strong> 12:00 PM - 2:00 PM</p>
        <p><strong>Dinner:</strong> 5:00 PM - 7:00 PM</p>
      </div>
    </div>
  );
}

export default Hours;
