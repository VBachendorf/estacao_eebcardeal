import dash_bootstrap_components as dbc
from dash import html

def umidade_page():
    return html.Div([
        html.H1("Página sobre Umidade"),
        html.P("Aqui está o conteúdo sobre umidade."),
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
