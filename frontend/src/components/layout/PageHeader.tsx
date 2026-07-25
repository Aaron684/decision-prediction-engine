interface PageHeaderProps {
  title: string;
  subtitle?: string;
}

function PageHeader({ title, subtitle }: PageHeaderProps) {
  return (
    <div className="mb-8">
      <h1 className="text-4xl font-bold text-slate-800">{title}</h1>

      {subtitle && <p className="mt-2 text-slate-600">{subtitle}</p>}
    </div>
  );
}

export default PageHeader;
