import re
import pydeck as pdk
import pandas as pd
import statistics
from config import DECKGL_VERSION
from bs4 import BeautifulSoup


def get_middle_point(points):
    all_coords = [p["coordinates"] for p in points]
    all_lon = [x[0] for x in all_coords]
    all_lat = [x[1] for x in all_coords]
    return [statistics.mean(all_lon), statistics.mean(all_lat)]


def get_city_info(selected, points):
    if not selected:
        return None

    sel = selected.replace(' ', '').split('(')
    city_points = []
    for p in points:
        if p['city'] == sel[0] and p['country'] == sel[1].replace(')', ''):
            city_points.append(p)
            
    if not city_points:
        return None
        
    city_points.sort(key=lambda x: x.get('year', 2025), reverse=True)
    return city_points


def get_tabular_memt_data(points):
    grouped = {}
    for point in points:
        target_lng, target_lat = point['coordinates']
        year = point.get('year', 2025)
        for measure in point['measures']:
            source_lng, source_lat = measure['coordinates']
            transport_data = measure['data'][0]
            
            key = (point['city'], point['country'], point['destiny'], measure['place_name'], measure['route_name'])
            
            if key not in grouped:
                grouped[key] = {
                    'source_lng': source_lng,
                    'source_lat': source_lat,
                    'target_lng': target_lng,
                    'target_lat': target_lat,
                    'place_name': measure['place_name'],
                    'route_name': measure['route_name'],
                    'distance_km': measure['distance'],
                    'data_unit': point['data_unit'],
                    'country': point['country'],
                    'city': point['city'],
                    'destiny': point['destiny'],
                    'years_data': {}
                }
            
            grouped[key]['years_data'][year] = {
                'bike_time': transport_data.get('bike', "-"),
                'bus_time': transport_data.get('bus', "-"),
                'taxi_time': transport_data.get('taxi', "-"),
                'car_time': transport_data.get('car', "-"),
                'walk_time': transport_data.get('walk', "-"),
                'moto_time': transport_data.get('moto', "-"),
                'train_time': transport_data.get('train', "-"),
                'cicles_time': transport_data.get('cicles', "-"),
                'other_time': transport_data.get('other', "-"),
            }

    data = []
    for val in grouped.values():
        years = sorted(list(val['years_data'].keys()), reverse=True)
        route_id = str(val['route_name']).replace(' ', '_').replace('(', '').replace(')', '')
        
        tooltip_html = f"""
            <div id="tooltip" style="pointer-events: auto;">
                <b style='font-size: 16px; color: #222;'>
                    {val['route_name']} ({val['distance_km']} km)
                </b>
                <div style='margin-top: 4px; font-size: 14px;'>
                    <p style="margin-bottom: 5px;">Desde {val['place_name']} hasta {val['destiny']}</p>
                    <p style="margin-bottom: 5px;">(Tiempo medido en {val['data_unit']})</p>
        """
        
        if len(years) > 1:
            tooltip_html += "<div class='tooltip-tabs'>"
            for i, y in enumerate(years):
                checked = "checked" if i == 0 else ""
                tooltip_html += f"""
                    <input type="radio" name="tt_year_{route_id}" id="tt_tab_{y}_{route_id}" {checked} style="display: none;">
                    <label for="tt_tab_{y}_{route_id}" class="tt-tab-label">{y}</label>
                """
            tooltip_html += "<div class='tt-tab-contents'>"
            for i, y in enumerate(years):
                tdata = val['years_data'][y]
                tooltip_html += f"""
                    <div class="tt-tab-content tt-content-{y}">
                        <table class="travel-table" style="margin-top: 0;">
                            <thead><tr><th>Modo</th><th style="text-align: center;">Tiempo</th></tr></thead>
                            <tbody>
                                <tr><td>Bicicleta</td><td class="minutes" style="text-align: center;">{tdata['bike_time']}</td></tr>
                                <tr><td>Micro o bus</td><td class="minutes" style="text-align: center;">{tdata['bus_time']}</td></tr>
                                <tr><td>Automóvil</td><td class="minutes" style="text-align: center;">{tdata['car_time']}</td></tr>
                                <tr><td>Metro o tren</td><td class="minutes" style="text-align: center;">{tdata['train_time']}</td></tr>
                                <tr><td>Taxi o colectivo</td><td class="minutes" style="text-align: center;">{tdata['taxi_time']}</td></tr>
                                <tr><td>Motocicleta</td><td class="minutes" style="text-align: center;">{tdata['moto_time']}</td></tr>
                                <tr><td>Otros ciclos</td><td class="minutes" style="text-align: center;">{tdata['cicles_time']}</td></tr>
                            </tbody>
                        </table>
                    </div>
                """
            tooltip_html += "</div></div>"
            
            tooltip_html += """
                <style>
                    .tooltip-tabs { margin-top: 10px; }
                    .tt-tab-label { 
                        display: inline-block; padding: 4px 8px; cursor: pointer; 
                        background: #eee; border-radius: 4px 4px 0 0; margin-right: 2px;
                        color: #333; border: 1px solid #ccc; border-bottom: none;
                    }
                    input[type="radio"]:checked + .tt-tab-label { 
                        background: #fff; border-bottom: 2px solid #36a9e0; 
                        font-weight: bold; color: #36a9e0; 
                    }
                    .tt-tab-content { display: none; background: #fff; border-top: 1px solid #ccc; padding-top: 5px; }
                """
            for y in years:
                tooltip_html += f'input#tt_tab_{y}_{route_id}:checked ~ .tt-tab-contents .tt-content-{y} {{ display: block; }}'
            tooltip_html += "</style>"
            
        else:
            y = years[0]
            tdata = val['years_data'][y]
            tooltip_html += f"""
                    <table class="travel-table" style="margin-top: 10px;">
                        <thead><tr><th>Modo</th><th style="text-align: center;">Tiempo</th></tr></thead>
                        <tbody>
                            <tr><td>Bicicleta</td><td class="minutes" style="text-align: center;">{tdata['bike_time']}</td></tr>
                            <tr><td>Micro o bus</td><td class="minutes" style="text-align: center;">{tdata['bus_time']}</td></tr>
                            <tr><td>Automóvil</td><td class="minutes" style="text-align: center;">{tdata['car_time']}</td></tr>
                            <tr><td>Metro o tren</td><td class="minutes" style="text-align: center;">{tdata['train_time']}</td></tr>
                            <tr><td>Taxi o colectivo</td><td class="minutes" style="text-align: center;">{tdata['taxi_time']}</td></tr>
                            <tr><td>Motocicleta</td><td class="minutes" style="text-align: center;">{tdata['moto_time']}</td></tr>
                            <tr><td>Otros ciclos</td><td class="minutes" style="text-align: center;">{tdata['cicles_time']}</td></tr>
                        </tbody>
                    </table>
            """
            
        tooltip_html += "</div></div>"
        
        val['tooltip_html'] = tooltip_html
        data.append(val)
        
    return pd.DataFrame(data)


