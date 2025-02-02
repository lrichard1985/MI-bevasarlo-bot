# src/security.py
from google.cloud import secretmanager
import os

def get_secret(secret_name):
    """
    Lekéri a megadott titok értékét a Google Cloud Secret Managerből.
    :param secret_name: A titok neve a Secret Managerben.
    :return: A titok értéke string formában.
    """
    # Létrehoz egy Secret Manager klienst
    client = secretmanager.SecretManagerServiceClient()

# Lekérni a VERIFY_TOKEN értékét:
verify_token = get_secret('VERIFY_TOKEN')

# Lekérni a PAGE_ACCESS_TOKEN értékét:
page_access_token = get_secret('PAGE_ACCESS_TOKEN')
  
    # A projekt azonosítóját a környezeti változóból veszi
    project_id = os.getenv('GOOGLE_CLOUD_PROJECT')

    # Összeállítja a titok teljes nevét
    secret_version_name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"

    # Lekéri a titok aktuális verziójának értékét
    response = client.access_secret_version(request={"name": secret_version_name})
    secret_value = response.payload.data.decode('UTF-8')

    return secret_value
