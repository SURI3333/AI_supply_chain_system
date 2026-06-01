import { useEffect, useState } from "react";
import { getRisk } from "../api/api";
import { BarChart, Bar, XAxis, YAxis, Tooltip } from "recharts";

export default function RiskChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    getRisk().then(res => {
      const formatted = res.data.map((r, i) => ({
        id: i,
        risk: r[1]
      }));
      setData(formatted);
    });
  }, []);

  return (
    <div>
      <h3>⚠️ Risk Prediction</h3>
      <BarChart width={400} height={300} data={data}>
        <XAxis dataKey="id" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="risk" fill="#f87171" />
      </BarChart>
    </div>
  );
}