import React, { useEffect, useState } from "react";
import axios from "axios";
import { Line } from "react-chartjs-2";
import 'chart.js/auto';

function App() {
  const [metrics, setMetrics] = useState([]);

  useEffect(() => {
    const loadData = async () => {
      const res = await axios.get("http://localhost:8000/metrics");
      setMetrics(res.data.logs);
    };
    loadData();
    const interval = setInterval(loadData, 5000);
    return () => clearInterval(interval);
  }, []);

  const labels = metrics.map((m) => new Date(m[1]).toLocaleTimeString());
  const efficiency = metrics.map((m) => m[5]);

  return (
    <div style={{ padding: "30px" }}>
      <h2>🧠 AI Agent Traceability Dashboard</h2>
      <Line
        data={{
          labels,
          datasets: [
            {
              label: "Efficiency (1/response time)",
              data: efficiency,
              borderColor: "blue",
              fill: false,
            },
          ],
        }}
      />
    </div>
  );
}

export default App;
