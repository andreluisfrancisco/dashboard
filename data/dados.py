import pandas as pd
import random

MESES = [
    'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
    'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'
]
VENDEDORES = ['Vendedor A', 'Vendedor B', 'Vendedor C']
CATEGORIAS = ['Eletrônicos', 'Roupas', 'Eletrodomésticos']

CORES_CATEGORIA = {
    'Eletrônicos': '#3498db',
    'Roupas': '#e74c3c',
    'Eletrodomésticos': '#2ecc71'
}

def gerar_dados():
    dados = []

    for mes in MESES:
        for vendedor in VENDEDORES:
            for categoria in CATEGORIAS:
                vendas = random.randint(5000, 30000)
                dados.append({
                    'Mes': mes,
                    'Vendedor': vendedor,
                    'Categoria': categoria,
                    'Vendas': vendas
                })

    return pd.DataFrame(dados)
