import logging
import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Iniciando execução da função HttpTriggerOnvio")

    # URL do token no GitHub (RAW)
    token_url = "https://raw.githubusercontent.com/andersonhubnexxo/token-onvio/main/token.txt"

    try:
        logging.info("Buscando token no GitHub...")
        token_resp = requests.get(token_url)
        token_resp.raise_for_status()

        token = token_resp.text.strip()
        logging.info(f"Token recebido com
