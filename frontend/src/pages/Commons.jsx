
import React from 'react';

function Commons() {
  return (
    <div style={{ padding: '20px' }}>
      <h2>Commons Dining Hall</h2>
      <p style={{ textAlign: 'center', marginTop: '-25px' }}>1999 Burdett Ave, Troy, NY, 12180</p>
      <select name="simpleDropdown" id="simpleDropdown">
        <option value="option1">Breakfast</option>
        <option value="option4">Brunch</option>
        <option value="option2">Lunch</option>
        <option value="option3">Dinner</option>
      </select>
      <div style={{ display: 'flex' }}>
        <div style={{ flex: 1, boxSizing: 'border-box', padding: '10px' }}>
          <h3>Grill</h3>
          <h4>Station Name</h4>
          <p>Meal</p>
          <p>Sides</p>
        </div>
      </div>
    </div>
  );
}

export default Commons;
