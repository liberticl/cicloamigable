# from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask, render_template, url_for, request
from config import NAVBAR_ITEMS, VLPO_CICLOAMIGABLE, MEMT, FNB, get_points
from utils import (create_map, create_memt_map, create_fnb_map, get_html,
                   get_city_info, get_fnb_services_types, get_service_info)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", navbar_items=NAVBAR_ITEMS)


def update_icon_path(point):
    point["icon"] = f"{url_for('home', _external=True)}/static/{point['icon']}"
    return point


@app.route("/mapa")
def mapa():
    # base_url = 'https://www.cicloamigable.cl' if PROD else 'http://localhost:5000' # noqa
    base_url = url_for('static', filename='img')
    points = get_points(VLPO_CICLOAMIGABLE, base_url)
    this_map = create_map(points)
    headers, deckgl = get_html(this_map)
    return render_template("mapa.html",
                           navbar_items=NAVBAR_ITEMS,
                           headers=headers,
                           map=deckgl)


@app.route("/memt")
def memt():
    base_url = url_for('static', filename='img')
    points = get_points(MEMT, base_url)

    selected = request.args.get('city', None)
    selected_year = request.args.get('year', None)

    city_info = get_city_info(selected, points)

    if selected_year and selected_year.isdigit():
        selected_year = int(selected_year)
    elif city_info:
        selected_year = city_info[0].get('year')

    if selected_year and selected:
        # Filter points so the map only draws lines for the selected year (for the selected city)
        # We keep points from other cities intact to show them globally if needed.
        city_name = selected.replace(' ', '').split('(')[0]
        map_points = [p for p in points if p['city'] != city_name or p.get('year') == selected_year]
    else:
        map_points = points

    this_map = create_memt_map(map_points, city=selected)
    headers, deckgl = get_html(this_map)

    cities = sorted(list({f"{point['city']} ({point['country']})" for point in points})) # noqa
    return render_template("memt.html",
                           navbar_items=NAVBAR_ITEMS,
                           headers=headers,
                           map=deckgl,
                           cities=cities,
                           selected=selected,
                           selected_year=selected_year,
                           city_info=city_info)


@app.route("/fnb")
def fnb():
    base_url = url_for('static', filename='img')
    points = get_points(FNB, base_url)
    types = get_fnb_services_types(points)

    selected = request.args.get('service', None)
    to_show = get_service_info(selected, points)

    this_map = create_fnb_map(to_show)
    headers, deckgl = get_html(this_map)

    info = None
    footer = None
    coords = None
    if selected not in types and selected and selected != 'all':
        if to_show:
            coords = to_show[0].get('coordinates', [0,0])
            footer = to_show[0].get('details', {}).get('footer', [])
            rooms = to_show[0].get('details', {}).get('rooms', [])
            conditions = to_show[0].get('details', {}).get('conditions', {})
            activities = to_show[0].get('details', {}).get('activities', [])
            efe = to_show[0].get('name', '')

            if to_show[0].get('type') == 'Estadía':
                if rooms:
                    info = ['hostal', rooms]
                elif conditions:
                    info = ['discount', conditions]

            if to_show[0].get('type') == 'EFE':
                if efe:
                    info = ['efe', efe]
            
            if to_show[0].get('type') == 'Gastronomía':
                if conditions:
                    info = ['discount', conditions]

            if activities:
                info = ['fnb', activities]

    services = {t: [p['name'] for p in points if p['type'] == t] for t in types}  # noqa
    services = dict(reversed(services.items()))
    return render_template("fnb.html",
                           navbar_items=NAVBAR_ITEMS,
                           headers=headers,
                           map=deckgl,
                           services=services,
                           selected=selected,
                           info=info,
                           coords = coords,
                           footer=footer)


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
