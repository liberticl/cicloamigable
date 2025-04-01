from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask, render_template, url_for, redirect, request
from config import NAVBAR_ITEMS, get_points
from utils import create_map, get_map_html


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)


# @app.before_request
# def force_https():
#     if not request.is_secure:
#         url = request.url.replace("http://", "https://", 1)
#         return redirect(url, code=301)


@app.route("/")
def home():
    return render_template("index.html", navbar_items=NAVBAR_ITEMS)

# @app.route("/licitaciones")
# def licitaciones():
#     return render_template("licitaciones.html", navbar_items=NAVBAR_ITEMS)


def update_icon_path(point):
    point["icon"] = f"{url_for('home', _external=True)}/static/{point['icon']}"
    return point


@app.route("/mapa")
def mapa():
    base_url = url_for('home', _external=True)
    points = get_points(base_url)
    this_map = create_map(points)
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
