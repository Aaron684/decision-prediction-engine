import type { InputHTMLAttributes } from "react";

interface TextInputProps extends InputHTMLAttributes<HTMLInputElement> {}

function TextInput({ className = "", ...props }: TextInputProps) {
  return (
    <input
      {...props}
      className={`
        w-full
        rounded-xl
        border
        border-slate-300
        bg-white
        px-4
        py-2.5
        text-slate-800
        outline-none
        transition
        focus:border-slate-800
        focus:ring-2
        focus:ring-slate-200
        ${className}
      `}
    />
  );
}

export default TextInput;
