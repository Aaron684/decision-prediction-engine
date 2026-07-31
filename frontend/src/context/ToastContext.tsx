import {
  createContext,
  useContext,
  useMemo,
  useState,
  type ReactNode,
} from "react";

import ToastContainer from "../components/ui/ToastContainer";

export type ToastType = "success" | "error" | "info";

export interface ToastMessage {
  id: number;
  type: ToastType;
  message: string;
}

interface ToastContextValue {
  success: (message: string) => void;
  error: (message: string) => void;
  info: (message: string) => void;
}

const ToastContext = createContext<ToastContextValue | null>(null);

interface ToastProviderProps {
  children: ReactNode;
}

function ToastProvider({ children }: ToastProviderProps) {
  const [toasts, setToasts] = useState<ToastMessage[]>([]);

  function addToast(type: ToastType, message: string) {
    const id = Date.now();

    setToasts((current) => [
      ...current,
      {
        id,
        type,
        message,
      },
    ]);

    setTimeout(() => {
      setToasts((current) => current.filter((toast) => toast.id !== id));
    }, 3000);
  }

  const value = useMemo(
    () => ({
      success: (message: string) => addToast("success", message),

      error: (message: string) => addToast("error", message),

      info: (message: string) => addToast("info", message),
    }),
    [],
  );

  return (
    <ToastContext.Provider value={value}>
      {children}

      <ToastContainer toasts={toasts} />
    </ToastContext.Provider>
  );
}

export function useToast() {
  const context = useContext(ToastContext);

  if (!context) {
    throw new Error("useToast must be used inside ToastProvider.");
  }

  return context;
}

export default ToastProvider;
