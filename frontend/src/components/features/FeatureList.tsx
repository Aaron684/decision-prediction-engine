import type { Feature } from "../../api/Features";

import FeatureItem from "./FeatureItem";

interface FeatureListProps {
  features: Feature[];
  onUpdated: () => void;
}

function FeatureList({ features, onUpdated }: FeatureListProps) {
  if (features.length === 0) {
    return <p className="text-slate-500">No features have been created yet.</p>;
  }

  return (
    <div className="space-y-3">
      {features.map((feature) => (
        <FeatureItem key={feature.id} feature={feature} onUpdated={onUpdated} />
      ))}
    </div>
  );
}

export default FeatureList;
