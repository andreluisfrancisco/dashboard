from dash import Dash, Input, Output
from data.dados import gerar_dados
from grafico.layout import criar_layout, criar_grafico

app = Dash(__name__)
df = gerar_dados()
app.layout = criar_layout()

@app.callback(
    Output('grafico-vendas', 'figure'),
    [
        Input('dropdown-mes', 'value'),
        Input('dropdown-vendedor', 'value'),
        Input('dropdown-categoria', 'value')
    ]
)

def atualizar_grafico(mes_selecionado, vendedor_selecionado, categoria_selecionada):
    df_filtrado = df.copy()
    
    if mes_selecionado:
        df_filtrado = df_filtrado[df_filtrado['Mes'] == mes_selecionado]
    if vendedor_selecionado:
        df_filtrado = df_filtrado[df_filtrado['Vendedor'] == vendedor_selecionado]
    if categoria_selecionada:
        df_filtrado = df_filtrado[df_filtrado['Categoria'] == categoria_selecionada]
    
    return criar_grafico(df_filtrado)

if __name__ == "__main__":
    app.run_server(debug=True)
