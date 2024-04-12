
import React from 'react';

function RusselSage() {
  return (
    <div style={{ padding: '20px' }}>
      <h2>Russell Sage Dining Hall</h2>
      <p style={{ textAlign: 'center', marginTop: '-25px' }}>1649 15th St, Troy, NY 12180</p>
      <select name="simpleDropdown" id="simpleDropdown">
        <option value="option1">Breakfast</option>
        <option value="option4">Brunch</option>
        <option value="option2">Lunch</option>
        <option value="option3">Dinner</option>
      </select>
    </div>
  );
}

export default RusselSage;
