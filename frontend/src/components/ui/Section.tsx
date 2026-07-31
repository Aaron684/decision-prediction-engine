import type { ReactNode } from "react";

interface SectionProps {
  title: string;
  action?: ReactNode;
  children: ReactNode;
}

function Section({ title, action, children }: SectionProps) {
  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-xl font-semibold text-slate-800">{title}</h2>

        {action}
      </div>

      {children}
    </div>
  );
}

export default Section;
