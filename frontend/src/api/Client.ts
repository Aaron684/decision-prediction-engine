const API_BASE_URL = "http://localhost:8000";

async function request<T>(endpoint: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    headers: {
      "Content-Type": "application/json",
      ...(options?.headers ?? {}),
    },
    ...options,
  });

  if (!response.ok) {
    throw new Error(`API Error: ${response.status}`);
  }

  // DELETE endpoints usually return 204 No Content.
  if (response.status === 204) {
    return undefined as T;
  }

  return response.json();
}

export default request;
