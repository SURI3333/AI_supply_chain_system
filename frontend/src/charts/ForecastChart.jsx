import { useEffect, useState } from "react";
import { getForecast } from "../api/api";
import { LineChart, Line, XAxis, YAxis, Tooltip } from "recharts";

export default function ForecastChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    getForecast().then(res => setData(res.data));
  }, []);

  return (
    <div>
      <h3>📊 Demand Forecast</h3>
      <LineChart width={500} height={300} data={data}>
        <XAxis dataKey="ds" />
        <YAxis />
        <Tooltip />
        <Line dataKey="yhat" stroke="#4ade80" />
      </LineChart>
    </div>
  );
}