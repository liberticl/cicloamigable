PROD = False
DECKGL_VERSION = '8.9.*'

NAVBAR_ITEMS = [
    {"name": "Inicio", "url": "/"},
    # {"name": "Licitaciones", "url": "/licitaciones"},
    # {"name": "Presentación", "url": "/presentacion"},
    {"name": "Proyecto", "url": "/proyecto"},
    {"name": "Mapa", "url": "/mapa"},
    {"name": "MEMT", "url": "/memt"},
    {"name": "FNB", "url": "/fnb"},
    # {"name": "Actividades", "url": "/actividades"},
]


FNB = [
    {
        "type": "hostal",
        "name": "Casa Volante Hostal",
        "logo": "<BASE_URL>/fnb/casa_volante_hostal.png",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.041034, -71.6281573],
        "description": "<ul><li>Ubicado en Fischer 27, Cerro Alegre, Valparaíso.</li><li>Capacidad para 96 personas.</li><li>A 350 metros de la Plaza Sotomayor.</li></ul>",
        "details": {
            "distance": "350 metros",
            "footer": "Avisar participación en el Foro Nacional de la Bicicleta al reservar",
            "rooms": [
                {
                    "name": "Privada 6/8 personas (Literas, Baño Compartido)",
                    "detail": "Por persona",
                    "price": 14000
                },
                {
                    "name": "Doble Económica (Litera, Baño Compartido)",
                    "detail": "Por persona",
                    "price": 17000
                },
                {
                    "name": "Doble Estándar (Matrimonial/2 Camas, TV, Baño Compartido)",
                    "detail": "Por persona",
                    "price": 20000
                },
                {
                    "name": "Triple Económica (Litera Especial, Baño Compartido)",
                    "detail": "Por persona",
                    "price": 16000
                },
                {
                    "name": "Triple Estándar (Matrimonial + Litera, TV, Baño Compartido)",
                    "detail": "Por persona",
                    "price": 18500
                },
                {
                    "name": "Cuádruple Estándar (Matrimonial + Litera, Baño Compartido)",
                    "detail": "Por persona",
                    "price": 17000
                },
                {
                    "name": "Cama en Compartido 6/8 (Literas, Baño Compartido)",
                    "detail": "Por persona",
                    "price": 14000
                },
                {
                    "name": "Desayuno Buffet Diario",
                    "detail": "Por persona",
                    "price": 6000
                }
            ]
        }
    }
]

