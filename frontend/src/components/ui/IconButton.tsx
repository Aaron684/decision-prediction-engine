import type {
  ButtonHTMLAttributes,
  ReactNode,
} from "react";

interface IconButtonProps
  extends ButtonHTMLAttributes<HTMLButtonElement> {
  children: ReactNode;
}

function IconButton({
  children,
  className = "",
  ...props
}: IconButtonProps) {
  return (
    <button
      {...props}
      className={`
        rounded-lg
        p-2
        text-slate-600
        transition
        hover:bg-slate-100
        hover:text-slate-900
        disabled:opacity-50
        ${className}
      `}
    >
      {children}
    </button>
  );
}

export default IconButton;