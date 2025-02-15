var express = require("express");
var bodyParser = require("body-parser");

var app = express();

var expressWs = require("express-ws")(app);
var index = require("./routes/index");

app.set("view engine", "pug");

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));
app.use("/", index);

app.get("/healthz", (req, res) => {
    res.status(200).send("OK");
});

app.listen(8000);
