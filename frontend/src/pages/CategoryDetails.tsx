import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import { getCategory, type Category } from "../api/Categories";

import {
  getActiveModel,
  trainCategory,
  type ActiveModel,
} from "../api/Training";

import FeatureSection from "../components/features/FeatureSection";
import ObservationSection from "../components/observations/ObservationSection";
import PredictionSection from "../components/predictions/PredictionSection";

import PageLayout from "../components/layout/PageLayout";
import PageHeader from "../components/layout/PageHeader";

import Card from "../components/ui/Card";
import Tabs from "../components/ui/Tabs";
import TabList from "../components/ui/TabList";
import TabButton from "../components/ui/TabButton";
import TabPanel from "../components/ui/TabPanel";

import ModelPanel from "../components/models/ModelPanel";

import { useToast } from "../context/ToastContext";

import { Brain, ListTree, Table, Target } from "lucide-react";

function CategoryDetails() {
  const { id } = useParams();

  const { success, error: showError } = useToast();

  const [category, setCategory] = useState<Category | null>(null);

  const [activeModel, setActiveModel] = useState<ActiveModel | null>(null);

  const [loading, setLoading] = useState(true);

  const [training, setTraining] = useState(false);

  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadCategory() {
      if (!id) {
        setError("Invalid category.");

        setLoading(false);

        return;
      }

      try {
        const categoryId = Number(id);

        const [categoryResult, modelResult] = await Promise.all([
          getCategory(categoryId),
          getActiveModel(categoryId),
        ]);

        setCategory(categoryResult);

        setActiveModel(modelResult);
      } catch {
        setError("Unable to load category.");
      } finally {
        setLoading(false);
      }
    }

    loadCategory();
  }, [id]);

  async function handleTrain() {
    if (!id) return;

    try {
      setTraining(true);

      await trainCategory(Number(id));

      const updatedModel = await getActiveModel(Number(id));

      setActiveModel(updatedModel);

      success("Model trained successfully.");
    } catch (error) {
      console.error(error);

      showError("Unable to train model.");
    } finally {
      setTraining(false);
    }
  }

  if (loading) {
    return (
      <PageLayout>
        <PageHeader title="Category" subtitle="Loading..." />
      </PageLayout>
    );
  }

  if (error || !category) {
    return (
      <PageLayout>
        <PageHeader title="Category" subtitle="Something went wrong." />

        <Card>
          <p className="text-red-600">{error}</p>
        </Card>
      </PageLayout>
    );
  }

  return (
    <PageLayout>
      <PageHeader title={category.name} subtitle={category.description} />

      <Card>
        <div className="space-y-2">
          <p>
            <strong>Target:</strong> {category.target_name}
          </p>

          <p>
            <strong>Type:</strong> {category.target_type}
          </p>
        </div>
      </Card>

      <div className="mt-8">
        <Tabs defaultTab="features">
          <TabList>
            <TabButton value="features">
              <ListTree size={18} />
              Features
            </TabButton>

            <TabButton value="observations">
              <Table size={18} />
              Observations
            </TabButton>

            <TabButton value="models">
              <Brain size={18} />
              Models
            </TabButton>

            <TabButton value="predictions">
              <Target size={18} />
              Predictions
            </TabButton>
          </TabList>

          <TabPanel value="features">
            <FeatureSection categoryId={category.id} />
          </TabPanel>

          <TabPanel value="observations">
            <ObservationSection categoryId={category.id} />
          </TabPanel>

          <TabPanel value="models">
            <ModelPanel
              loading={training}
              hasModel={activeModel !== null}
              modelName={activeModel?.model_name}
              primaryScore={activeModel?.primary_score}
              observationCount={activeModel?.observation_count}
              onTrain={handleTrain}
            />
          </TabPanel>

          <TabPanel value="predictions">
            <PredictionSection categoryId={category.id} />
          </TabPanel>
        </Tabs>
      </div>
    </PageLayout>
  );
}

export default CategoryDetails;
