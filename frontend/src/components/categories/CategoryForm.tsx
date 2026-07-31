import { useEffect, useState } from "react";

import {
  createCategory,
  updateCategory,
  type Category,
  type CategoryCreate,
} from "../../api/Categories";

import { useToast } from "../../context/ToastContext";

import Button from "../ui/Button";
import Card from "../ui/Card";
import FormField from "../ui/FormField";
import TextInput from "../ui/TextInput";
import Select from "../ui/Select";

interface CategoryFormProps {
  category?: Category;

  onSaved: () => void;

  onCancel?: () => void;
}

function CategoryForm({ category, onSaved, onCancel }: CategoryFormProps) {
  const toast = useToast();

  const editing = category !== undefined;

  const [form, setForm] = useState<CategoryCreate>({
    name: "",
    description: "",
    target_name: "",
    target_type: "classification",
  });

  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (category) {
      setForm({
        name: category.name,
        description: category.description,
        target_name: category.target_name,
        target_type: category.target_type,
      });
    } else {
      setForm({
        name: "",
        description: "",
        target_name: "",
        target_type: "classification",
      });
    }
  }, [category]);

  function updateField(field: keyof CategoryCreate, value: string) {
    setForm((previous) => ({
      ...previous,
      [field]: value,
    }));
  }

  async function handleSubmit() {
    if (!form.name || !form.target_name) {
      toast.error("Name and target are required.");

      return;
    }

    try {
      setLoading(true);

      if (editing) {
        await updateCategory(category.id, {
          name: form.name,
          description: form.description,
          target_name: form.target_name,
        });

        toast.success("Category updated.");
      } else {
        await createCategory(form);

        toast.success("Category created.");
      }

      onSaved();
    } catch {
      toast.error("Unable to save category.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <Card>
      <div className="space-y-5">
        <FormField label="Name">
          <TextInput
            value={form.name}
            onChange={(event) => updateField("name", event.target.value)}
            disabled={loading}
          />
        </FormField>

        <FormField label="Description">
          <TextInput
            value={form.description}
            onChange={(event) => updateField("description", event.target.value)}
            disabled={loading}
          />
        </FormField>

        <FormField label="Target Name">
          <TextInput
            value={form.target_name}
            onChange={(event) => updateField("target_name", event.target.value)}
            disabled={loading}
          />
        </FormField>

        <FormField label="Target Type">
          <Select
            value={form.target_type}
            disabled={editing || loading}
            onChange={(event) => updateField("target_type", event.target.value)}
          >
            <option value="classification">Classification</option>

            <option value="regression">Regression</option>
          </Select>
        </FormField>

        <div className="flex gap-3">
          <Button onClick={handleSubmit} disabled={loading}>
            {editing ? "Save Changes" : "Create Category"}
          </Button>

          {editing && onCancel && (
            <Button onClick={onCancel} disabled={loading}>
              Cancel
            </Button>
          )}
        </div>
      </div>
    </Card>
  );
}

export default CategoryForm;
