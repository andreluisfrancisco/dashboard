from dash import html, dcc
from data.dados import MESES, VENDEDORES, CATEGORIAS, CORES_CATEGORIA
import plotly.graph_objects as go


def criar_layout():
    return html.Div([
        html.Div([
            html.H2('Selecione o mês:'),
            criar_dropdown('dropdown-mes', MESES, "Selecione o mês"),
            html.H2('Selecione o vendedor:'),
            criar_dropdown('dropdown-vendedor', VENDEDORES, "Selecione o vendedor"),
            html.H2('Selecione a categoria:'),
            criar_dropdown('dropdown-categoria', CATEGORIAS, "Selecione a categoria"),
        ], className='sidebar', style={'width': '20%', 'padding': '20px', 'background-color': 'white'}),

        html.Div([
            html.H1('Gráfico de Vendas', style={'text-align': 'center'}),
            dcc.Graph(id='grafico-vendas'),
        ], style={'width': '75%', 'padding': '20px', 'background-color': 'white'})
    ], style={'display': 'flex', 'flex-direction': 'row'})

def criar_dropdown(id, opcoes, placeholder):
    return dcc.Dropdown(
        id=id,
        options=[{'label': opcao, 'value': opcao} for opcao in opcoes],
        value=None,
        placeholder=placeholder,
        clearable=True,
        optionHeight=40
    )

def criar_grafico(df_filtrado):
    fig = go.Figure()

    for categoria in df_filtrado['Categoria'].unique():
        dados_categoria = df_filtrado[df_filtrado['Categoria'] == categoria]
        fig.add_trace(
            go.Bar(
                x=dados_categoria['Mes'],
                y=dados_categoria['Vendas'],
                name=categoria,
                marker=dict(color=CORES_CATEGORIA.get(categoria, '#000000'))
            )
        )

    fig.update_layout(
        plot_bgcolor='white',
        width=900,
        height=450,
        xaxis_title="Mês",
        yaxis_title="Vendas (R$)",
        font=dict(color="black"),
        xaxis=dict(showgrid=True, gridcolor='#ccc'),
        yaxis=dict(showgrid=True, gridcolor='#ccc'),
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='white',
        barmode='group'
    )
    
    return fig
