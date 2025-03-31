import pydeck as pdk
from bs4 import BeautifulSoup


def create_map(points):
    # layer = pdk.Layer(
    #     "ScatterplotLayer",
    #     data=points,
    #     pickable=True,
    #     opacity=0.6,
    #     filled=True,
    #     radius_scale=5,
    #     radius_min_pixels=2,
    #     radius_max_pixels=10,
    #     get_position="coordinates",
    #     get_radius=10,
    #     get_fill_color=[0, 137, 88],
    # )

    layer = pdk.Layer(
        "IconLayer",
        data=points,
        get_icon="icon",
        get_size=4,
        size_scale=15,
        get_position="coordinates",
        pickable=True,
    )

    # Vista del mapa centrada en Viña del Mar
    view_state = pdk.ViewState(
        longitude=-71.617950,
        latitude=-33.040821,
        zoom=13.5,
        # pitch=45,
    )


    # Renderizar
    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style="light",
        # map_style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json",  # noqa
        height="500px",
        width="100%",
        tooltip={
            "html": "<b>{name}</b><br/>{description}",
            # "style": {
            #     "backgroundColor": "steelblue",
            #     "color": "white"
            # }
        }
    )


    return r.to_html(as_string=True)


def get_map_html(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    script = list(soup.find_all('script'))[-1].string
    return ''.join(
        str(child) for child in soup.body.children) + f"\n<script>{script}</script>"  # noqa
