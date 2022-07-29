from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    title = "Homepage"	
    return render_template("index.html", title=title)

@app.route("/about")
def about():
    title = "About"	
    return render_template("about.html",title=title)

@app.route("/contact")
def contact():
    title = "Contact"	
    return render_template("contact.html",title=title)