import urllib.parse
from uuid import uuid4
from flask import Flask, render_template, render_template_string, request, redirect, url_for, flash, jsonify, session
import base64, os
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image, ImageFilter
import time


FLAG = os.environ.get("FLAG")
session_key = "Cl0wnk1n9M4d3Th1sCh4ll"

def body_guard(string):
    # flask SSTI filter 
    evil = ["{","<",">","'","\""]
    if any(x in string for x in evil):
        return False
    else:
        return True

def img2b64(url,mode=None):
    # open browser
    chromeOptions = webdriver.ChromeOptions() 
    chromeOptions.add_argument("--no-sandbox") 
    chromeOptions.add_argument("--remote-debugging-port=9222")
    chromeOptions.add_argument("--disable-dev-shm-usage")
    chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.add_argument("--start-maximized")

    driver = webdriver.Chrome("/chromedriver", options=chromeOptions)
    # access gooogle
    driver.get(url)
    print(driver.save_screenshot("ahihi.png"))
    driver.quit()

    # blur image
    im = Image.open("ahihi.png")
    if mode == "blur":
        im = im.filter(ImageFilter.GaussianBlur(radius=10))
    im.resize((400,400)).save("ahhi.png")

    f = open("ahihi.png", "rb")
    data = f.read()
    f.close()
    b64 = base64.b64encode(data).decode("utf-8")
    return b64

def highlỉne_markdown(string):
    return string.replace("[m:highlight]", "<span style='background-color:#00FEFE'>").replace("[/m:highlight]", "</span>")

def code_markdown(string):
    return string.replace("[m:code]", "<code>").replace("[/m:code]", "</code>")

def url_markdown(string):
    link = string.replace("[m:url]", "").replace("[/m:url]", "")
    return string.replace("[m:url]", "<a href='"+link+"' target='_blank'>").replace("[/m:url]", "</a>")

def screenshot_markdown(string):
    link = string.replace("[m:screenshot]", "").replace("[/m:screenshot]", "")
    data = img2b64(link)
    return string.replace("[m:screenshot]","<img src='data:image/png;base64,{}'/>".format(data)).replace("[/m:screenshot]", "")

def markdown(string):
    if "[m:highlight]" in string:
        string = highlỉne_markdown(string)
    elif "[m:code]" in string:
        string = code_markdown(string)
    elif "[m:url]" in string:
        string = url_markdown(string)
    elif "[m:screenshot]" in string:
        string = screenshot_markdown(string)
    else:
        pass
    return string

app = Flask(__name__)
# get secret key from enviroment
app.secret_key = session_key


# @app.route('/')
# def index():
#     return render_template_string(markdown(string))

@app.route('/')
def index():
    if "username" in session:
        return render_template("ahihi.html")
    else:
        return redirect(url_for("setuser"))

@app.route("/setuser", methods=["GET"])
def setuser():
    if request.method == "GET":
        if request.args.get("username") and request.args.get("username") != "admin":
            session["username"] = request.args.get("username")
            return redirect(url_for("index"))
        else:
            return render_template("index.html")

@app.route('/note',methods=["POST","GET"])

def note():
    # check username in currnet session
    if "username" in session:
        # get POST data
        if request.method == "POST":
            note = request.form.get("note")
            if not body_guard(note):
                render_template_string("WAF Block your request")
        if session["username"] == "admin":
           return render_template_string(FLAG) 
        return render_template_string(markdown(note))
    else:
        flash('You are not authorized to view this page')
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run("0.0.0.0",8888,debug=False)




