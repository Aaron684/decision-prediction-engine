import type { ReactNode } from "react";

import { useTabs } from "./Tabs";

interface TabButtonProps {
  value: string;
  children: ReactNode;
}

function TabButton({ value, children }: TabButtonProps) {
  const { activeTab, setActiveTab } = useTabs();

  const active = activeTab === value;

  return (
    <button
      onClick={() => setActiveTab(value)}
      className={`
        flex
        items-center
        gap-2
        rounded-t-xl
        px-5
        py-3
        text-sm
        font-medium
        transition-colors

        ${
          active
            ? "border-b-2 border-slate-800 text-slate-900"
            : "text-slate-500 hover:text-slate-900"
        }
      `}
    >
      {children}
    </button>
  );
}

export default TabButton;
