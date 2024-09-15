import json
from pathlib import Path

def carregar_dados_json(caminho_arquivo):
    try:
        arquivo = Path(caminho_arquivo)
        if arquivo.is_file():
            with arquivo.open('r') as f:
                dados = json.load(f)
            return dados.get("dias", [])
        else:
            raise FileNotFoundError(f"Arquivo {caminho_arquivo} nao encontrado.")
    except json.JSONDecodeError as e:
        return f"Erro ao carregar JSON: {e}"

def calcular_faturamento(dados_faturamento):
    faturamento_validos = [dia['faturamento'] for dia in dados_faturamento if dia['faturamento'] > 0]

    if not faturamento_validos:
        return "ERRO: Nao ha faturamentos validos."

    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)

    media_faturamento = sum(faturamento_validos) / len(faturamento_validos)

    dias_acima_media = sum(1 for f in faturamento_validos if f > media_faturamento)

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_media": dias_acima_media
    }

if __name__ == "__main__":
    caminho_arquivo = 'faturamento.json'
    dados_faturamento = carregar_dados_json(caminho_arquivo)

    if isinstance(dados_faturamento, str):
        print(dados_faturamento)
    else:
        resultados = calcular_faturamento(dados_faturamento)
        if isinstance(resultados, str):
            print(resultados)
        else:
            print(f"Menor faturamento: {resultados['menor_faturamento']}")
            print(f"Maior faturamento: {resultados['maior_faturamento']}")
            print(f"Numero de dias acima da media: {resultados['dias_acima_media']}")
