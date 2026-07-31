import type { ChangeEvent, ReactNode } from "react";

interface SelectProps {
  value: string;
  onChange: (event: ChangeEvent<HTMLSelectElement>) => void;
  children: ReactNode;
  disabled?: boolean;
}

function Select({ value, onChange, children, disabled = false }: SelectProps) {
  return (
    <select
      value={value}
      onChange={onChange}
      disabled={disabled}
      className="
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
        focus:border-slate-500
      "
    >
      {children}
    </select>
  );
}

export default Select;
