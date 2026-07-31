import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Tutorial from "./pages/Tutorial";
import Categories from "./pages/Categories";
import CategoryDetails from "./pages/CategoryDetails";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />

      <Route path="/help" element={<Tutorial />} />

      <Route path="/categories" element={<Categories />} />

      <Route path="/categories/:id" element={<CategoryDetails />} />
    </Routes>
  );
}

export default App;