def get_fnb_data(points):
    return {
        'hostal': [p for p in points if p.get('type') == 'hostal']
    }

def create_map(points):
    middle = get_middle_point(points)
    layer = pdk.Layer(
        "IconLayer",
        data=points,
        get_icon="icon",
        get_size=4,
        size_scale=10,
        get_position="coordinates",
        pickable=True,
    )

    view_state = pdk.ViewState(
        longitude=middle[0],
        latitude=middle[1],
        zoom=13.5,
    )

    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style="light",
        height="500px",
        width="100%",
        tooltip={
            "html": """
                <div class="tooltip">
                    <b style='font-size: 16px; color: #222;'>{name}</b>
                    <div style='margin-top: 4px; font-size: 14px;'>
                        {description}
                    </div>
                </div>
            """,
            "style": {
                "backgroundColor": "transparent",
                "border": "none"
            }
        }
    )
    return r.to_html(as_string=True)


def create_memt_map(points, city=None):
    memt_data = get_tabular_memt_data(points)

    if city:
        sel = city.replace(' ', '').split('(')
        for p in points:
            if p['city'] == sel[0] and p['country'] == sel[1].replace(')', ''):
                middle = p['coordinates']
                if len(p['measures']) > 1:
                    middle = [middle[0] - 0.015, middle[1] + 0.015]
                break
        zoom_level = 13
    else:
        middle = get_middle_point(points)
        zoom_level = 3

    city_layer = pdk.Layer(
        "IconLayer",
        data=points,
        get_icon="icon",
        get_size=4,
        size_scale=10,
        get_position=["coordinates[1]", "coordinates[0]"],
        pickable=False,
    )

    travel_layer = pdk.Layer(
        "ArcLayer",
        data=memt_data,
        get_width=5,
        get_source_position=["source_lat", "source_lng"],
        get_target_position=["target_lat", "target_lng"],
        get_tilt=0,
        get_source_color=[54, 169, 224],
        get_target_color=[162, 190, 62],
        pickable=True,
        auto_highlight=True,
    )

    view_state = pdk.ViewState(
        longitude=middle[1],
        latitude=middle[0],
        zoom=zoom_level,
    )

    r = pdk.Deck(
        layers=[city_layer, travel_layer],
        initial_view_state=view_state,
        map_style="light",
        height="500px",
        width="100%",
        tooltip={
            "html": "{tooltip_html}",
            "style": {
                "text-align": "center",
                "backgroundColor": "rgb(255,255,255,0.95)",
                "padding": "10px",
                "borderRadius": "1.5rem",
                "boxShadow": "0 2px 10px rgba(0,0,0,0.2)",
                "pointerEvents": "auto"
            }
        }
    )
    return r.to_html(as_string=True)


