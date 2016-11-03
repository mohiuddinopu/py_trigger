import json
from cm_api.api_client import ApiResource
from cm_api.endpoints.types import ApiClusterTemplate
from cm_api.endpoints.cms import ClouderaManager
import socket
import os

cwd = os.getcwd()
hostname = (socket.gethostname())

print hostname
print cwd


resource = ApiResource(hostname, 7180, "admin", "admin", version=12)
cluster = resource.get_cluster("Cluster 1")
template = cluster.export()
with open( cwd + '/template.json', 'w') as outfile:
   json.dump(template.to_json_dict(), outfile, indent=4, sort_keys=True)
