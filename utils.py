import re
import pydeck as pdk
import pandas as pd
import statistics
from config import DECKGL_VERSION
from bs4 import BeautifulSoup
import requests
import json


def get_middle_point(points):
    all_coords = [p["coordinates"] for p in points]
    all_lon = [x[0] for x in all_coords]
    all_lat = [x[1] for x in all_coords]
    return [statistics.mean(all_lon), statistics.mean(all_lat)]


def get_city_info(selected, points):
    if not selected:
        return None

    sel = selected.replace(' ', '').split('(')
    for p in points:
        if p['city'] == sel[0] and p['country'] == sel[1].replace(')', ''):
            return p
    return None


def get_tabular_memt_data(points):
    data = []
    for point in points:
        target_lng, target_lat = point['coordinates']
        for measure in point['measures']:
            source_lng, source_lat = measure['coordinates']
            # Accedemos al primer elemento de 'data'
            transport_data = measure['data'][0]

            data.append({
                # Coordenadas de origen (source)
                'source_lng': source_lng,
                'source_lat': source_lat,
                # Coordenadas de destino (target)
                'target_lng': target_lng,
                'target_lat': target_lat,
                # Metadatos adicionales
                'place_name': measure['place_name'],
                'route_name': measure['route_name'],
                'distance_km': measure['distance'],
                'data_unit': point['data_unit'],
                # Tiempos de transporte
                'bike_time': transport_data.get('bike', '-'),
                'bus_time': transport_data.get('bus', '-'),
                'taxi_time': transport_data.get('taxi', '-'),
                'car_time': transport_data.get('car', '-'),
                'walk_time': transport_data.get('walk', '-'),
                'moto_time': transport_data.get('moto', '-'),
                'train_time': transport_data.get('train', '-'),
                'cicles_time': transport_data.get('cicles', '-'),
                'other_time': transport_data.get('other', '-'),
                # Datos globales del punto
                'country': point['country'],
                'city': point['city'],
                'destiny': point['destiny']
            })
    return pd.DataFrame(data)


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
            "html": """
                <div id="tooltip">
                    <b style='font-size: 16px; color: #222;'>
                        {route_name} ({distance_km} km)
                    </b>
                    <div style='margin-top: 4px; font-size: 14px;'>
                        <p>Desde {place_name} hasta {destiny}</p>
                        <p>(Tiempo medido en {data_unit})</p>
                        <table class="travel-table">
                            <thead>
                                <tr>
                                    <th>Modo</th>
                                    <th style="text-align: center;">Tiempo</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Bicicleta</td>
                                    <td class="minutes"
                                        style="text-align: center;"
                                        >{bike_time}</td>
                                </tr>
                                <tr>
                                    <td>Micro o bus</td>
                                    <td class="minutes"
                                        style="text-align: center;"
                                        >{bus_time}</td>
                                </tr>
                                <tr>
                                    <td>Automóvil</td>
                                    <td class="minutes"
                                        style="text-align: center;"
                                        >{car_time}</td>
                                </tr>
                                <tr>
                                    <td>Taxi o colectivo</td>
                                    <td class="minutes"
                                        style="text-align: center;"
                                        >{taxi_time}</td>
                                </tr>
                                <tr>
                                    <td>Motocicleta</td>
                                    <td class="minutes"
                                        style="text-align: center;"
                                        >{moto_time}</td>
                                </tr>
                                <tr>
                                    <td>Metro o tren</td>
                                    <td class="minutes"
                                        style="text-align: center;"
                                        >{train_time}</td>
                                </tr>
                                <tr>
                                    <td>Otros ciclos</td>
                                    <td class="minutes"
                                        style="text-align: center;"
                                        >{cicles_time}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            """,
            "style": {
                "text-align": "center",
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


# Source: https://desarrolladores.mercadopublico.cl/
API_TICKET = ''
BASE_URL_LICITACIONES = 'https://api.mercadopublico.cl/servicios/v1/publico/licitaciones.json'


def get_tenders(keywords, **kwargs):
    """
    Consulta licitaciones en Mercado Público.

    Args:
        keywords (list): Lista de palabras clave a buscar.
        day (str, optional): Fecha asociada al estado de las licitaciones a buscar.
        status (str, optional): Estado de las licitaciones a buscar.
        region (str, optional): Código de la región para filtrar.
        comuna (str, optional): Código de la comuna para filtrar.

    Returns:
        list: Lista de licitaciones encontradas o None si hay error.
    """
    if not API_TICKET or API_TICKET == "TU_TICKET_DE_ACCESO":
        return None

    query_params = {
        'ticket': API_TICKET,
        # 'fecha': datetime.now().strftime('%d%m%Y'),
        # 'estado': 'activas' # u otro estado que te interese
    }

    if kwargs:
        for key, value in kwargs.items():
            if key in ['fecha', 'estado', 'codigoRegion', 'codigoComuna']:
                query_params.update({key: value})

    try:
        response = requests.get(BASE_URL_LICITACIONES, params=query_params, timeout=10)
        print(response.request.path_url)
        response.raise_for_status()  # Lanza una excepción para errores HTTP (4xx o 5xx)
        data = response.json()

        founded = []
        for lic in data.get('Listado', []):
            name = lic.get('Nombre', '').lower()
            description = lic.get('Descripcion', '').lower()

            flag = False
            for kw in keywords:
                if kw.lower() in name or kw.lower() in description:
                    flag = True
                    break
            
            if flag:
                founded.append({
                    'CodigoExterno': lic.get('CodigoExterno'),
                    'Nombre': lic.get('Nombre'),
                    'FechaCierre': lic.get('FechaCierre'),
                    'Comprador': lic.get('Comprador', {}).get('NombreOrganismo'),
                })
        return founded


    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud HTTP: {e}")
        if response is not None:
            print(f"Respuesta del servidor: {response.text}")
        return None
    except json.JSONDecodeError:
        print("Error al decodificar la respuesta JSON.")
        print(f"Respuesta del servidor: {response.text}")
        return None

# --- Ejemplo de uso ---
if __name__ == "__main__":
        palabras_interes = ["ciclov", "bicicleta", "bici", "plaza" "cicloamigable"]
        print("\n--- Buscando en todo Chile ---")
        licitaciones = get_tenders(palabras_interes, **{'estado': 'cerrada'})
        if licitaciones:
            print(f"Se encontraron {len(licitaciones)} licitaciones:")
            for lic in licitaciones:
                print(f"  ID: {lic['CodigoExterno']}, Nombre: {lic['Nombre']}, Cierre: {lic['FechaCierre']}, Comprador: {lic['Comprador']}")
        else:
            print("No se encontraron licitaciones con esos criterios.")
