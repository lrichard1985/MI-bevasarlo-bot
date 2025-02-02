# src/security.py
from google.cloud import secretmanager
import os
import json
from oauth2client.service_account import ServiceAccountCredentials

def get_secret(secret_name):
    """
    Lekéri a megadott titok értékét a Google Cloud Secret Managerből.
    :param secret_name: A titok neve a Secret Managerben.
    :return: A titok értéke string formában.
    """
    # Létrehoz egy Secret Manager klienst
    client = secretmanager.SecretManagerServiceClient()

    # A projekt azonosítóját a környezeti változóból veszi
    project_id = os.getenv('GOOGLE_CLOUD_PROJECT')

    # Összeállítja a titok teljes nevét
    secret_version_name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"

    # Lekéri a titok aktuális verziójának értékét
    response = client.access_secret_version(request={"name": secret_version_name})
    secret_value = response.payload.data.decode('UTF-8')

    return secret_value

def get_service_account_credentials():
    """
    Dinamikusan betölti a Google Cloud Service Account JSON kulcsot a Secret Managerből.
    :return: A service account hitelesítő adatai.
    """
    service_account_info = json.loads(get_secret('SERVICE_ACCOUNT_JSON'))
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(service_account_info)
    return credentials
