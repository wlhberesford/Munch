
import React from 'react';

function Barh() {
  return (
    <div style={{ padding: '20px' }}>
      <h2>BARH Dining Hall</h2>
      <p style={{ textAlign: 'center', marginTop: '-25px' }}>100 Albright Ct, Troy, NY 12180</p>
      <select name="simpleDropdown" id="simpleDropdown">
        <option value="option1">Breakfast</option>
        <option value="option4">Brunch</option>
        <option value="option2">Lunch</option>
        <option value="option3">Dinner</option>
      </select>
    </div>
  );
}

export default Barh;
