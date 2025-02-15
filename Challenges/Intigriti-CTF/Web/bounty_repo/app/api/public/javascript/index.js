$(document).ready(function () {
  open_ws();
  $("#id").on("keyup", function (_event) {
    bug_search();
  });
});

function bug_search() {
  var bug_id = $("#id").val();
  if (bug_id) {
    var msg = JSON.stringify({ id: bug_id });
    ws.send(msg);

    var rows = $("table tbody tr");
    rows.removeClass("highlight").css("color", "");
    rows.each(function () {
      var row = $(this);
      if (row.find("td:first-child").text() == bug_id) {
        row.addClass("highlight").css("color", "black");
      }
    });
  }
}

function open_ws() {
  var HOST = location.origin.replace(/^http/, "ws");
  console.log(HOST)
  window.ws = new WebSocket(HOST + "/ws");

  ws.onopen = function (_event) {
    setInterval(ping, 42000);
  };

  ws.onmessage = function (event) {
    if (event.data == "__pong__") {
      pong();
      return;
    }

    try {
      msg = JSON.parse(event.data);
      $("#res-container").html(msg.message);
    } catch (e) {
      $("#res-container").html(event.data);
    }
  };

  ws.onerror = function (event) {
    try {
      msg = JSON.parse(event.data);
      $("#res-container").text(msg.message);
    } catch (e) {
      $("#res-container").text(event.data);
    }
  };

  ws.onclose = function (_event) {
    console.log("Connection closed!");
  };
}

function ping() {
  ws.send("__ping__");
  tm = setTimeout(function () {}, 4200);
}

function pong() {
  clearTimeout(tm);
}
