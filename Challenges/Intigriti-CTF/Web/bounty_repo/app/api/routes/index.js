const express = require("express");

const router = express.Router();
const database = require("../config/database");

db = database.initializeDatabase();

router.get("/", function (_req, res, _next) {
    db.all(
        "SELECT * FROM bug_reports WHERE LOWER(severity) != 'critical';;",
        function (error, result) {
            if (error) {
                res.status(500).send({
                    status: "Error",
                    message: "Internal Server Error",
                });
            } else if (result.length == 0) {
                res.status(404).send({
                    status: "ERROR",
                    message: "Report not found!",
                });
            } else {
                res.status(200);
                res.render("index.pug", { data: result });
            }
        }
    );
});

router.ws("/ws", function (ws, _req) {
    ws.on("message", function (msg) {
        if (msg == "__ping__") {
            ws.send("__pong__");
            return;
        }
        try {
            bug = JSON.parse(msg);
            query = `SELECT * FROM bug_reports WHERE id=${bug.id};`;
            console.log(query);
            db.get(query, function (error, result) {
                if (error) {
                    ws.send(
                        '{"message": "<span class=purple>Ooops.. something went wrong!</span>"}'
                    );
                } else if (!result) {
                    ws.send(
                        '{"message": "<span class=blue>Bug not found!</span>"}'
                    );
                } else if (result.status) {
                    ws.send(
                        `{"message": "<span class=${result.status.toLowerCase()}>Bug report from ${
                            result.reported_by
                        } is ${result.status}</span>"}`
                    );
                }
            });
        } catch (e) {
            ws.send('{"message":"Error!"}');
        }
    });
});

module.exports = router;
