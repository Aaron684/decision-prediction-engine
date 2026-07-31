import type { ReactNode } from "react";

import { useTabs } from "./Tabs";

interface TabPanelProps {
  value: string;
  children: ReactNode;
}

function TabPanel({ value, children }: TabPanelProps) {
  const { activeTab } = useTabs();

  if (activeTab !== value) {
    return null;
  }

  return <>{children}</>;
}

export default TabPanel;
