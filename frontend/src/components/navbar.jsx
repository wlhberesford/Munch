import React from 'react';
import { NavLink } from 'react-router-dom';

function NavigationBar() {
  return (
    <div className="navbar">
      <NavLink to="/commons" activeClassName="active">Commons</NavLink>
      <NavLink to="/russelsage" activeClassName="active">Russel Sage</NavLink>
      <NavLink to="/barh" activeClassName="active">BARH</NavLink>
      <NavLink to="/blitman" activeClassName="active">Blitman</NavLink>
    </div>
  );
}

export default NavigationBar;
