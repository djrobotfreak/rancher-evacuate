import os
import sys
import requests
from requests.auth import HTTPBasicAuth

if "RANCHER_API_HOST" not in os.environ:
    sys.exit("RANCHER_API_HOST environment variable is required")
if "RANCHER_ENVIRONMENT_ID" not in os.environ:
    sys.exit("RANCHER_ENVIRONMENT_ID environment variable is required")
if "RANCHER_ACCESS_KEY" not in os.environ:
    sys.exit("RANCHER_ACCESS_KEY environment variable is required")
if "RANCHER_SECRET_KEY" not in os.environ:
    sys.exit("RANCHER_SECRET_KEY environment variable is required")

rancher_host = os.environ["RANCHER_API_HOST"]
rancher_environment_id = os.environ["RANCHER_ENVIRONMENT_ID"]
rancher_access_key = os.environ["RANCHER_ACCESS_KEY"]
rancher_secret_key = os.environ["RANCHER_SECRET_KEY"]
base_environment_url = rancher_host + "/v2-beta/projects/" + rancher_environment_id + "/"
basic_auth = HTTPBasicAuth(rancher_access_key, rancher_secret_key)

hostname = str(requests.get("http://169.254.169.254/latest/meta-data/local-hostname").text)
all_hosts = requests.get(base_environment_url + "hosts", auth=basic_auth).json()["data"]
filtered_hosts = [host for host in all_hosts if str(host["hostname"]) == hostname]
if len(filtered_hosts) < 1:
    sys.exit("Could not find host by hostname")

this_host_id = filtered_hosts[0]["id"]
requests.post(base_environment_url + "hosts/" + this_host_id + "?action=evacuate", auth=basic_auth)