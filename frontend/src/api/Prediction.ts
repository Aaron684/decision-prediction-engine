import request from "./Client";

export interface PredictionRequest {
  values: Record<string, unknown>;
}

export interface FeatureContribution {
  feature_name: string;

  feature_value: unknown;

  importance: number;

  direction: string;
}

export interface PredictionExplanation {
  method: string;

  confidence: number;

  feature_contributions: FeatureContribution[];
}

export interface PredictionResult {
  prediction: unknown;

  explanation: PredictionExplanation;
}

export async function predictCategory(
  categoryId: number,
  data: PredictionRequest,
): Promise<PredictionResult> {
  return request<PredictionResult>(`/predict/categories/${categoryId}`, {
    method: "POST",

    body: JSON.stringify(data),
  });
}
