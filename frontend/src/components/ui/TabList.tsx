import type { ReactNode } from "react";

interface TabListProps {
  children: ReactNode;
}

function TabList({ children }: TabListProps) {
  return (
    <div
      className="
        mb-6
        flex
        gap-2
        border-b
        border-slate-200
      "
    >
      {children}
    </div>
  );
}

export default TabList;
