import Button from "./Button";

interface ConfirmDialogProps {
  open: boolean;
  title: string;
  message: string;
  confirmText?: string;
  cancelText?: string;
  onConfirm: () => void;
  onCancel: () => void;
}

function ConfirmDialog({
  open,
  title,
  message,
  confirmText = "Confirm",
  cancelText = "Cancel",
  onConfirm,
  onCancel,
}: ConfirmDialogProps) {
  if (!open) {
    return null;
  }

  return (
    <div
      className="
        fixed
        inset-0
        z-50
        flex
        items-center
        justify-center
        bg-black/40
      "
    >
      <div
        className="
          w-full
          max-w-md
          rounded-2xl
          bg-white
          p-6
          shadow-xl
        "
      >
        <h2 className="text-xl font-semibold text-slate-800">{title}</h2>

        <p className="mt-3 text-slate-600">{message}</p>

        <div className="mt-6 flex justify-end gap-3">
          <Button
            className="bg-slate-500 hover:bg-slate-600"
            onClick={onCancel}
          >
            {cancelText}
          </Button>

          <Button onClick={onConfirm}>{confirmText}</Button>
        </div>
      </div>
    </div>
  );
}

export default ConfirmDialog;
