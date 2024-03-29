import os
import json
from flask import Flask, render_template, request, flash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        #  print(request.form) - prints all form data on terminal / throws NONE if there is no key
        #  print(request.form.get("name")) OR request.form["name"]- gets name from form (form is a DICTIONARY) / throws EXCEPTION if there's no key
        flash("Thanks {}, We've received your message and will get back ASAP".format(request.form.get("name")))
    return render_template("contact.html", page_title="Contact Us!")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Come Work With Us!")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True # MUST CHANGE to False before submission/ PRODUCTION
    )
