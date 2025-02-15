const express = require("express");
const puppeteer = require("puppeteer");

const app = express();
const PORT = 3001;

const bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({ extended: true }));

const browser_options = {
  headless: true,
  ignoreHTTPSErrors: true,
  args: [
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-background-networking",
    "--disable-default-apps",
    "--disable-extensions",
    "--disable-gpu",
    "--disable-sync",
    "--disable-translate",
    "--mute-audio",
    "--hide-scrollbars",
    "--metrics-recording-only",
    "--no-first-run",
    "--safebrowsing-disable-auto-update",
    "--js-flags=--noexpose_wasm,--jitless",
    "--ignore-certificate-errors",
  ],
};

const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

const viewMeme = async (url) => {
  const browser = await puppeteer.launch(browser_options);
  try {
    let page = await browser.newPage();
    await page.bringToFront();

    console.log(`Admin logging in @ ${process.env.BOT_LOGIN_URL}`);

    await page.goto(process.env.BOT_LOGIN_URL, {
      waitUntil: "networkidle2",
      timeout: 50000,
    });

    await page.type("#username", process.env.ADMIN_USERNAME);
    await page.type("#password", process.env.ADMIN_PASSWORD);
    await page.click("#submit");
    await sleep(500);
    await page.setCookie({
      name: "FLAG",
      value: process.env.FLAG,
    });

    console.log(`Admin watching meme @ ${url}`);
    await page.goto(url, {
      waitUntil: "networkidle2",
      timeout: 50000,
    });
    await sleep(1000);

    await page.close();
    return true;
  } catch (e) {
    console.log(e);
  } finally {
    await browser.close();
  }
  return false;
};

app.post("/show", async (req, res) => {
  const body = req.body;
  const visited = await viewMeme(body.url);
  if (visited) {
    res.status = 200;
    res.send("Haha!");
  } else {
    res.status = 500;
    res.send("broken");
  }
  res.end();
});

app.get("/ping", async (req, res) => {
  res.status = 200;
  res.send("Pong");
  res.end();
});

app.listen(PORT, (e) => {
  if (e) console.log(e);
  else console.log("Server listening on PORT", PORT);
});
