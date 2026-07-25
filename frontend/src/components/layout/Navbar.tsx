import { NavLink } from "react-router-dom";

function Navbar() {
  const linkClasses = ({ isActive }: { isActive: boolean }) =>
    `transition-colors ${
      isActive
        ? "text-slate-900 font-semibold"
        : "text-slate-500 hover:text-slate-900"
    }`;

  return (
    <nav className="border-b border-slate-200 bg-white">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-8 py-4">
        <NavLink to="/" className="text-xl font-bold text-slate-800">
          Decision Engine
        </NavLink>

        <div className="flex items-center gap-8">
          <NavLink to="/" className={linkClasses}>
            Home
          </NavLink>

          <NavLink to="/categories" className={linkClasses}>
            Categories
          </NavLink>

          <NavLink to="/help" className={linkClasses}>
            Help
          </NavLink>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
