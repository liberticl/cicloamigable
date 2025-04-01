BASE_URL = "http://localhost:5000"  # Cambia según tu entorno


NAVBAR_ITEMS = [
    {"name": "Inicio", "url": "/"},
    # {"name": "Licitaciones", "url": "/licitaciones"},
    # {"name": "Presentación", "url": "/presentacion"},
    {"name": "Proyecto", "url": "/proyecto"},
    {"name": "Mapa", "url": "/mapa"},
    # {"name": "Actividades", "url": "/actividades"},
]


POINTS = [
    {
        "name": "Plaza Bismarck",
        "description": "Estacionamientos instalados en plazas para dejar la bicicleta cuando te encuentres cerca. Son de tipo U invertida con capacidad para un máximo de 10 bicicletas.",  # noqa
        "coordinates": [-71.6309695, -33.0477747],
        "icon": {
            "url": f"{BASE_URL}/static/img/icons/estacionamiento.png",
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
            "url": f"{BASE_URL}/static/img/icons/estacionamiento.png",
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
            "url": f"{BASE_URL}/static/img/icons/estacionamiento.png",
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
            "url": f"{BASE_URL}/static/img/icons/estacionamiento.png",
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
            "url": f"{BASE_URL}/static/img/icons/ciclocalle.png",
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
            "url": f"{BASE_URL}/static/img/icons/ciclocalle.png",
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
            "url": f"{BASE_URL}/static/img/icons/ciclocalle.png",
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
            "url": f"{BASE_URL}/static/img/icons/ciclocalle.png",
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
            "url": f"{BASE_URL}/static/img/icons/ciclocalle.png",
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
            "url": f"{BASE_URL}/static/img/icons/ciclocalle.png",
            "width": 242,
            "height": 242,
            "anchorY": 242
        }
    },
    {
        "name": "Zona compartida peatones y ciclos",
        "description": "Señalética que indica que la vereda se comparte entre peatones y usuarios de ciclos. Fue considerada en este proyecto debido al uso multiprósito que tiene Errázuriz por el ancho del paseo peatonal.", # noqa
        "coordinates": [-71.620832, -33.04308],
        "icon": {
            "url": f"{BASE_URL}/static/img/icons/peatones-ciclos.png",
            "width": 242,
            "height": 242,
            "anchorY": 242
        }
    },
    {
        "name": "Zona compartida peatones y ciclos",
        "description": "Señalética que indica que la vereda se comparte entre peatones y usuarios de ciclos. Fue considerada en este proyecto debido al uso multiprósito que tiene Errázuriz por el ancho del paseo peatonal.", # noqa
        "coordinates": [-71.606211, -33.043238],
        "icon": {
            "url": f"{BASE_URL}/static/img/icons/peatones-ciclos.png",
            "width": 242,
            "height": 242,
            "anchorY": 242
        }
    },
    {
        "name": "Zona compartida peatones y ciclos",
        "description": "Señalética que indica que la vereda se comparte entre peatones y usuarios de ciclos. Fue considerada en este proyecto debido al uso multiprósito que tiene Errázuriz por el ancho del paseo peatonal.", # noqa
        "coordinates": [-71.6082922, -33.0439705],
        "icon": {
            "url": f"{BASE_URL}/static/img/icons/peatones-ciclos.png",
            "width": 242,
            "height": 242,
            "anchorY": 242
        }
    }
]
