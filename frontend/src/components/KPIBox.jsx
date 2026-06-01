import { motion } from "framer-motion";

export default function KPIBox({ title, value }) {
  return (
    <motion.div
      whileHover={{ scale: 1.05 }}
      style={{
        padding: "20px",
        background: "rgb(70, 109, 164)",
        color: "white",
        borderRadius: "10px",
        width: "200px"
      }}
    >
      <h4>{title}</h4>
      <h2>{value}</h2>
    </motion.div>
  );
}
