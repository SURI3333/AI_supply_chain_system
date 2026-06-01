import KPIBox from "../components/KPIBox";
import AlertPanel from "../components/AlertPanel";
import ForecastChart from "../charts/ForecastChart";
import RiskChart from "../charts/RiskChart";

export default function Dashboard() {
  return (
    <div style={{ padding: "20px", background: "rgb(198, 245, 117)", minHeight: "100vh" }}>
      
      <h1 style={{ color: "white" }}>🚀 AI Supply Chain Dashboard</h1>

      {/* KPI Section */}
      <div style={{ display: "flex", gap: "20px", marginTop: "20px" }}>
        <KPIBox title="Total Stock" value="1200" />
        <KPIBox title="Predicted Demand" value="950" />
        <KPIBox title="Risk Score" value="Medium" />
      </div>

      {/* Charts Section */}
      <div style={{ display: "flex", gap: "50px", marginTop: "40px" }}>
        <ForecastChart />
        <RiskChart />
      </div>

      {/* Alerts */}
      <div style={{ marginTop: "30px" }}>
        <AlertPanel />
      </div>

    </div>
  );
}