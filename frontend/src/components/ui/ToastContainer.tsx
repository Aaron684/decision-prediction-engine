import type { ToastMessage } from "../../context/ToastContext";

import Toast from "./Toast";

interface ToastContainerProps {
  toasts: ToastMessage[];
}

function ToastContainer({ toasts }: ToastContainerProps) {
  return (
    <div
      className="
        fixed
        right-6
        top-6
        z-50
        flex
        flex-col
        gap-3
      "
    >
      {toasts.map((toast) => (
        <Toast key={toast.id} toast={toast} />
      ))}
    </div>
  );
}

export default ToastContainer;
