from flask import render_template, Blueprint, request
from fav_bands import favourite_bands

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/page2")
def page2():
    return render_template("page3.html", favourite_bands = favourite_bands)

@my_view.route("/my_name", methods=["GET", "POST"])
def my_name():
    if request.method == "POST":
       new_band = request.form["added_map"]
     #  rating = int(request.form["added_rating"])
       feed_back = request.form["added_feedback"]
       favourite_bands.append({
        "Map": new_band,
    #   "Rating": Rating,
        "Feedback": feed_back,  
    })
    return render_template("page2.html")
