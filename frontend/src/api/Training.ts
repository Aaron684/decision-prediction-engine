import request from "./Client";

export interface TrainingResult {
  model_name: string;
  model_id: string;
  observation_count: number;
  primary_score: number;
}

export async function trainCategory(
  categoryId: number,
): Promise<TrainingResult> {
  return request<TrainingResult>(`/training/categories/${categoryId}`, {
    method: "POST",
  });
}

export interface ActiveModel {
  id: number;
  model_name: string;
  version: number;
  observation_count: number;
  primary_score: number;
  is_active: boolean;
}

export async function getActiveModel(
  categoryId: number,
): Promise<ActiveModel | null> {
  return request(`/training/categories/${categoryId}`);
}
