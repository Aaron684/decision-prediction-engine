import { useEffect, useState } from "react";

import { getFeatures, type Feature } from "../../api/Features";

import { predictCategory, type PredictionResult } from "../../api/Prediction";

import Card from "../ui/Card";
import Button from "../ui/Button";

import { useToast } from "../../context/ToastContext";

interface PredictionSectionProps {
  categoryId: number;
}

function PredictionSection({ categoryId }: PredictionSectionProps) {
  const [features, setFeatures] = useState<Feature[]>([]);

  const [values, setValues] = useState<Record<string, unknown>>({});

  const [result, setResult] = useState<PredictionResult>();

  const [loading, setLoading] = useState(false);

  const { success, error } = useToast();

  useEffect(() => {
    async function loadFeatures() {
      try {
        const data = await getFeatures(categoryId);

        setFeatures(data);

        const defaults: Record<string, unknown> = {};

        data.forEach((feature) => {
          if (feature.data_type === "boolean") {
            defaults[feature.name] = false;
          }
        });

        setValues(defaults);
      } catch {
        error("Unable to load features.");
      }
    }

    loadFeatures();
  }, [categoryId]);

  function updateValue(name: string, value: unknown) {
    setValues((current) => ({
      ...current,
      [name]: value,
    }));
  }

  async function handlePredict() {
    try {
      setLoading(true);

      const prediction = await predictCategory(categoryId, {
        values,
      });

      setResult(prediction);

      success("Prediction generated.");
    } catch {
      error("Unable to generate prediction.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-6">
      <Card>
        <div className="space-y-5">
          <h2 className="text-xl font-semibold">Make Prediction</h2>

          {features.map((feature) => (
            <div key={feature.id} className="space-y-1">
              <label className="text-sm font-medium">{feature.name}</label>

              {feature.data_type === "numeric" ? (
                <input
                  type="number"
                  className="w-full rounded-lg border px-3 py-2"
                  onChange={(e) =>
                    updateValue(feature.name, Number(e.target.value))
                  }
                />
              ) : (
                <select
                  className="w-full rounded-lg border px-3 py-2"
                  onChange={(e) =>
                    updateValue(feature.name, e.target.value === "true")
                  }
                >
                  <option value="true">True</option>

                  <option value="false">False</option>
                </select>
              )}
            </div>
          ))}

          <Button onClick={handlePredict} disabled={loading}>
            {loading ? "Predicting..." : "Predict"}
          </Button>
        </div>
      </Card>

      {result && (
        <Card>
          <div className="space-y-5">
            <h2 className="text-xl font-semibold">Prediction Result</h2>

            <p>
              <strong>Prediction:</strong> {String(result.prediction)}
            </p>

            <p>
              <strong>Method:</strong> {result.explanation.method}
            </p>

            <p>
              <strong>Confidence:</strong>{" "}
              {(result.explanation.confidence * 100).toFixed(1)}%
            </p>

            <div>
              <h3 className="font-semibold mb-3">Feature Contributions</h3>

              <div className="space-y-2">
                {result.explanation.feature_contributions.map((item) => (
                  <div
                    key={item.feature_name}
                    className="border rounded-lg p-3"
                  >
                    <p>
                      <strong>{item.feature_name}</strong>
                    </p>

                    <p>Value: {String(item.feature_value)}</p>

                    <p>Importance: {item.importance.toFixed(3)}</p>

                    <p>Direction: {item.direction}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </Card>
      )}
    </div>
  );
}

export default PredictionSection;
