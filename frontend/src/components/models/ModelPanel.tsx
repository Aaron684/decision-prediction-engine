import Button from "../ui/Button";
import Card from "../ui/Card";

interface ModelPanelProps {
  loading: boolean;

  hasModel: boolean;

  modelName?: string;

  primaryScore?: number;

  observationCount?: number;

  onTrain: () => void;
}

function ModelPanel({
  loading,
  hasModel,
  modelName,
  primaryScore,
  observationCount,
  onTrain,
}: ModelPanelProps) {
  return (
    <Card>
      <div className="space-y-6">
        <div>
          <h2 className="text-xl font-semibold text-slate-800">
            Machine Learning
          </h2>

          <p className="mt-1 text-slate-500">
            Train the best model for this category.
          </p>
        </div>

        {!hasModel ? (
          <>
            <p className="text-slate-600">
              No trained model exists for this category.
            </p>

            <Button onClick={onTrain} disabled={loading}>
              {loading ? "Training..." : "Train Best Model"}
            </Button>
          </>
        ) : (
          <>
            <div className="space-y-2 text-sm text-slate-700">
              <p>
                <strong>Active Model:</strong> {modelName}
              </p>

              <p>
                <strong>Primary Score:</strong> {primaryScore?.toFixed(3)}
              </p>

              <p>
                <strong>Training Samples:</strong> {observationCount}
              </p>
            </div>

            <Button onClick={onTrain} disabled={loading}>
              {loading ? "Training..." : "Retrain Model"}
            </Button>
          </>
        )}
      </div>
    </Card>
  );
}

export default ModelPanel;
