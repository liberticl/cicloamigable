from flask import Flask, render_template
from config import NAVBAR_ITEMS, POINTS, BASE_URL
from utils import create_map, get_map_html


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", navbar_items=NAVBAR_ITEMS)

# @app.route("/licitaciones")
# def licitaciones():
#     return render_template("licitaciones.html", navbar_items=NAVBAR_ITEMS)


def update_icon_path(point):
    # point["icon"] = url_for("static", filename=point["icon"], _external=True)
    point["icon"] = f"{BASE_URL}/static/{point['icon']}"
    return point


@app.route("/mapa")
def mapa():
    this_map = create_map(POINTS)
    content = get_map_html(this_map)
    return render_template("mapa.html",
                           navbar_items=NAVBAR_ITEMS,
                           map=content)


# @app.route("/presentacion")
# def presentacion():
#     return render_template("presentacion.html", navbar_items=NAVBAR_ITEMS)

@app.route("/login")
def login():
    return render_template("login.html", navbar_items=NAVBAR_ITEMS)


@app.route("/register")
def register():
    return render_template("register.html", navbar_items=NAVBAR_ITEMS)


@app.route("/proyecto")
def proyecto():
    return render_template("proyecto.html", navbar_items=NAVBAR_ITEMS)


@app.route("/actividades")
def actividades():
    return render_template("actividades.html", navbar_items=NAVBAR_ITEMS)


if __name__ == "__main__":
    app.run(debug=True)
