import { Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar/Navbar";
import Footer from "./components/footer/Footer";

import Home from "./page/Home";
import Recommendation from "./page/Recommendation";
import Package from "./page/Package";
import About from "./page/About";
import NotFound from "./page/NotFound";

function App(){
  return(
    <>
        <Navbar />

            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/recommendation" element={<Recommendation />} />
              <Route path="/package/:id" element={<Package />} />
              <Route path="/about" element={<About />} />
              <Route path="*" element={<NotFound />} />
            </Routes>

        <Footer />
    </>
  );
}

export default App;

