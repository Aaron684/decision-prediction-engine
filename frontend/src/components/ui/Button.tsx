import type { ButtonHTMLAttributes, ReactNode } from "react";

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  children: ReactNode;
}

function Button({ children, className = "", ...props }: ButtonProps) {
  return (
    <button
      {...props}
      className={`
        rounded-xl
        bg-slate-800
        px-5
        py-2.5
        font-medium
        text-white
        transition
        hover:bg-slate-700
        active:scale-95
        disabled:cursor-not-allowed
        disabled:opacity-50
        disabled:hover:bg-slate-800
        ${className}
      `}
    >
      {children}
    </button>
  );
}

export default Button;
