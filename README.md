# Forge Python Data Management API

**About**

Python library for Data Management API.

**Author**

```
Damian Harasymczuk
harasymczuk@contecht.eu
```

**Requirements**

- Python 3.3

**Installation**

```
git clone https://github.com/dmh126/forge-python-data-management-api.git
cd forge-python-data-management-api
pip install .
```

**How to**

```
from forge_data_management_api import ClientApi

client_id = 'your_client_id'
client_secret = 'client_secret'
scope = 'bucket:read' # ex. 'data:read'

dma = ClientApi()

dma.authClientTwoLegged(client_id, client_secret, scope=scope)

buckets = dma.getBuckets()

print( buckets )
```

**Documentation**

Method | Parameters | Endpoint | Description
------------ | ------------- | ------------- | -------------
**authClientTwoLegged** | client_id: string, client_secret: string, scope: string, grant_type: string | /authentication/v1/authenticate |defaults: scope='data:read', grant_type='client_credentials'


**TODO**

- Fix headers
- Documentation