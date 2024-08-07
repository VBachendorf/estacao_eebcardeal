import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from pages.vento_page import vento_page
from pages.temperatura_page import temperatura_page
from pages.umidade_page import umidade_page
from pages.luminosidade_page import luminosidade_page
from pages.pressaoatm_page import pressaoatm_page
from pages.precipitacao_page import precipitacao_page

from func.get_data import view_data

#****************************************************
# TRECHO DO CÓDOGO PARA IMPORTAR DADOS FAVOR RESPEITAR
temp_max = view_data("""SELECT * FROM estacao.temp_data 		where cast(data_hora as date) = curdate()  
		ORDER by temp_dht desc limit 1""")


temp_min = view_data("""SELECT id, data_hora, id_estacao, temp_dht, umidad_dht, lumininosidade, pressao, temp_bmp, uv_intensity FROM estacao.temp_data 
		where cast(data_hora as date) = curdate()  
		ORDER by temp_dht asc limit 1
		""")

temp_now = view_data("""SELECT id, data_hora, id_estacao, temp_dht, umidad_dht, lumininosidade, pressao, temp_bmp, uv_intensity FROM estacao.temp_data ORDER by id desc limit 1""")



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# Definindo o layout do aplicativo
sidebar = html.Div(
    [
        html.H2("Weamet", className="display-4"),
        html.Hr(),
        html.P("Navegue pelas páginas", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Vento", href="/pages/Vento", active="exact"),
                dbc.NavLink("Temperatura", href="/pages/Temperatura", active="exact"),
                dbc.NavLink("Umidade", href="/pages/Umidade", active="exact"),
                dbc.NavLink("Pressão Atmosférica", href="/pages/Pressao_Atmosferica", active="exact"),
                dbc.NavLink("Precipitação", href="/pages/Precipitacao", active="exact"),
                dbc.NavLink("Luminosidade", href="/pages/Luminosidade", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style={
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'bottom': 0,
        'width': '250px',
        'padding': '20px',
        'backgroundColor': '#f8f9fa',
    },
)

content = html.Div(
    id="page-content",
    style={"marginLeft": "270px", "padding": "20px"}
)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# Definindo o conteúdo da página com base na URL
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    card_style = {
        'backgroundColor': '#ffffff',
        'border': 'none',
        'borderRadius': '10px',
        'padding': '20px',
        'margin': '10px',
        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
        'textAlign': 'center',
        'cursor': 'pointer',
        'width': '350px',
        'height': '350px',
        'transition': 'background-color 0.3s',
        'textDecoration': 'none',
        'color': '#000'
    }

    if pathname == '/':
        return html.Div([
            html.H1("Weamet", style={'textAlign': 'center', 'color': '#000'}),
            html.Div(
                className="container",
                children=[
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    [
                                        html.Img(src='https://img.icons8.com/ios/80/000000/wind.png', style={'width': '80px', 'height': '80px'}),
                                        html.H3("Vento", style={'margin': '0', 'color': '#000'}),
                                        html.P("Informações sobre vento")
                                    ],
                                    href="/pages/Vento",
                                    style=card_style
                                ),
                                width=4,
                            ),
                            dbc.Col(
                                dbc.Button(
                                    [
                                        html.Img(src='https://img.icons8.com/ios/80/000000/thermometer.png', style={'width': '80px', 'height': '80px'}),
                                        html.H3("Temperatura", style={'margin': '0', 'color': '#000'}),
                                        
                                        html.H2(f"{temp_now[0]['temp_dht']} °C"),
                                        html.P('Temperatura Atual'),

                                        html.H4(f"{temp_max[0]['temp_dht']} °C"),
                                        html.P('Temperatura Máxima'),
                                        html.H4(f"{temp_min[0]['temp_dht']} °C"),
                                        html.P('Temperatura Mínima')

                                    ],
                                    href="/pages/Temperatura",
                                    style=card_style
                                ),
                                width=4,
                            ),
                            dbc.Col(
                                dbc.Button(
                                    [
                                        html.Img(src='https://img.icons8.com/ios/80/000000/humidity.png', style={'width': '80px', 'height': '80px'}),
                                        html.H3("Umidade", style={'margin': '0', 'color': '#000'})
                                    ],
                                    href="/pages/Umidade",
                                    style=card_style
                                ),
                                width=4,
                            )
                        ],
                        justify="center",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    [
                                        html.Img(src='https://img.icons8.com/ios/50/000000/barometer.png', style={'width': '80px', 'height': '80px'}),
                                        html.H3("Pressão Atmosférica", style={'margin': '0', 'color': '#000'})
                                    ],
                                    href="/pages/Pressao_Atmosferica",
                                    style=card_style
                                ),
                                width=4,
                            ),
                            dbc.Col(
                                dbc.Button(
                                    [
                                        html.Img(src='https://img.icons8.com/ios/50/000000/rain.png', style={'width': '80px', 'height': '80px'}),
                                        html.H3("Precipitação", style={'margin': '0', 'color': '#000'})
                                    ],
                                    href="/pages/Precipitacao",
                                    style=card_style
                                ),
                                width=4,
                            ),
                            dbc.Col(
                                dbc.Button(
                                    [
                                        html.Img(src='https://img.icons8.com/ios/80/000000/sun.png', style={'width': '80px', 'height': '80px'}),
                                        html.H3("Luminosidade", style={'margin': '0', 'color': '#000'})
                                    ],
                                    href="/pages/Luminosidade",
                                    style=card_style
                                ),
                                width=4,
                            )
                        ],
                        justify="center",
                    ),
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": "https://via.placeholder.com/800x400.png?text=Slide+1"},
                            {"key": "2", "src": "https://via.placeholder.com/800x400.png?text=Slide+2"},
                            {"key": "3", "src": "https://via.placeholder.com/800x400.png?text=Slide+3"},
                        ],
                        controls=True,
                        indicators=True,
                        interval=2000,
                        ride="carousel",
                        style={'margin': '20px 0'}
                    )
                ]
            )
        ])
    elif pathname == '/pages/Vento':
        return vento_page()
    elif pathname == '/pages/Temperatura':
        return temperatura_page()
    elif pathname == '/pages/Umidade':
        return umidade_page()
    elif pathname == '/pages/Luminosidade':
        return luminosidade_page()
    elif pathname == '/pages/Precipitacao':
        return precipitacao_page()
    elif pathname == '/pages/Pressao_Atmosferica':
        return pressaoatm_page()
    else:
        return html.Div([
            html.H1("404 - Página não encontrada"),
            html.P("A página que você está procurando não existe."),
            dbc.Button(
                "Voltar para a Página Inicial",
                href="/",
                style={
                    'backgroundColor': '#ffffff',
                    'border': 'none',
                    'borderRadius': '10px',
                    'padding': '10px',
                    'marginTop': '20px',
                    'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
                    'cursor': 'pointer',
                    'transition': 'background-color 0.3s',
                    'textDecoration': 'none',
                    'color': '#000'
                }
            )
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
