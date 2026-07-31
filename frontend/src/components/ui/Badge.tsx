interface BadgeProps {
  children: React.ReactNode;
}

function Badge({ children }: BadgeProps) {
  return (
    <span
      className="
        rounded-full
        bg-slate-100
        px-3
        py-1
        text-xs
        font-medium
        uppercase
        tracking-wide
        text-slate-600
      "
    >
      {children}
    </span>
  );
}

export default Badge;
