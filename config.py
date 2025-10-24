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

FNB_TYPES = ['Estadía', 'FNB', 'Gastronomía', 'EFE']
FNB = [
    {
        "type": "Estadía",
        "name": "Casa Volante Hostal",
        "logo": "<BASE_URL>/fnb/casa_volante_hostal.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.041034, -71.6281573],
        "description": "<ul><li>Ubicado en Fischer 27, Cerro Alegre, Valparaíso.</li><li>Capacidad para 96 personas.</li><li>A 350 metros de la Plaza Sotomayor.</li></ul>",
        "details": {
            "footer": [
                "Todos los precios son por persona.",
                "Avisar participación en el Foro Nacional de la Bicicleta al reservar."
            ],
            "rooms": [
                {
                    "name": "Privada 6/8 personas (Literas, baño compartido)",
                    "price": 14000
                },
                {
                    "name": "Doble Económica (Litera, baño compartido)",
                    "price": 17000
                },
                {
                    "name": "Doble Estándar (Matrimonial/2 camas, TV, baño compartido)",
                    "price": 20000
                },
                {
                    "name": "Triple Económica (Litera especial, baño compartido)",
                    "price": 16000
                },
                {
                    "name": "Triple Estándar (Matrimonial + litera, TV, baño compartido)",
                    "price": 18500
                },
                {
                    "name": "Cuádruple Estándar (Matrimonial + litera, baño compartido)",
                    "price": 17000
                },
                {
                    "name": "Compartida 6/8 (Literas, baño compartido)",
                    "price": 14000
                },
                {
                    "name": "Desayuno Buffet Diario",
                    "price": 6000
                }
            ]
        }
    },
    {
        "type": "FNB",
        "name": "Mercado Puerto",
        "logo": "<BASE_URL>/fnb/mercado_puerto.png",
        "logo_style": "width: 80px;",
        "icon": {
            "url": "<BASE_URL>/fnb/fnb.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.035846, -71.630126],
        "description": "<b>Actividades en este espacio</b>:<br><ul><li>Inauguración del FNB 2025.</li><li>Fiesta de Halloween.</li><li>Asamblea Nacional Ciclista.</li></ul>",
        "details": {
            "footer": [
                "Los horarios de los eventos pueden cambiar.",
                "Verificar <a href='https://fnb.cl' target='_blank'>programa</a>."
            ],
            "activities": [
                {
                    "name": "Inauguración del Foro Nacional",
                    "day": "Jueves 30 de octubre",
                    "time": "18:00 horas"
                },
                {
                    "name": "Fiesta de Halloween",
                    "day": "Viernes 31 de octubre",
                    "time": "21:30 horas"
                },
                {
                    "name": "Asamblea Nacional Ciclista",
                    "day": "Domingo 02 de noviembre",
                    "time": "10:00 horas"
                }
            ]
        }
    },
    {
        "type": "FNB",
        "name": "Plaza Sotomayor",
        "logo": "<BASE_URL>/fnb/mercado_puerto.png",
        "logo_style": "width: 80px;",
        "icon": {
            "url": "<BASE_URL>/fnb/fnb.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.0390271, -71.6292013],
        "description": "<b>Actividades en este espacio</b>:<br><ul><li>Panel Avenida España.</li><li>Panel Cicloturismo.</li><li>Exposiciones.</li></li><li>Cicletada de Halloween.</li></li><li>Cicletada Intermodal.</li></li><li>Emprendimientos.</li></ul>",
        "details": {
            "footer": [
                "Los horarios de los eventos pueden cambiar.",
                "Verificar <a href='https://fnb.cl/programa/' target='_blank'>programa</a>."
            ],
            "activities": [
                {
                    "name": "Panel Avenida España",
                    "day": "Viernes 31 de octubre",
                    "time": "09:30 horas"
                },
                {
                    "name": "Cicletada de Halloween",
                    "day": "Viernes 31 de octubre",
                    "time": "19:30 horas"
                },
                {
                    "name": "Panel Cicloturismo",
                    "day": "Sábado 01 de noviembre",
                    "time": "09:30 horas"
                },
                {
                    "name": "Cicletada Intermodal",
                    "day": "Sábado 01 de noviembre",
                    "time": "18:30 horas"
                },
                {
                    "name": "Exposiciones",
                    "day": "Ambos días",
                    "time": "14:30 horas"
                },
                {
                    "name": "Emprendimientos",
                    "day": "Ambos días",
                    "time": "10:00 horas"
                }
            ]
        }
    },
    {
        "type": "EFE",
        "name": "Puerto",
        "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
        "logo": "<BASE_URL>/fnb/efe.svg",
        "logo_style": "width: 150px;",
        "details": {
            "name": "Puerto"
        },
        "coordinates": [
            -33.038889,
            -71.626389
        ],
        "icon": {
            "url": "<BASE_URL>/fnb/efe.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        }
    },
    # {
    #     "type": "EFE",
    #     "name": "Bellavista",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "Bellavista"
    #     },
    #     "coordinates": [
    #         -33.043056,
    #         -71.620833
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    # {
    #     "type": "EFE",
    #     "name": "Francia",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "Francia"
    #     },
    #     "coordinates": [
    #         -33.043889,
    #         -71.612778
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    # {
    #     "type": "EFE",
    #     "name": "Barón",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "Barón"
    #     },
    #     "coordinates": [
    #         -33.042222,
    #         -71.605556
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    # {
    #     "type": "EFE",
    #     "name": "Portales",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "Portales"
    #     },
    #     "coordinates": [
    #         -33.032778,
    #         -71.591667
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    # {
    #     "type": "EFE",
    #     "name": "Recreo",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "Recreo"
    #     },
    #     "coordinates": [
    #         -33.027222,
    #         -71.575833
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    # {
    #     "type": "EFE",
    #     "name": "Miramar",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "Miramar"
    #     },
    #     "coordinates": [
    #         -33.025,
    #         -71.561667
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    # {
    #     "type": "EFE",
    #     "name": "Viña del Mar",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "Viña del Mar"
    #     },
    #     "coordinates": [
    #         -33.026389,
    #         -71.552222
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    # {
    #     "type": "EFE",
    #     "name": "Hospital",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "Hospital"
    #     },
    #     "coordinates": [
    #         -33.028889,
    #         -71.541667
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    # {
    #     "type": "EFE",
    #     "name": "Chorrillos",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "Chorrillos"
    #     },
    #     "coordinates": [
    #         -33.033333,
    #         -71.532778
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    # {
    #     "type": "EFE",
    #     "name": "El Salto",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "El Salto"
    #     },
    #     "coordinates": [
    #         -33.041111,
    #         -71.521389
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    # {
    #     "type": "EFE",
    #     "name": "Quilpué",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "Quilpué"
    #     },
    #     "coordinates": [
    #         -33.045278,
    #         -71.445
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    # {
    #     "type": "EFE",
    #     "name": "El Sol",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "El Sol"
    #     },
    #     "coordinates": [
    #         -33.039722,
    #         -71.428611
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    # {
    #     "type": "EFE",
    #     "name": "El Belloto",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "El Belloto"
    #     },
    #     "coordinates": [
    #         -33.046389,
    #         -71.407222
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    {
        "type": "EFE",
        "name": "Las Américas",
        "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
        "logo": "<BASE_URL>/fnb/efe.svg",
        "logo_style": "width: 150px;",
        "details": {
            "name": "Las Américas"
        },
        "coordinates": [
            -33.043889,
            -71.395
        ],
        "icon": {
            "url": "<BASE_URL>/fnb/efe.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        }
    },
    # {
    #     "type": "EFE",
    #     "name": "La Concepción",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "La Concepción"
    #     },
    #     "coordinates": [
    #         -33.041667,
    #         -71.382222
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    # {
    #     "type": "EFE",
    #     "name": "Villa Alemana",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "Villa Alemana"
    #     },
    #     "coordinates": [
    #         -33.0425,
    #         -71.373611
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    # {
    #     "type": "EFE",
    #     "name": "Sargento Aldea",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "Sargento Aldea"
    #     },
    #     "coordinates": [
    #         -33.041944,
    #         -71.366111
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    {
        "type": "EFE",
        "name": "Peñablanca",
        "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
        "logo": "<BASE_URL>/fnb/efe.svg",
        "logo_style": "width: 150px;",
        "details": {
            "name": "Peñablanca"
        },
        "coordinates": [
            -33.040278,
            -71.352778
        ],
        "icon": {
            "url": "<BASE_URL>/fnb/efe.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        }
    },
    # {
    #     "type": "EFE",
    #     "name": "Limache",
    #     "description": "<b>Información general</b>:<br><ul><li>Podrás subir la bicicleta durante el foro.</li><li>Se puede pagar con tarjeta de débito.</li><li>Servicio nocturno de buses cada una hora.</li></ul>",
    #     "logo": "<BASE_URL>/fnb/efe.svg",
    #     "logo_style": "width: 150px;",
    #     "details": {
    #         "name": "Limache"
    #     },
    #     "coordinates": [
    #         -32.984444,
    #         -71.2775
    #     ],
    #     "icon": {
    #         "url": "<BASE_URL>/fnb/efe.png",
    #         "width": 350,
    #         "height": 350,
    #         "anchorY": 350
    #     }
    # },
    {
        "type": "Estadía",
        "name": "Augusta Apart Hotel",
        "logo": "<BASE_URL>/fnb/hostal.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.043839, -71.629293],
        "description": "<ul><li>Ubicado en San Enrique 577, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "San Enrique 577",
                "phone_1": "+56322525175",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.augustavalparaiso.com",
                "instagram": "augustavalparaiso"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "AYCA La Flora Hotel Boutique",
        "logo": "<BASE_URL>/fnb/ayca_la_flora.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.041935, -71.625451],
        "description": "<ul><li>Ubicado en Subida Concepción 35, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Subida Concepción 35",
                "phone_1": "+56322212775",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.laflora-valpo.com",
                "instagram": "aykalaflora.valparaiso"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "CasaBlu",
        "logo": "<BASE_URL>/fnb/casa_blu.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.042778, -71.630198],
        "description": "<ul><li>Ubicado en San Enrique 387, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "San Enrique 387",
                "phone_1": "+56229441402",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.casablu.cl",
                "instagram": "casablu.hotel"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Casa Galos Hotel & Lofts",
        "logo": "<BASE_URL>/fnb/casa_galos.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.043875, -71.630115],
        "description": "<ul><li>Ubicado en Templeman 893, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Templeman 893",
                "phone_1": "+56322112633",
                "phone_2": "+56962705458",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.casagalos.cl",
                "instagram": "casagalos"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Casa Puente Hotel Boutique",
        "logo": "<BASE_URL>/fnb/casa_puente.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.042776, -71.631146],
        "description": "<ul><li>Ubicado en San Agustín 552, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "San Agustín 552",
                "phone_1": "+56995386025",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.casapuente.cl",
                "instagram": "casapuente_artwinehotel"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Casa Vander Valparaiso, Cerro Alegre Hotel Boutique",
        "logo": "<BASE_URL>/fnb/casa_wander.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.043810, -71.626872],
        "description": "<ul><li>Ubicado en P.º Dimalow 135, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "P.º Dimalow 135",
                "phone_1": "+56323327662",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.casawander.cl",
                "instagram": "casawanderhotelboutique"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Fauna Hotel & Restaurante",
        "logo": "<BASE_URL>/fnb/hotel_fauna.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.043774, -71.626955],
        "description": "<ul><li>Ubicado en P.º Dimalow 166, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "P.º Dimalow 166",
                "phone_1": "+56323370719",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.faunahotel.cl",
                "instagram": "faunahotel"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Hotel Boutique Acontraluz",
        "logo": "<BASE_URL>/fnb/hotel_acontraluz.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.043311, -71.629720],
        "description": "<ul><li>Ubicado en San Enrique 473, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "San Enrique 473",
                "phone_1": "+56322511328",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.hotelacontraluz.cl",
                "instagram": "acontraluz_hotelboutique"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Hotel Casa Higueras",
        "logo": "<BASE_URL>/fnb/hotel_casa_higueras.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.040651, -71.630828],
        "description": "<ul><li>Ubicado en Higuera 133, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Higuera 133",
                "phone_1": "+56322497800",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.casahigueras.cl",
                "instagram": "casahigueras"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Hotel Gervasoni",
        "logo": "<BASE_URL>/fnb/hotel_gervasoni.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.041112, -71.626971],
        "description": "<ul><li>Ubicado en Paseo Gervasoni Nº1, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Paseo Gervasoni Nº1",
                "phone_1": "+56322110438",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.hotelgervasoni.cl",
                "instagram": "hotelgervasoni"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Hotel Casa Somerscales",
        "logo": "<BASE_URL>/fnb/hotel_somerscales.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.043234, -71.630078],
        "description": "<ul><li>Ubicado en San Enrique 446, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "San Enrique 446",
                "phone_1": "+56322331006",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.hotelsomerscales.cl",
                "instagram": "hotelsomerscales"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Hotel Puerto natura",
        "logo": "<BASE_URL>/fnb/puerto_natura.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.052812, -71.622424],
        "description": "<ul><li>Ubicado en Héctor Calvo 850, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Héctor Calvo 850",
                "phone_1": "+56981956021",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.puertonatura.cl",
                "instagram": "puertonaturahotel.spa"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Hotel Manoir Atkinson",
        "logo": "<BASE_URL>/fnb/manor_atkinson.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.042765, -71.625312],
        "description": "<ul><li>Ubicado en P.º Atkinson 165, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "P.º Atkinson 165",
                "phone_1": "+56322754257",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.hotelatkinson.cl",
                "instagram": "hotelmanoiratkinson"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Hotel Ultramar Restaurant boutique",
        "logo": "<BASE_URL>/fnb/hotel_ultramar.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.048822, -71.632432],
        "description": "<ul><li>Ubicado en José Joaquín Pérez 173, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "José Joaquín Pérez 173",
                "phone_1": "+56322210000",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.hotelultramar.com",
                "instagram": "hotelultramarvalparaiso"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Verso Hotel",
        "logo": "<BASE_URL>/fnb/hostal.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.053220, -71.621240],
        "description": "<ul><li>Ubicado en Mena 665, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Mena 665",
                "phone_1": "+5622495774",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.versohotel.cl",
                "instagram": "versohotel"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Zerohotel",
        "logo": "<BASE_URL>/fnb/hostal.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.042079, -71.629784],
        "description": "<ul><li>Ubicado en Lautaro Rosas 343, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Lautaro Rosas 343",
                "phone_1": "+56322111313",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.zerohotel.com",
                "instagram": "zerohotel"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Hotel Boutique 17",
        "logo": "<BASE_URL>/fnb/hotel_17.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.041930, -71.626404],
        "description": "<ul><li>Ubicado en Papudo 557, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Papudo 557",
                "phone_1": "+56323327295",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.hotel17.cl",
                "instagram": "hotelboutique17"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Bo Hotel & Terraza",
        "logo": "<BASE_URL>/fnb/hotel_bo.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.044268, -71.630165],
        "description": "<ul><li>Ubicado en Almte. Montt 677, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Almte. Montt 677",
                "phone_1": "+56233564260",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.bohotel.cl",
                "instagram": "bohotel"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Fortunata Chacana Guest House",
        "logo": "<BASE_URL>/fnb/fortunata_chacana.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.027950, -71.633515],
        "description": "<ul><li>Ubicado en Waddington 270, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Waddington 270",
                "phone_1": "+56322801746",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.fortunatachacana.cl",
                "instagram": "fortunatachacana"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "New Voga Hotel Boutique",
        "logo": "<BASE_URL>/fnb/hostal.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.043454, -71.630514],
        "description": "<ul><li>Ubicado en Galos 435, Valparaíso.</li><li>Descuento: 20% según disponibilidad.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Galos 435",
                "phone_1": "+56992547852",
                "phone_2": "",
                "discount": "20% de descuento según disponibilidad",
                "url": "www.newboga.cl",
                "instagram": "newboga"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Casa Club Hostel",
        "logo": "<BASE_URL>/fnb/casa_club_hostel.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.029755, -71.631810],
        "description": "<ul><li>Ubicado en Pedro Leon Gallo 427, Valparaíso, Chile.</li><li>Descuento: 15% de descuento.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Pedro Leon Gallo 427, Valparaíso, Chile",
                "phone_1": "+56 9 7358 5799",
                "phone_2": "",
                "discount": "15% de descuento",
                "url": "casaclub-hostel.valparaiso-hotels.com/es/",
                "instagram": "casaclubhostel"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Hostal El Rincon Marino",
        "logo": "<BASE_URL>/fnb/hostal_el_rincon_marino.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.047950, -71.611270],
        "description": "<ul><li>Ubicado en San Ignacio 454 Valparaiso, Valparaíso, Chile.</li><li>Descuento: 15% de descuento.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "San Ignacio 454 Valparaiso, Valparaíso, Chile",
                "phone_1": "+56 9 7497 1909",
                "phone_2": "",
                "discount": "15% de descuento",
                "url": "elrinconmarino.cl",
                "instagram": "hostalelrinconmarino"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Residencia En El Cerro Bed And Breakfast",
        "logo": "<BASE_URL>/fnb/residencia_en_el_cerro_bed_and_breakfast.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.042124, -71.627880],
        "description": "<ul><li>Ubicado en Pierre Loti 51, Cerro Concepción Valparaíso.</li><li>Descuento: 15% de descuento.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Pierre Loti 51, Cerro Concepción Valparaíso",
                "phone_1": "+56 32 249 5298",
                "phone_2": "+56 9 8776 0993",
                "discount": "15% de descuento",
                "url": "residenciaenelcerro.cl",
                "instagram": "residenciaenelcerro"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Hostal Mirenart",
        "logo": "<BASE_URL>/fnb/hostal_mirenart.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.053851, -71.617052],
        "description": "<ul><li>Ubicado en Calle 13 Nº210 cerro Monjas, Valparaiso.</li><li>Descuento: 15% de descuento.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Calle 13 Nº210 cerro Monjas, Valparaiso",
                "phone_1": "+56 32 332 2178",
                "phone_2": "+56 9 7698 3434",
                "discount": "15% de descuento",
                "url": "hostalmirenart.cl",
                "instagram": "mirenarthostal"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Hostal De Colores",
        "logo": "<BASE_URL>/fnb/hostal_de_colores.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.047288, -71.628616],
        "description": "<ul><li>Ubicado en Cumming 603, Valparaíso, Cerro Carcel, Valparaíso.</li><li>Descuento: 15% de descuento.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Cumming 603, Valparaíso, Cerro Carcel, Valparaíso",
                "phone_1": "+56 9 9421 2450",
                "phone_2": "",
                "discount": "15% de descuento",
                "url": "hostaldecolores.cl",
                "instagram": "decolores_hostal"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Camila 109 Bed And Breakfast",
        "logo": "<BASE_URL>/fnb/camila_109_bed_and_breakfast.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.048851, -71.629303],
        "description": "<ul><li>Ubicado en Calle Camila Nº 109 – Cerro La Loma (Avenida Alemania altura 5600) – Valparaiso.</li><li>Descuento: 15% de descuento.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Calle Camila Nº 109 – Cerro La Loma (Avenida Alemania altura 5600) – Valparaiso",
                "phone_1": "+56 32 249 1746",
                "phone_2": "+56 9 5197 8377",
                "discount": "15% de descuento",
                "url": "camila109.cl",
                "instagram": "camila109bb"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "El Mirador Bed And Breakfast",
        "logo": "<BASE_URL>/fnb/el_mirador_bed_and_breakfast.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.032443, -71.637768],
        "description": "<ul><li>Ubicado en Levarte 251 Cerro Playa Ancha, Valparaíso.</li><li>Descuento: 15% de descuento.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Levarte 251 Cerro Playa Ancha, Valparaíso",
                "phone_1": "+56 32 234 5937",
                "phone_2": "+56 9 9733 3347",
                "discount": "15% de descuento",
                "url": "elmiradordevalparaiso.cl",
                "instagram": "el.miradorbb"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Hostal Recuerdos De Familia",
        "logo": "<BASE_URL>/fnb/hostal_recuerdos_de_familia.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.030952, -71.630483],
        "description": "<ul><li>Ubicado en Taqueadero 502 playa ancha Nº499, Valparaiso.</li><li>Descuento: 15% de descuento.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Taqueadero 502 playa ancha Nº499, Valparaiso",
                "phone_1": "+56 32 249 7909",
                "phone_2": "+56 9 9324 4132",
                "discount": "15% de descuento",
                "url": "recuerdosdefamilia.com",
                "instagram": "recuerdosdefamiliavalpo"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Hostal El Viajero",
        "logo": "<BASE_URL>/fnb/hostal_el_viajero.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.033896, -71.631813],
        "description": "<ul><li>Ubicado en Avenida Carampangue135-131, Valparaíso.</li><li>Descuento: 15% de descuento.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Avenida Carampangue135-131, Valparaíso",
                "phone_1": "+56 9 5735 3512",
                "phone_2": "",
                "discount": "15% de descuento",
                "url": "hostaldelviajero.cl",
                "instagram": "hostal.delviajero"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Apart Hotel Comarca Valparaiso",
        "logo": "<BASE_URL>/fnb/apart_hotel_comarca_valparaiso.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hotel.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.049198, -71.627021],
        "description": "<ul><li>Ubicado en AVENIDA SAN JUAN DE DIOS 601, VALPARAÍSO.</li><li>Descuento: 15% de descuento.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "AVENIDA SAN JUAN DE DIOS 601, VALPARAÍSO",
                "phone_1": "+56 32 249 0378",
                "phone_2": "+56 9 8686 7034",
                "discount": "15% de descuento",
                "url": "comarcavalparaiso.cl",
                "instagram": "comarcavalparaiso"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Hotel Casa Ferrari 406",
        "logo": "<BASE_URL>/fnb/hotel_casa_ferrari_406.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hotel.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.051104, -71.622062],
        "description": "<ul><li>Ubicado en R. H. de Ferrari 406 Cerro Bellavista, Valparaíso, Chile.</li><li>Descuento: 15% de descuento.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "R. H. de Ferrari 406 Cerro Bellavista, Valparaíso, Chile",
                "phone_1": "+56 32 327 1648",
                "phone_2": "+56 9 9401 0565",
                "discount": "15% de descuento",
                "url": "ferrari406.cl",
                "instagram": "hotel.ferrari.406"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Hostal Puerto Encantado",
        "logo": "<BASE_URL>/fnb/hostal_puerto_encantado.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.048276, -71.610669],
        "description": "<ul><li>Ubicado en Victoria 2431, Barrio Almendral Valparaíso.</li><li>Descuento: 15% de descuento.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Victoria 2431, Barrio Almendral Valparaíso",
                "phone_1": "+56 32 317 2011",
                "phone_2": "+56 9 9297 3714",
                "discount": "15% de descuento",
                "url": "puertoencantado.cl",
                "instagram": ""
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Comarca Recreo Eco Hostal",
        "logo": "<BASE_URL>/fnb/comarca_recreo_eco_hostal.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.028768, -71.574289],
        "description": "<ul><li>Ubicado en Cochrane 229, Recreo, Viña del Mar.</li><li>Descuento: 15% de descuento.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Cochrane 229, Recreo, Viña del Mar",
                "phone_1": "+56 32 328 4391",
                "phone_2": "+56 9 9129 8177",
                "discount": "15% de descuento",
                "url": "comarcarecreo.cl",
                "instagram": "comarcarecreo"
            }
        }
    },
    {
        "type": "Estadía",
        "name": "Hostal Plenovalpo",
        "logo": "<BASE_URL>/fnb/hostal_plenovalpo.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/hostal.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.046500, -71.623745],
        "description": "<ul><li>Ubicado en Cerro Bellavista – Becker 131, Cerro Bellavista Valparaíso.</li><li>Descuento: 15% de descuento.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Cerro Bellavista – Becker 131, Cerro Bellavista Valparaíso",
                "phone_1": "+56 9 8804 6688",
                "phone_2": "",
                "discount": "15% de descuento",
                "url": "plenovalpo.cl",
                "instagram": "hostal_plenovalpo"
            }
        }
    },
    {
        "type": "Gastronomía",
        "name": "Restaurant Capri",
        "logo": "<BASE_URL>/fnb/restaurant_capri.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/restaurant.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.039370, -71.628356],
        "description": "<ul><li>Ubicado en Cochrane 664, Valparaíso.</li><li>Descuento: 15% de descuento.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Cochrane 664, Valparaíso",
                "phone_1": "+56 9 3895 6186",
                "phone_2": "",
                "discount": "15% de descuento",
                "url": "restorancapri.cl",
                "instagram": "restorancaprivalpo"
            }
        }
    },
    {
        "type": "Gastronomía",
        "name": "Restaurant Del Barrio",
        "logo": "<BASE_URL>/fnb/restaurant_del_barrio.png",
        "logo_style": "width: 200px;",
        "icon": {
            "url": "<BASE_URL>/fnb/restaurant.png",
            "width": 350,
            "height": 350,
            "anchorY": 350
        },
        "coordinates": [-33.047473, -71.612632],
        "description": "<ul><li>Ubicado en Av Pedro Montt 2302, Valparaiso.</li><li>Descuento: 15% de descuento.</li></ul>",
        "details": {
            "footer": [
                "La reserva es directa con el establecimiento.",
                "Promoción no acumulable con otros descuentos."
            ],
            "conditions": {
                "direction": "Av Pedro Montt 2302, Valparaiso",
                "phone_1": "+56 32 221 3345",
                "phone_2": "",
                "discount": "15% de descuento",
                "url": "lachinganadelbarrio.cl",
                "instagram": "delbarriovalpo"
            }
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
        p['icon']['url'] = p['icon']['url'].replace(
            '<BASE_URL>', f"{base_url}/icons")
        if 'logo' in p.keys():
            p['logo'] = p['logo'].replace('<BASE_URL>', f"{base_url}/logos")
        points_with_url.append(p)
    return points_with_url
