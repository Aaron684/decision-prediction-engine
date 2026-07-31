import { useState } from "react";

import { Pencil, Trash2 } from "lucide-react";

import { deleteFeature, updateFeature, type Feature } from "../../api/Features";

import { useToast } from "../../context/ToastContext";

import Card from "../ui/Card";
import Button from "../ui/Button";
import Badge from "../ui/Badge";
import ConfirmDialog from "../ui/ConfirmDialogue";
import FormField from "../ui/FormField";
import IconButton from "../ui/IconButton";
import TextInput from "../ui/TextInput";

interface FeatureItemProps {
  feature: Feature;
  onUpdated: () => void;
}

function FeatureItem({ feature, onUpdated }: FeatureItemProps) {
  const toast = useToast();

  const [editing, setEditing] = useState(false);

  const [showDeleteDialog, setShowDeleteDialog] = useState(false);

  const [name, setName] = useState(feature.name);

  const [loading, setLoading] = useState(false);

  async function handleSave() {
    try {
      setLoading(true);

      await updateFeature(feature.id, {
        name,
      });

      toast.success("Feature updated.");

      setEditing(false);

      onUpdated();
    } catch {
      toast.error("Unable to update feature.");
    } finally {
      setLoading(false);
    }
  }

  async function confirmDelete() {
    try {
      setLoading(true);

      await deleteFeature(feature.id);

      toast.success("Feature deleted.");

      setShowDeleteDialog(false);

      onUpdated();
    } catch {
      toast.error("Unable to delete feature.");
    } finally {
      setLoading(false);
    }
  }

  function handleCancel() {
    setName(feature.name);
    setEditing(false);
  }

  return (
    <>
      <Card>
        {editing ? (
          <div className="space-y-4">
            <FormField label="Feature Name">
              <TextInput
                value={name}
                onChange={(event) => setName(event.target.value)}
                disabled={loading}
              />
            </FormField>

            <div className="flex items-center gap-3">
              <Badge>{feature.data_type}</Badge>

              <span className="text-sm text-slate-500">
                Data type cannot be changed.
              </span>
            </div>

            <div className="flex gap-2">
              <Button onClick={handleSave} disabled={loading}>
                Save
              </Button>

              <Button onClick={handleCancel} disabled={loading}>
                Cancel
              </Button>
            </div>
          </div>
        ) : (
          <div className="flex items-center justify-between">
            <div>
              <h3 className="font-medium text-slate-800">{feature.name}</h3>

              <div className="mt-2">
                <Badge>{feature.data_type}</Badge>
              </div>
            </div>

            <div className="flex gap-2">
              <IconButton
                onClick={() => setEditing(true)}
                disabled={loading}
                title="Edit Feature"
              >
                <Pencil size={18} />
              </IconButton>

              <IconButton
                onClick={() => setShowDeleteDialog(true)}
                disabled={loading}
                title="Delete Feature"
              >
                <Trash2 size={18} />
              </IconButton>
            </div>
          </div>
        )}
      </Card>

      <ConfirmDialog
        open={showDeleteDialog}
        title="Delete Feature"
        message={`Are you sure you want to delete "${feature.name}"?`}
        confirmText="Delete"
        cancelText="Cancel"
        onConfirm={confirmDelete}
        onCancel={() => setShowDeleteDialog(false)}
      />
    </>
  );
}

export default FeatureItem;
