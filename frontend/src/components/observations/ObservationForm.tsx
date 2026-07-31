import { useEffect, useState } from "react";

import type { Feature } from "../../api/Features";

import {
  createObservation,
  updateObservation,
  type Observation,
  type ObservationCreate,
} from "../../api/Observations";

import { useToast } from "../../context/ToastContext";

import Button from "../ui/Button";
import Card from "../ui/Card";
import FormField from "../ui/FormField";
import TextInput from "../ui/TextInput";
import Select from "../ui/Select";

interface ObservationFormProps {
  categoryId: number;
  features: Feature[];
  observation?: Observation;
  onSaved: () => void;
  onCancel?: () => void;
}

function ObservationForm({
  categoryId,
  features,
  observation,
  onSaved,
  onCancel,
}: ObservationFormProps) {
  const toast = useToast();

  const [values, setValues] = useState<Record<number, string>>({});

  const [targetValue, setTargetValue] = useState("");

  const [loading, setLoading] = useState(false);

  const editing = observation !== undefined;

  useEffect(() => {
    if (!observation) {
      setValues({});
      setTargetValue("");
      return;
    }

    const existingValues = observation.values.reduce(
      (result, item) => {
        result[item.feature_id] = item.value;

        return result;
      },
      {} as Record<number, string>,
    );

    setValues(existingValues);

    setTargetValue(observation.target_value);
  }, [observation]);

  function updateValue(featureId: number, value: string) {
    setValues((previous) => ({
      ...previous,
      [featureId]: value,
    }));
  }
  function validate(): string | null {
    for (const feature of features) {
      const value = values[feature.id];

      if (!value || value.trim() === "") {
        return `${feature.name} is required.`;
      }

      if (feature.data_type === "numeric" && isNaN(Number(value))) {
        return `${feature.name} must be a number.`;
      }
    }

    if (!targetValue || targetValue.trim() === "") {
      return "Target value is required.";
    }

    return null;
  }
  async function handleSubmit() {
    const error = validate();

if (error) {

    toast.error(error);

    return;

}
    try {
      setLoading(true);

      const payload: ObservationCreate = {
        category_id: categoryId,

        target_value: targetValue,

        values: features.map((feature) => ({
          feature_id: feature.id,
          value: values[feature.id] ?? "",
        })),
      };

      if (editing) {
        await updateObservation(observation.id, payload);

        toast.success("Observation updated.");
      } else {
        await createObservation(payload);

        toast.success("Observation created.");
      }

      setValues({});

      setTargetValue("");

      onSaved();
    } catch {
      toast.error("Unable to save observation.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <Card>
      <div className="space-y-5">
        {features.map((feature) => (
          <FormField key={feature.id} label={feature.name}>
            {feature.data_type === "boolean" ? (
              <Select
                value={values[feature.id] ?? ""}
                onChange={(event) =>
                  updateValue(feature.id, event.target.value)
                }
                disabled={loading}
              >
                <option value="">Select value</option>

                <option value="true">True</option>

                <option value="false">False</option>
              </Select>
            ) : (
              <TextInput
                value={values[feature.id] ?? ""}
                onChange={(event) =>
                  updateValue(feature.id, event.target.value)
                }
                disabled={loading}
              />
            )}
          </FormField>
        ))}

        <FormField label="Target">
          <TextInput
            value={targetValue}
            onChange={(event) => setTargetValue(event.target.value)}
            disabled={loading}
          />
        </FormField>

        <div className="flex gap-3">
          <Button onClick={handleSubmit} disabled={loading}>
            {editing ? "Save Changes" : "Add Observation"}
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

export default ObservationForm;
