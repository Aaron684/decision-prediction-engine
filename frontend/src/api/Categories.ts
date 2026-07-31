import request from "./Client";

export interface Category {
  id: number;

  name: string;

  description: string;

  target_name: string;

  target_type: string;
}

export interface CategoryCreate {
  name: string;

  description: string;

  target_name: string;

  target_type: string;
}

export type CategoryUpdate = Partial<CategoryCreate>;

export async function getCategories(): Promise<Category[]> {
  return request<Category[]>("/categories/");
}

export async function getCategory(id: number): Promise<Category> {
  return request<Category>(`/categories/${id}`);
}

export async function createCategory(data: CategoryCreate): Promise<Category> {
  return request<Category>("/categories/", {
    method: "POST",
    body: JSON.stringify(data),
  });
}

export async function updateCategory(
  id: number,
  data: CategoryUpdate,
): Promise<Category> {
  return request<Category>(`/categories/${id}`, {
    method: "PUT",
    body: JSON.stringify(data),
  });
}

export async function deleteCategory(id: number): Promise<void> {
  await request<void>(`/categories/${id}`, {
    method: "DELETE",
  });
}
