import logging
import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Iniciando execução da função HttpTriggerOnvio")

    # URL do token no GitHub (RAW)
    token_url = "https://raw.githubusercontent.com/andersonhubnexxo/token-onvio/main/token.txt"  # 🔁 Substitua!

    try:
        logging.info("Buscando token no GitHub...")
        token_resp = requests.get(token_url)
        token_resp.raise_for_status()

        token = token_resp.text.strip()
        logging.info(f"Token recebido com {len(token)} caracteres")

        # URL da API da Onvio
        api_url = "https://onvio.com.br/api/br-payroll-sr/v1/interns-registrations"
        headers = {
            "Authorization": f"UDSLongToken {token}"
        }

        logging.info("Chamando API da Onvio...")
        resp = requests.get(api_url, headers=headers)
        resp.raise_for_status()

        logging.info("Sucesso na chamada à API.")
        return func.HttpResponse(resp.text, mimetype="application/json")

    except Exception as e:
        logging.error(f"Erro: {str(e)}")
        return func.HttpResponse(f"Erro: {str(e)}", status_code=500)
