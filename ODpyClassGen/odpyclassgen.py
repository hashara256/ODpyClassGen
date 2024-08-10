import msal
import requests
import xml.etree.ElementTree as ET
import json

# --- Configuration Variables ---
client_id = 'your-client-id'  # Replace with your Azure AD Application (client) ID
tenant_id = 'your-tenant-id'  # Replace with your Azure AD Tenant ID
redirect_uri = 'http://localhost'  # Redirect URI configured in your Azure AD app
service_instance = 'https://your-service-instance-url'  # Replace with your OData service URL

# --- URLs and Scopes ---
authority = f'https://login.microsoftonline.com/{tenant_id}'
scope = [f'{service_instance}/.default']
base_url = f'{service_instance}/data/'
metadata_url = f'{base_url}$metadata'

# --- Functions ---

def authenticate():
    """Authenticates the user and returns the access token."""
    app = msal.PublicClientApplication(client_id, authority=authority)
    result = app.acquire_token_interactive(scopes=scope, redirect_uri=redirect_uri)

    if 'access_token' in result:
        print('Authentication successful!')
        return result['access_token']
    else:
        raise Exception(f"Authentication failed: {result.get('error_description', 'No further details available')}")

def get_metadata(access_token):
    """Retrieves and parses the OData metadata."""
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(metadata_url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to retrieve metadata: {response.status_code} - {response.text}")

    print('Metadata retrieval successful!')
    return response.content

def parse_metadata(metadata):
    """Parses the OData metadata and generates Python classes."""
    root = ET.fromstring(metadata)
    namespace = {
        'edmx': 'http://docs.oasis-open.org/odata/ns/edmx',
        'm': 'http://schemas.microsoft.com/ado/2007/08/dataservices/metadata'
    }

    entity_types = root.findall('.//m:EntityType', namespaces=namespace)

    for entity_type in entity_types:
        generate_class(entity_type)

def generate_class(entity_type):
    """Generates a Python class for an OData entity type."""
    class_name = entity_type.attrib['Name']
    print(f'class {class_name}:')
    print(f'    base_url = "{base_url}{class_name}"')

    print('    def __init__(self):')
    for prop in entity_type.findall('m:Property', namespaces=namespace):
        prop_name = prop.attrib['Name']
        prop_type = prop.attrib['Type'].split('.')[-1]
        print(f'        self.{prop_name} = None  # {prop_type}')

    print_methods(class_name)

def print_methods(class_name):
    """Prints the standard methods and a search method for the generated class."""
    print('    def to_dict(self):')
    print('        return {')
    for prop in entity_type.findall('m:Property', namespaces=namespace):
        prop_name = prop.attrib['Name']
        print(f'            "{prop_name}": self.{prop_name},')
    print('        }')
    print()

    print('    def create(self, access_token):')
    print('        headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}')
    print('        response = requests.post(self.base_url, headers=headers, data=json.dumps(self.to_dict()))')
    print('        return response.status_code, response.json()')
    print()

    print('    def update(self, access_token, entity_id):')
    print('        headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}')
    print('        response = requests.patch(self.base_url + f"({entity_id})", headers=headers, data=json.dumps(self.to_dict()))')
    print('        return response.status_code, response.json()')
    print()

    print('    def delete(self, access_token, entity_id):')
    print('        headers = {"Authorization": f"Bearer {access_token}"}')
    print('        response = requests.delete(self.base_url + f"({entity_id})", headers=headers)')
    print('        return response.status_code')
    print()

    print('    @staticmethod')
    print('    def search(access_token, **kwargs):')
    print('        headers = {"Authorization": f"Bearer {access_token}"}')
    print('        filters = " and ".join([f"{k} eq \'{v}\'" for k, v in kwargs.items()])')
    print('        query_url = f"{class_name}.base_url?$filter={filters}"')
    print('        response = requests.get(query_url, headers=headers)')
    print('        return response.status_code, response.json()')
    print()

# --- Main Execution ---

if __name__ == "__main__":
    try:
        access_token = authenticate()
        metadata = get_metadata(access_token)
        parse_metadata(metadata)
    except Exception as e:
        print(f"Error: {e}")

