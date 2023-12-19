import geopandas as gpd
from flask import Blueprint, render_template, request, url_for

base = Blueprint("base", __name__)

@base.route("/")
def index():
    return render_template("index.html")