def get_fnb_services_types(points):
    return list(set(p.get('type') for p in points if p.get('type')))


def get_service_info(selected, points):
    if not selected or selected == 'all':
        return points

    types = get_fnb_services_types(points)
    if selected in types:
        return [p for p in points if selected == p.get('type')]
    else:
        return [p for p in points if selected == p.get('name')]


def create_fnb_map(points):
    middle = [-33.0390271, -71.6292013] if len(get_fnb_services_types(points)) > 1 else get_middle_point(points)
    zoom_level = 15

    hostals_layer = pdk.Layer(
        "IconLayer",
        data=points,
        get_icon="icon",
        get_size=5,
        size_scale=10,
        get_position=["coordinates[1]", "coordinates[0]"],
        pickable=True,
    )

    view_state = pdk.ViewState(
        longitude=middle[1],
        latitude=middle[0],
        zoom=zoom_level,
    )

    r = pdk.Deck(
        layers=[hostals_layer], #, travel_layer],
        initial_view_state=view_state,
        map_style="light",
        height="500px",
        width="100%",
        tooltip={
            "html": """
                <div id="tooltip">
                    <div style='text-align: center'>
                        <h3 style="color: #222">{name}</h3>
                    </div>
                    <div style='margin-top: 4px; font-size: 14px; color: #222; margin-left: 25px'>
                        {description}
                    </div>
                </div>
            """,
            "style": {
                "width": "370px",
                "text-align": "left",
                "backgroundColor": "rgb(255,255,255,0.7)",
                "padding": "10px",
                "borderRadius": "1.5rem",
                "boxShadow": "0 2px 10px rgba(0,0,0,0.2)"
            }
        }
    )
    return r.to_html(as_string=True)


def change_gl_version(url: str):
    match = re.search(r'@~(\d+\.\d+\.\*)', url)
    if match:
        return url.replace(match.group(1), DECKGL_VERSION)
    else:
        return url


def get_html(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    scripts = list(soup.find_all('script'))
    links = list(soup.find_all('link'))
    html = links + scripts[:2]
    headers = [change_gl_version(str(h)) for h in html]
    gl_script = scripts[-1].string
    deckgl = f'\n<div id="deck-container"></div>\n<script>{gl_script}</script>'  # noqa
    return '\n'.join(headers), deckgl
