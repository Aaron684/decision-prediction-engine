import request from "./Client";

export interface Feature {
  id: number;

  category_id: number;

  name: string;

  data_type: string;
}

export interface CreateFeatureRequest {
  category_id: number;

  name: string;

  data_type: string;
}

export interface UpdateFeatureRequest {
  name?: string;
}

export async function getFeatures(categoryId: number): Promise<Feature[]> {
  return request<Feature[]>(`/features/?category_id=${categoryId}`);
}

export async function getFeature(id: number): Promise<Feature> {
  return request<Feature>(`/features/${id}`);
}

export async function createFeature(
  data: CreateFeatureRequest,
): Promise<Feature> {
  return request<Feature>("/features", {
    method: "POST",

    body: JSON.stringify(data),
  });
}

export async function updateFeature(
  id: number,
  data: UpdateFeatureRequest,
): Promise<Feature> {
  return request<Feature>(`/features/${id}`, {
    method: "PUT",

    body: JSON.stringify(data),
  });
}

export async function deleteFeature(id: number): Promise<void> {
  await request<void>(`/features/${id}`, {
    method: "DELETE",
  });
}
