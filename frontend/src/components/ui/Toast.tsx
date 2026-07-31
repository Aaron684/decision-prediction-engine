import type { ToastMessage } from "../../context/ToastContext";

interface ToastProps {
  toast: ToastMessage;
}

function Toast({ toast }: ToastProps) {
  const colors = {
    success: "bg-green-100 border-green-300 text-green-800",

    error: "bg-red-100 border-red-300 text-red-800",

    info: "bg-slate-100 border-slate-300 text-slate-800",
  };

  return (
    <div
      className={`
        rounded-xl
        border
        px-5
        py-3
        shadow-lg
        transition-all
        ${colors[toast.type]}
      `}
    >
      {toast.message}
    </div>
  );
}

export default Toast;
