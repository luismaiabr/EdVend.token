# config.py  
INTEGRATION_ID = "5d7809a9-6378-4673-97ce-82c70ddabfe4"  
SECRET_KEY = "qBJ0qWBM96MwXKtMgwaAsMvgHLmjgmMVCxFDJKhf6BxtB2Ob2fVYFnUggvmN9Vkm"  
REDIRECT_URI = "sua_uri_de_redirecionamento"  

import requests
import base64

def get_tokens(authorization_code):
    # URLdo endpoint de token
    token_url = "https://atendimentocentralesquadrias.kommo.com/oauth2/access_token"
    
    # Preparar as credenciais em Base64
    credentials = f"{INTEGRATION_ID}:{SECRET_KEY}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    
    # Headers da requisição
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/json"
    }
    
    # Dados da requisição
    data = {
        "grant_type": "authorization_code",
        "code": authorization_code,
        "redirect_uri": REDIRECT_URI
    }
    
    # Fazer a requisição
    response = requests.post(token_url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao obter tokens: {response.text}")

# Uso
try:
    tokens = get_tokens("seu_codigo_de_autorizacao")
    access_token = tokens["access_token"]
    #refresh_token = tokens["refresh_token"]
    print(f"Tokens obtidos com sucesso!:{access_token}")
except Exception as e:
    print(f"Erro: {str(e)}")

