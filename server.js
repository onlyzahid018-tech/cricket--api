const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());

app.get("/", (req, res) => {
  res.send("CricWin API Running");
});

app.get("/live", (req, res) => {
  res.json({
    match: "IND vs AUS",
    score: "145/3",
    overs: "16.2",
    status: "LIVE"
  });
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log("Server running");
});