VLPO_CICLOAMIGABLE = [
        {
            "name": "Plaza Bismarck",
            "description": "Estacionamientos instalados en plazas para dejar la bicicleta cuando te encuentres cerca. Son de tipo U invertida con capacidad para un máximo de 10 bicicletas.",  # noqa
            "coordinates": [-71.6309695, -33.0477747],
            "icon": {
                "url": "<BASE_URL>/estacionamiento.png",
                "width": 242,
                "height": 242,
                "anchorY": 242,
            }
        },
        {
            "name": "Plaza de Los Poetas",
            "description": "Estacionamientos instalados en plazas para dejar la bicicleta cuando te encuentres cerca. Son de tipo U invertida con capacidad para un máximo de 10 bicicletas.",  # noqa
            "coordinates": [-71.6216531, -33.0529473],
            "icon": {
                "url": "<BASE_URL>/estacionamiento.png",
                "width": 242,
                "height": 242,
                "anchorY": 242
            }
        },
        {
            "name": "Plaza Victoria",
            "description": "Estacionamientos instalados en plazas para dejar la bicicleta cuando te encuentres cerca. Son de tipo U invertida con capacidad para un máximo de 10 bicicletas.",  # noqa
            "coordinates": [-71.6201343, -33.0462627],
            "icon": {
                "url": "<BASE_URL>/estacionamiento.png",
                "width": 242,
                "height": 242,
                "anchorY": 242
            }
        },
        {
            "name": "Caleta Portales",
            "description": "Estacionamientos instalados en plazas para dejar la bicicleta cuando te encuentres cerca. Son de tipo U invertida con capacidad para un máximo de 10 bicicletas.",  # noqa
            "coordinates": [-71.5912128, -33.0327061],
            "icon": {
                "url": "<BASE_URL>/estacionamiento.png",
                "width": 242,
                "height": 242,
                "anchorY": 242
            }
        },
        {
            "name": "Ciclocalle",
            "description": "Señalética que indica calle compartida entre vehículos motorizados y ciclos. Por regulación, sólo puede utilizarse en zonas 30 y se encuentra acompañada de una demarcación de doble chevron.",  # noqa
            "coordinates": [-71.633855, -33.046935],
            "icon": {
                "url": "<BASE_URL>/ciclocalle.png",
                "width": 242,
                "height": 242,
                "anchorY": 242
            }
        },
        {
            "name": "Ciclocalle",
            "description": "Señalética que indica calle compartida entre vehículos motorizados y ciclos. Por regulación, sólo puede utilizarse en zonas 30 y se encuentra acompañada de una demarcación de doble chevron.",  # noqa
            "coordinates": [-71.634301, -33.042629],
            "icon": {
                "url": "<BASE_URL>/ciclocalle.png",
                "width": 242,
                "height": 242,
                "anchorY": 242
            }
        },
        {
            "name": "Ciclocalle",
            "description": "Señalética que indica calle compartida entre vehículos motorizados y ciclos. Por regulación, sólo puede utilizarse en zonas 30 y se encuentra acompañada de una demarcación de doble chevron.",  # noqa
            "coordinates": [-71.638566, -33.040495],
            "icon": {
                "url": "<BASE_URL>/ciclocalle.png",
                "width": 242,
                "height": 242,
                "anchorY": 242
            }
        },
        {
            "name": "Ciclocalle",
            "description": "Señalética que indica calle compartida entre vehículos motorizados y ciclos. Por regulación, sólo puede utilizarse en zonas 30 y se encuentra acompañada de una demarcación de doble chevron.",  # noqa
            "coordinates": [-71.634407, -33.031686],
            "icon": {
                "url": "<BASE_URL>/ciclocalle.png",
                "width": 242,
                "height": 242,
                "anchorY": 242
            }
        },
        {
            "name": "Ciclocalle",
            "description": "Señalética que indica calle compartida entre vehículos motorizados y ciclos. Por regulación, sólo puede utilizarse en zonas 30 y se encuentra acompañada de una demarcación de doble chevron.",  # noqa
            "coordinates": [-71.633268, -33.028571],
            "icon": {
                "url": "<BASE_URL>/ciclocalle.png",
                "width": 242,
                "height": 242,
                "anchorY": 242
            }
        },
        {
            "name": "Ciclocalle",
            "description": "Señalética que indica calle compartida entre vehículos motorizados y ciclos. Por regulación, sólo puede utilizarse en zonas 30 y se encuentra acompañada de una demarcación de doble chevron.",  # noqa
            "coordinates": [-71.62225, -33.05473],
            "icon": {
                "url": "<BASE_URL>/ciclocalle.png",
                "width": 242,
                "height": 242,
                "anchorY": 242
            }
        },
        {
            "name": "Zona compartida peatones y ciclos",
            "description": "Señalética que indica que la vereda se comparte entre peatones y usuarios de ciclos. Fue considerada en este proyecto debido al uso multiprósito que tiene Errázuriz por el ancho del paseo peatonal.",  # noqa
            "coordinates": [-71.620832, -33.04308],
            "icon": {
                "url": "<BASE_URL>/peatones-ciclos.png",
                "width": 242,
                "height": 242,
                "anchorY": 242
            }
        },
        {
            "name": "Zona compartida peatones y ciclos",
            "description": "Señalética que indica que la vereda se comparte entre peatones y usuarios de ciclos. Fue considerada en este proyecto debido al uso multiprósito que tiene Errázuriz por el ancho del paseo peatonal.",  # noqa
            "coordinates": [-71.606211, -33.043238],
            "icon": {
                "url": "<BASE_URL>/peatones-ciclos.png",
                "width": 242,
                "height": 242,
                "anchorY": 242
            }
        },
        {
            "name": "Zona compartida peatones y ciclos",
            "description": "Señalética que indica que la vereda se comparte entre peatones y usuarios de ciclos. Fue considerada en este proyecto debido al uso multiprósito que tiene Errázuriz por el ancho del paseo peatonal.",  # noqa
            "coordinates": [-71.6082922, -33.0439705],
            "icon": {
                "url": "<BASE_URL>/peatones-ciclos.png",
                "width": 242,
                "height": 242,
                "anchorY": 242
            }
        }
    ]


