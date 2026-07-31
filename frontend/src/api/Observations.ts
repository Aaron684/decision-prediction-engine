import request from "./Client";

export interface ObservationFeature {
  id: number;
  name: string;
  data_type: string;
}

export interface ObservationValue {
  feature_id: number;
  value: string;
  feature: ObservationFeature;
}

export interface Observation {
  id: number;
  category_id: number;
  target_value: string;
  values: ObservationValue[];
}

export interface ObservationCreate {
  category_id: number;
  target_value: string;
  values: {
    feature_id: number;
    value: string;
  }[];
}

export async function getObservations(
  categoryId: number,
): Promise<Observation[]> {
  return request<Observation[]>(`/observations/?category_id=${categoryId}`);
}

export async function getObservation(id: number): Promise<Observation> {
  return request<Observation>(`/observations/${id}`);
}

export async function createObservation(
  data: ObservationCreate,
): Promise<Observation> {
  return request<Observation>("/observations/", {
    method: "POST",
    body: JSON.stringify(data),
  });
}

export async function updateObservation(
  id: number,
  data: ObservationCreate,
): Promise<Observation> {
  return request<Observation>(`/observations/${id}`, {
    method: "PUT",
    body: JSON.stringify(data),
  });
}

export async function deleteObservation(id: number): Promise<void> {
  await request<void>(`/observations/${id}`, {
    method: "DELETE",
  });
}
