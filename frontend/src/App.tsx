import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Categories from "./pages/Categories";
import Tutorial from "./pages/Tutorial";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />

        <Route path="/categories" element={<Categories />} />

        <Route path="/help" element={<Tutorial />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
