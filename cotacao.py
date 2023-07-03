import requests

def pegar_cotacoes():
    """
    Função para obter as cotações de dólar, euro e bitcoin em relação ao real.
    """
    try:
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
        requisicao.raise_for_status()  # Lança uma exceção se a requisição falhar
        requisicao_dic = requisicao.json()

        cotacao_dolar = requisicao_dic.get('USDBRL', {}).get('bid')
        cotacao_euro = requisicao_dic.get('EURBRL', {}).get('bid')
        cotacao_btc = requisicao_dic.get('BTCBRL', {}).get('bid')

        if cotacao_dolar and cotacao_euro and cotacao_btc:
            texto = f'''
            Dólar: {cotacao_dolar}
            Euro: {cotacao_euro}
            BTC: {cotacao_btc}'''

            return texto
        else:
            return "Não foi possível obter as cotações."

    except requests.exceptions.RequestException as e:
        return f"Erro na requisição: {e}"
    except ValueError as e:
        return f"Erro ao processar a resposta JSON: {e}"

if __name__ == "__main__":
    cotacoes = pegar_cotacoes()
    print(cotacoes)
