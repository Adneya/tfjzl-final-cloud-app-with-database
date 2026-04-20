const express = require("express");
const path = require("path");

const app = express();
const port = process.env.PORT || 3000;

app.get("/", (_req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

app.get("/v1", (_req, res) => {
  res.sendFile(path.join(__dirname, "index.default.html"));
});

app.listen(port, () => {
  console.log(`Guestbook server running on port ${port}`);
});
