import type { Feature } from "../../api/Features";
import type { Observation } from "../../api/Observations";

import Card from "../ui/Card";

import ObservationRow from "./ObservationRow";

interface ObservationTableProps {
  features: Feature[];
  observations: Observation[];
  onUpdated: () => void;
  onEdit: (observation: Observation) => void;
}

function ObservationTable({
  features,
  observations,
  onUpdated,
  onEdit,
}: ObservationTableProps) {
  return (
    <Card>
      <div className="overflow-x-auto">
        <table className="w-full text-left">
          <thead>
            <tr className="border-b border-slate-200">
              {features.map((feature) => (
                <th
                  key={feature.id}
                  className="
                      px-4
                      py-3
                      text-sm
                      font-semibold
                      text-slate-700
                    "
                >
                  {feature.name}
                </th>
              ))}

              <th
                className="
                  px-4
                  py-3
                  text-sm
                  font-semibold
                  text-slate-700
                "
              >
                Target
              </th>

              <th
                className="
                  px-4
                  py-3
                  text-sm
                  font-semibold
                  text-slate-700
                "
              >
                Actions
              </th>
            </tr>
          </thead>

          <tbody>
            {observations.map((observation) => (
              <ObservationRow
                key={observation.id}
                observation={observation}
                features={features}
                onUpdated={onUpdated}
                onEdit={() => onEdit(observation)}
              />
            ))}
          </tbody>
        </table>
      </div>
    </Card>
  );
}

export default ObservationTable;
