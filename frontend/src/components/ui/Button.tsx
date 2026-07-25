import type { ReactNode } from "react";

interface ButtonProps {
  children: ReactNode;
  onClick?: () => void;
  className?: string;
}

function Button({ children, onClick, className = "" }: ButtonProps) {
  return (
    <button
      onClick={onClick}
      className={`
        rounded-xl
        bg-slate-800
        px-5
        py-2.5
        text-white
        font-medium
        transition
        hover:bg-slate-700
        active:scale-95
        ${className}
      `}
    >
      {children}
    </button>
  );
}

export default Button;
