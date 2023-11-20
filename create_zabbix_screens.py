import requests
import json

# Variables for easy changes
zabbix_url = "http://localhost/api_jsonrpc.php"
user = "user"
password = "pass"
host_names = ["test", "server"]
screen_name = "cpu_usage"
graph_name = "CPU Usage"

# Number of hosts per row (adjust as needed)
hosts_per_row = 3

# Function to make requests to the Zabbix API
def zabbix_api(method, params, auth_token=None):
    headers = {'content-type': 'application/json'}
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "auth": auth_token,
        "id": 1
    }
    response = requests.post(zabbix_url, data=json.dumps(data), headers=headers)
    result = response.json().get('result')
    if result is None:
        print(f"Error in {method} API call: {response.json().get('error')}")
    return result

# Get the auth token
auth_token = zabbix_api("user.login", {"user": user, "password": password})

# Get all hosts
hosts = zabbix_api("host.get", {"output": "extend"}, auth_token)

# Filter hosts that have any of the host_names in their names
hosts = [host for host in hosts if any(name in host['name'] for name in host_names)]

# Calculate the number of rows for the screen
vsize = (len(hosts) + hosts_per_row - 1) // hosts_per_row

# Create a screen
screen = zabbix_api("screen.create", {"name": screen_name, "hsize": hosts_per_row, "vsize": vsize}, auth_token)

# Add a graph for each host
for i, host in enumerate(hosts):
    graph = zabbix_api("graph.get", {"hostids": host['hostid'], "search": {"name": graph_name}}, auth_token)
    if graph:
        x = i % hosts_per_row
        y = i // hosts_per_row
        zabbix_api("screenitem.create", {
            "screenid": screen['screenids'][0], 
            "resourcetype": 0, 
            "resourceid": graph[0]['graphid'], 
            "x": x, 
            "y": y, 
            "width": 500, 
            "height": 100
        }, auth_token)
