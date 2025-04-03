import pydeck as pdk
from bs4 import BeautifulSoup


def create_map(points):
    layer = pdk.Layer(
        "IconLayer",
        data=points,
        get_icon="icon",
        get_size=4,
        size_scale=15,
        get_position="coordinates",
        pickable=True,
    )

    view_state = pdk.ViewState(
        longitude=-71.617950,
        latitude=-33.040821,
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
                    <div style='margin-top: 4px; font-size: 14px;'>{description}</div>
                </div>
            """,
            "style": {
                "backgroundColor": "transparent",
                "border": "none"
            }
        }
    )
    return r.to_html(as_string=True)


def get_map_html(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    script = list(soup.find_all('script'))[-1].string
    return ''.join(
        str(child) for child in soup.body.children) + f"\n<script>{script}</script>"  # noqa
