
import React from 'react';

function Blitman() {
  return (
    <div style={{ padding: '20px' }}>
      <h2>Blitman Dining Hall</h2>
      <p style={{ textAlign: 'center', marginTop: '-25px' }}>1800 6th Ave, Troy, NY 12180</p>
      <select name="simpleDropdown" id="simpleDropdown">
        <option value="option1">Breakfast</option>
        <option value="option4">Brunch</option>
        <option value="option2">Lunch</option>
        <option value="option3">Dinner</option>
      </select>
    </div>
  );
}

export default Blitman;
