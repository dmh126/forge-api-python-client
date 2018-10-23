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

Group | Method | Parameters | Endpoint | Description
------------ | ------------ | ------------- | ------------- | -------------
Auth | **authClientTwoLegged** | client_id: string, client_secret: string, scope: string, grant_type: string | /authentication/v1/authenticate |defaults: scope='data:read', grant_type='client_credentials'
Buckets | **getBuckets** |  | /oss/v2/buckets |  |
Buckets | **GetBucketDetails** | bucket_key: string | /oss/v2/buckets/:bucketKey/details | |
Buckets | **createBucket** | bucket_key: string, allow: string, policy_key: string | /oss/v2/buckets | |
Folders | **getFolder** | project_id: string, folder_id: string | /data/v1/projects/:project_id/folders/:folder_id | |
Folders | **getFolderContents** | project_id: string, folder_id: string | /data/v1/projects/:project_id/folders/:folder_id/contents | |
Folders | **getFolderParent** | project_id: string, folder_id: string | /data/v1/projects/:project_id/folders/:folder_id/parent | |
Folders | **getFolderRefs** | project_id: string, folder_id: string | /data/v1/projects/:project_id/folders/:folder_id/refs | |
Folders | **getFolderRelationshipsLinks** | project_id: string, folder_id: string | /data/v1/projects/:project_id/folders/:folder_id/relationships/links | |
Folders | **getFolderRelationships** | project_id: string, folder_id: string | /data/v1/projects/:project_id/folders/:folder_id/relationships/refs | |
Folders | **getFolderSearch** | project_id: string, folder_id: string | /data/v1/projects/:project_id/folders/:folder_id/search | |
Folders | **patchFolder** | project_id: string, folder_id: string, body: dict | /data/v1/projects/:project_id/folders/:folder_id | |
Folders | **postFolder** | project_id: string, body: dict | /data/v1/projects/:project_id/folders | |
Folders | **postFolderRelationshipsRefs** | project_id: string, folder_id: string, body: dict | /data/v1/projects/:project_id/folders/:folder_id/relationships/refs | |
Hubs | **getHubs** |  | /project/v1/hubs | |
Hubs | **getHub** | hub_id: string | /project/v1/hubs/:hub_id | |
Items | **getItem** | project_id: string, item_id: string | /data/v1/projects/:project_id/items/:item_id | |
Items | **getItemParent** | project_id: string, item_id: string | /data/v1/projects/:project_id/items/:item_id/parent | |
Items | **getItemRefs** | project_id: string, item_id: string | /data/v1/projects/:project_id/items/:item_id/refs | |
Items | **getItemRelationshipsLinks** | project_id: string, item_id: string | /data/v1/projects/:project_id/items/:item_id/relationships/links | |
Items | **getItemRelationshipsRefs** | project_id: string, item_id: string | /data/v1/projects/:project_id/items/:item_id/relationships/refs | |
Items | **getItemTip** | project_id: string, item_id: string | /data/v1/projects/:project_id/items/:item_id/tip | |
Items | **getItemVersions** | project_id: string, item_id: string | /data/v1/projects/:project_id/items/:item_id/versions | |
Items | **patchItem** | project_id: string, item_id: string, body: dict | /data/v1/projects/:project_id/items/:item_id | |
Items | **postItem** | project_id: string, body: dict | /data/v1/projects/:project_id/items | |
Items | **postItemRelationshipsRefs** | project_id: string, item_id: string, body: dict | /data/v1/projects/:project_id/items/:item_id/relationships/refs | |
Objects | **putObject** | fpath: string, bucket_key: string, object_name: string | /oss/v2/buckets/:bucketKey/objects/:objectName | |
Objects | **putObjectResumable** | fpath: string, bucket_key: string, object_name: string | /oss/v2/buckets/:bucketKey/objects/:objectName/resumable | |
Objects | **getObjectSession** | bucket_key: string, object_name: string, session_id | /oss/v2/buckets/:bucketKey/objects/:objectName/status/:session_id | |
Objects | **getObjects** | bucket_key: string | /oss/v2/buckets/:bucketKey/objects | |
Objects | **getObjectDetails** | bucket_key: string, object_name: string | /oss/v2/buckets/:bucketKey/objects/:object_name/details | |
Objects | **getObject** | bucket_key: string, object_name: string | /oss/v2/buckets/:bucketKey/objects/:object_name | |
Objects | **postObjectSigned** | data: dict, bucket_key: string, object_name: string | /oss/v2/buckets/:bucketKey/objects/:object_name/signed | |
Objects | **putSignedResource** | fpath: string, id: string | /oss/v2/signedresources/:id | |
Objects | **putSignedResourceResumable** | fpath: string, id: string | /oss/v2/signedresources/:id/resumable | |
Objects | **getSignedResource** | id: string | /oss/v2/signedresources/:id | |
Objects | **deleteSignedResource** | id: string | /oss/v2/signedresources/:id | |
Objects | **copyObject** | bucket_key: string, object_name: string, new_name: string | /oss/v2/buckets/:bucketKey/objects/:objectName/copyto/:newObjectName | |
Objects | **deleteObject** | bucket_key: string, object_name: string | /oss/v2/buckets/:bucketKey/objects/:objectName | |
Projects | **getProjects** | hub_id: string | /project/v1/hubs/:hub_id/projects | |
Projects | **getProject** | hub_id: string, project_id: string | /project/v1/hubs/:hub_id/projects/:project_id | |
Projects | **getProjectHub** | hub_id: string, project_id: string | /project/v1/hubs/:hub_id/projects/:project_id/hub | |
Projects | **getTopFolders** | hub_id: string, project_id: string | /project/v1/hubs/:hub_id/projects/:project_id/topFolders | |
Projects | **getDownload** | project_id: string, download_id: string | /data/v1/projects/:project_id/downloads/:download_id | |
Projects | **getJobs** | project_id: string, job_id: string | /data/v1/projects/:project_id/jobs/:job_id | |
Projects | **postDownload** | project_id: string, body: dict | /data/v1/projects/:project_id/downloads | |
Projects | **postStorage** | project_id: string, body: dict | /data/v1/projects/:project_id/storage | |
Versions | **getVersion** | project_id: string, version_id: string | /data/v1/projects/:project_id/versions/:version_id ||
Versions | **getVersionDownloadFormats** | project_id: string, version_id: string | /data/v1/projects/:project_id/versions/:version_id/downloadFormats ||
Versions | **getVersionDownloads** | project_id: string, version_id: string | /data/v1/projects/:project_id/versions/:version_id/downloads ||
Versions | **getVersionItem** | project_id: string, version_id: string | /data/v1/projects/:project_id/versions/:version_id/item ||
Versions | **getVersionRefs** | project_id: string, version_id: string | /data/v1/projects/:project_id/versions/:version_id/refs ||
Versions | **getVersionLinks** | project_id: string, version_id: string | /data/v1/projects/:project_id/versions/:version_id/links ||
Versions | **getVersionRelationshipsRefs** | project_id: string, version_id: string | /data/v1/projects/:project_id/versions/:version_id/relationships/refs ||
Versions | **patchVersion** | project_id: string, version_id: string, body: dict | /data/v1/projects/:project_id/versions/:version_id ||
Versions | **postVersion** | project_id: string, body: dict | /data/v1/projects/:project_id/versions ||
Versions | **postVersionRelationshipsRefs** | project_id: string, version_id: string, body: dict | /data/v1/projects/:project_id/versions/:version_id/relationships/refs ||

**TODO**

- Model Derivatives
