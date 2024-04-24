import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/header';
import Footer from './components/footer';
import NavigationBar from './components/navbar';
import Commons from './pages/Commons';
import RusselSage from './pages/RusselSage';
import Barh from './pages/Barh';
import Blitman from './pages/Blitman';
import Hours from './pages/Hours';
import './theme.css'; 

function App() {
  return (
    <Router>
      <Header />
      <NavigationBar />
      <Routes>
        <Route path="/commons" element={<Commons />} />
        <Route path="/russelsage" element={<RusselSage />} />
        <Route path="/barh" element={<Barh />} />
        <Route path="/blitman" element={<Blitman />} />
        <Route path="/Hours" element={<Hours />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
