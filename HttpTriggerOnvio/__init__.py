import logging
import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Iniciando execução da função HttpTriggerOnvio")

    token_url = "https://hubnexxo-my.sharepoint.com/:t:/g/personal/anderson_santana_hubnexxo_com_br/ERyPNOZAYTRPiEj1NAV8GCAByju3EZp-Fw54KzzedptMCw?e=NMuCwd"

    try:
        logging.info("Buscando token do SharePoint...")
        token_resp = requests.get(token_url)
        logging.info(f"Status da resposta do token: {token_resp.status_code}")
        token_resp.raise_for_status()

        token = token_resp.text.strip()
        logging.info(f"Token recebido com {len(token)} caracteres")

        api_url = "https://onvio.com.br/api/br-payroll-sr/v1/interns-registrations"
        headers = { "Authorization": f"UDSLongToken 8016A38B609545C789A119287587AA08" }

        logging.info("Chamando API da Onvio...")
        resp = requests.get(api_url, headers=headers)
        resp.raise_for_status()

        return func.HttpResponse(resp.text, mimetype="application/json")

    except Exception as e:
        logging.error(f"Erro na função: {str(e)}")
        return func.HttpResponse(f"Erro: {str(e)}", status_code=500)

