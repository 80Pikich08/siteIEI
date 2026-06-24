import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "/api",
});

const PUBLIC_ENDPOINTS = [
  "/accounts/login/",
  "/accounts/register/",
  "/accounts/token/refresh/",
];

api.interceptors.request.use((config) => {
  const isPublicEndpoint = PUBLIC_ENDPOINTS.some((endpoint) =>
    config.url?.includes(endpoint)
  );

  if (isPublicEndpoint) {
    return config;
  }

  const token = localStorage.getItem("access");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

export default api;