MEMT = [
    {
        "country": "Chile",
        "city": "Antofagasta",
        "destiny": "Parque Brasil",
        "coordinates": [-23.654052, -70.401176],
        "data_unit": "minutos",
        "distance_unit": "kilómetros",
        "icon": {
            "url": "<BASE_URL>/memt/logo.png",
            "width": 250,
            "height": 250,
            "anchorY": 250
        },
        "measures": [
            {
                "coordinates": [-23.623107, -70.384487],
                "place_name": "Plaza Lautaro",
                "route_name": "Sector Norte",
                "distance": 4.5,
                "data": [
                    {
                        "bike": 10,
                        "bus": 20,
                        "car": 35
                    }
                ]
            },
            {
                "coordinates": [-23.693076, -70.409985],
                "place_name": "Plaza Coviefi",
                "route_name": "Sector Sur",
                "distance": 4.8,
                "data": [
                    {
                        "bike": 15,
                        "bus": 18,
                        "car": 29
                    }
                ]
            }
        ]
    },
    {
        "country": "Chile",
        "city": "Concepción",
        "destiny": "Plaza Independencia",
        "coordinates": [-36.827098, -73.050154],
        "data_unit": "minutos",
        "distance_unit": "kilómetros",
        "icon": {
            "url": "<BASE_URL>/memt/logo.png",
            "width": 250,
            "height": 250,
            "anchorY": 250
        },
        "measures": [
            {
                "coordinates": [-36.820138, -73.014921],
                "place_name": "Frontis UBB",
                "route_name": "Concepción",
                "distance": 5,
                "data": [
                    {
                        "bike": 13,
                        "bus": 30,
                        "car": 34,
                    }
                ]
            },
            {
                "coordinates": [-36.926334, -73.024522],
                "place_name": "Plaza Ursulinas",
                "route_name": "Chiguayante",
                "distance": 12,
                "data": [
                    {
                        "bike": 39.5,
                        "bus": 37,
                        "car": 36,
                        "train": 50
                    }
                ]
            },
            {
                "coordinates": [-36.846252, -73.130743],
                "place_name": "Estación Alborada",
                "route_name": "San Pedro de la Paz",
                "distance": 10,
                "data": [
                    {
                        "car": 46,
                        "train": 33
                    }
                ]
            }
        ]
    },
    {
        "country": "Chile",
        "city": "Talca",
        "destiny": "Hospital Regional de Talca",
        "coordinates": [-35.427558, -71.646429],
        "data_unit": "minutos",
        "distance_unit": "kilómetros",
        "icon": {
            "url": "<BASE_URL>/memt/logo.png",
            "width": 250,
            "height": 250,
            "anchorY": 250
        },
        "measures": [
            {
                "coordinates": [-35.442731, -71.629050],
                "place_name": "8 Sur con 32 Oriente",
                "route_name": "Sector Oriente Talca",
                "distance": 2.8,
                "data": [
                    {
                        "bike": 8,
                        "bus": 25,
                        "taxi": 20,
                        "car": 24
                    }
                ]
            },
            {
                "coordinates": [-35.459411, -71.664591],
                "place_name": "Sector Sur Maule Norte",
                "route_name": "9 Oriente con 29 Sur",
                "distance": 4.4,
                "data": [
                    {
                        "bike": 10,
                        "bus": 36,
                        "car": 26
                    }
                ]
            }
        ]
    },
    {
        "country": "Chile",
        "city": "Curicó",
        "destiny": "Plaza de Armas",
        "coordinates": [-34.985682, -71.230498],
        "data_unit": "minutos",
        "distance_unit": "kilómetros",
        "icon": {
            "url": "<BASE_URL>/memt/logo.png",
            "width": 250,
            "height": 250,
            "anchorY": 250
        },
        "measures": [
            {
                "coordinates": [-34.961628, -71.204214],
                "place_name": "Avenida Amsterdam con París",
                "route_name": "Ruta Única",
                "distance": 5.5,
                "data": [
                    {
                        "bike": 17,
                        "moto": 26,
                        "taxi": 31,
                        "car": 28
                    }
                ]
            }
        ]
    },
    {
        "country": "Chile",
        "city": "Molina",
        "destiny": "Villa María Auxiliadora",
        "coordinates": [-35.106129, -71.276390],
        "data_unit": "minutos",
        "distance_unit": "kilómetros",
        "icon": {
            "url": "<BASE_URL>/memt/logo.png",
            "width": 250,
            "height": 250,
            "anchorY": 250
        },
        "measures": [
            {
                "coordinates": [-35.103925, -71.302827],
                "place_name": "Terminal Aquelarre",
                "route_name": "Ruta Única",
                "distance": 3,
                "data": [
                    {
                        "bike": 11,
                        "moto": 11,
                        "bus": 19,
                        "car": 13,
                        "walk": 46
                    }
                ]
            }
        ]
    },
    {
        "country": "Ecuador",
        "city": "Guayaquil",
        "destiny": "Plaza Pentagonal",
        "coordinates": [-2.1686767, -79.9168653,],
        "data_unit": "minutos",
        "distance_unit": "kilómetros",
        "icon": {
            "url": "<BASE_URL>/memt/logo.png",
            "width": 250,
            "height": 250,
            "anchorY": 250
        },
        "measures": [
            {
                "coordinates": [-2.1860065, -79.8959017],
                "place_name": "Calles Quisquís y Tungurahua",
                "route_name": "Desde Quisquís y Tungurahua",
                "distance": 3,
                "data": [
                    {
                        "bike": 12,
                        "car": 11,
                        "moto": 10,
                        "bus": 14
                    }
                ]
            },
            {
                "coordinates": [-2.194815, -79.881133],
                "place_name": "Plaza de la Administración",
                "route_name": "Plaza de la Administración",
                "distance": 5.7,
                "data": [
                    {
                        "bike": "19 - 25",
                        "car": 41,
                        "cicles": 26,
                        "bus": 40
                    }
                ]
            }
        ]
    }
]


NOT_USED_HTML = """
    <tr>
        <td>A pie</td>
        <td class="minutes"
            style="text-align: center;"
            >{walk_time}</td>
    </tr>
    <tr>
        <td>Ciclos (patines, cicles)</td>
        <td class="minutes"
            style="text-align: center;"
            >{cicles_time}</td>
    </tr>
    <tr>
        <td>Otros</td>
        <td class="minutes"
            style="text-align: center;"
            >{other_time}</td>
    </tr>
"""


def get_points(points: list, base_url: str):
    points_with_url = []
    for p in points:
        p['icon']['url'] = p['icon']['url'].replace('<BASE_URL>', f"{base_url}/icons")
        if 'logo' in p.keys():
            p['logo'] = p['logo'].replace('<BASE_URL>', f"{base_url}/logos")
        points_with_url.append(p)
    return points_with_url
