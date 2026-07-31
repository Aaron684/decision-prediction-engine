import { useEffect, useState } from "react";

import { getFeatures, type Feature } from "../../api/Features";

import Card from "../ui/Card";
import Button from "../ui/Button";

import FeatureForm from "./FeatureForm";
import FeatureList from "./FeatureList";

interface FeatureSectionProps {
  categoryId: number;
}

function FeatureSection({ categoryId }: FeatureSectionProps) {
  const [features, setFeatures] = useState<Feature[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showForm, setShowForm] = useState(false);

  async function loadFeatures() {
    try {
      setLoading(true);
      setError(null);

      const result = await getFeatures(categoryId);

      setFeatures(result);
    } catch {
      setError("Unable to load features.");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadFeatures();
  }, [categoryId]);

  return (
    <Card>
      <div className="flex items-center justify-between">
        <h2 className="text-xl font-semibold text-slate-800">Features</h2>

        <Button onClick={() => setShowForm(!showForm)}>
          {showForm ? "Cancel" : "Add Feature"}
        </Button>
      </div>

      {showForm && (
        <div className="mt-6">
          <FeatureForm
            categoryId={categoryId}
            onCreated={() => {
              setShowForm(false);
              loadFeatures();
            }}
          />
        </div>
      )}

      <div className="mt-6">
        {loading ? (
          <p className="text-slate-500">Loading features...</p>
        ) : error ? (
          <p className="text-red-600">{error}</p>
        ) : (
          <FeatureList features={features} onUpdated={loadFeatures} />
        )}
      </div>
    </Card>
  );
}

export default FeatureSection;
