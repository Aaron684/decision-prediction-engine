import type { ReactNode } from "react";
import Navbar from "./Navbar";

interface PageLayoutProps {
  children: ReactNode;
}

function PageLayout({ children }: PageLayoutProps) {
  return (
    <div className="min-h-screen bg-slate-50">
      <Navbar />

      <main className="mx-auto max-w-7xl p-8">{children}</main>
    </div>
  );
}

export default PageLayout;
