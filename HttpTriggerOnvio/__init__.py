
import logging
import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Executando função: HttpTriggerOnvio")

    # Substitua essa URL pelo caminho correto do seu token.txt no SharePoint
    token_url = "https://hubnexxo.sharepoint.com/sites/.../token.txt"

    try:
        token_resp = requests.get(token_url)
        token_resp.raise_for_status()
        token = token_resp.text.strip()

        api_url = "https://onvio.com.br/api/br-payroll-sr/v1/interns-registrations"
        headers = {
            "Authorization": f"UDSLongToken {token}"
        }

        resp = requests.get(api_url, headers=headers)
        resp.raise_for_status()

        return func.HttpResponse(resp.text, mimetype="application/json")

    except Exception as e:
        return func.HttpResponse(f"Erro: {str(e)}", status_code=500)
