import type { ReactNode } from "react";

interface FormFieldProps {
  label: string;
  children: ReactNode;
}

function FormField({ label, children }: FormFieldProps) {
  return (
    <div className="space-y-2">
      <label className="block text-sm font-medium text-slate-700">
        {label}
      </label>

      {children}
    </div>
  );
}

export default FormField;
