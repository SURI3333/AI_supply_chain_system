import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000"
});

export const getForecast = () => API.get("/forecast?days=30");
export const getRisk = () => API.get("/risk");
export const getAnomaly = () => API.get("/anomaly");
export const getOptimize = (stock, demand) =>
  API.get(`/optimize?stock=${stock}&demand=${demand}`);

export const getSimulation = () =>
  API.get(`/simulate?demand_increase=0.3&delay=3`);