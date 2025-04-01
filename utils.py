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
                <div style="
                    background: rgba(249, 249, 249, 0.95);
                    border: 1px solid #ddd;
                    border-radius: 1.5rem;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    padding: 8px 12px;
                    font-family: Arial, sans-serif;
                    color: #333;
                    transition: all 1.4s ease;
                    width: 30%;
                    text-align: justify;
                    text-align-last: left;
                ">
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
