Como pegar dados com APIS com Python
Para consumir APIs em Python, a biblioteca `requests` é a mais utilizada por sua simplicidade. Siga estes passos:

### 1. **Instale a biblioteca `requests`**
```bash
pip install requests
```

### 2. **Exemplo Básico (GET Request)**
```python
import requests

# URL de exemplo (API pública)
url = "https://jsonplaceholder.typicode.com/posts/1"

# Envia requisição GET
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código 200)
if response.status_code == 200:
    # Converte a resposta JSON para dicionário Python
    data = response.json()
    print(data)
else:
    print(f"Erro: {response.status_code}")
```

### 3. **Parâmetros em Requisições GET**
```python
params = {"userId": 1}
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)
```

### 4. **Enviando Dados (POST Request)**
```python
new_post = {
    "title": "Teste",
    "body": "Conteúdo de exemplo",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post  # Usa 'json' para enviar como JSON
)

if response.status_code == 201:  # 201 = Created
    print("Dados enviados!")
    print(response.json())  # Resposta da API
```

### 5. **Headers e Autenticação**
```python
headers = {
    "Authorization": "Bearer SEU_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(
    "https://api.example.com/data",
    headers=headers
)
```

### 6. **Tratamento de Erros**
```python
try:
    response = requests.get("https://api.example.com/data", timeout=5)  # Timeout de 5 segundos
    response.raise_for_status()  # Lança exceção para códigos 4xx/5xx
    data = response.json()
except requests.exceptions.HTTPError as err:
    print(f"Erro HTTP: {err}")
except requests.exceptions.RequestException as err:
    print(f"Erro na requisição: {err}")
```

### 7. **Exemplo com Autenticação Básica**
```python
from requests.auth import HTTPBasicAuth

response = requests.get(
    "https://api.example.com/secure",
    auth=HTTPBasicAuth("usuário", "senha")
)
```

### Principais Conceitos:
- **Métodos HTTP**: `get()`, `post()`, `put()`, `delete()`.
- **Parâmetros**:
  - `params`: Dados para query string (GET).
  - `json`: Dados serializados como JSON (POST/PUT).
  - `headers`: Cabeçalhos personalizados.
  - `auth`: Autenticação.
- **Resposta**:
  - `response.status_code`: Código HTTP.
  - `response.json()`: Converte resposta JSON em objeto Python.
  - `response.text`: Conteúdo bruto da resposta (string).

### APIs Públicas para Testes:
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/)
- [OpenWeatherMap](https://openweathermap.org/api)
- [PokeAPI](https://pokeapi.co/)

### Documentação Oficial:
- [`requests`](https://requests.readthedocs.io/)

Com esses passos, você consegue interagir com a maioria das APIs RESTful! 😊