export default function AlertPanel() {
  return (
    <div style={{ background: "rgb(12, 66, 181)", color: "white", padding: "15px", borderRadius: "10px" }}>
      <h3>⚠️ Alerts</h3>
      <ul>
        <li>Warehouse W1 may face stockout</li>
        <li>High demand predicted</li>
      </ul>
    </div>
  );
}