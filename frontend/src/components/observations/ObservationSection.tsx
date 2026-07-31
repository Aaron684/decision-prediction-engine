import { useEffect, useState } from "react";

import { getObservations, type Observation } from "../../api/Observations";

import { getFeatures, type Feature } from "../../api/Features";

import Card from "../ui/Card";
import Section from "../ui/Section";

import ObservationForm from "./ObservationForm";
import ObservationTable from "./ObservationTable";

interface ObservationSectionProps {
  categoryId: number;
}

function ObservationSection({ categoryId }: ObservationSectionProps) {
  const [observations, setObservations] = useState<Observation[]>([]);

  const [features, setFeatures] = useState<Feature[]>([]);

  const [editingObservation, setEditingObservation] = useState<
    Observation | undefined
  >();

  const [loading, setLoading] = useState(true);

  async function loadData() {
    try {
      const [featureResult, observationResult] = await Promise.all([
        getFeatures(categoryId),
        getObservations(categoryId),
      ]);

      setFeatures(featureResult);

      setObservations(observationResult);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadData();
  }, [categoryId]);

  if (loading) {
    return <Card>Loading observations...</Card>;
  }

  return (
    <Section title="Observations">
      <ObservationForm
        categoryId={categoryId}
        features={features}
        observation={editingObservation}
        onSaved={() => {
          setEditingObservation(undefined);
          loadData();
        }}
        onCancel={() => setEditingObservation(undefined)}
      />

      <div className="mt-6">
        {observations.length === 0 ? (
          <Card>
            <p className="text-slate-500">No observations yet.</p>
          </Card>
        ) : (
          <ObservationTable
            features={features}
            observations={observations}
            onUpdated={loadData}
            onEdit={setEditingObservation}
          />
        )}
      </div>
    </Section>
  );
}

export default ObservationSection;
