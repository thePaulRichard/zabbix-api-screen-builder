# Zabbix API Screen Builder

Automate the creation of dynamic Zabbix screens with host-specific graphs using the Zabbix API.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)

## Introduction

This Python script interacts with the Zabbix API to automate the creation of screens with host-specific graphs. It is designed to simplify the process of setting up monitoring dashboards for multiple hosts.

## Features

- Dynamically create Zabbix screens based on specified hosts.
- Customize the layout and arrangement of graphs on the screens.
- Utilize the Zabbix API for seamless integration.

## Usage

1. Modify the script with your Zabbix server details, authentication credentials, and other parameters.

    - **host_names**: Specify a list of host names to filter and include in the dashboard. For example:

        ```python
        host_names = ["nginx", "aws"]
        ```

        In this case, all servers with names containing "nginx" or "aws" (e.g., nginxsvr1, nginxsvr2, svrnginx1, awsserver1, serveraws2) will be added to the Zabbix screen.

    - **graph_name**: Define the name of the graph you want to add to the Zabbix screen. This variable retrieves the graph from the specified hosts. Note that the graph must exist on the hosts for this to work. Example:

        ```python
        graph_name = "CPU Usage"
        ```
1. Run the script:

    ```python
    python create_zabbix_screens.py
    ```

1. Check your Zabbix dashboard for the dynamically created screens with host-specific graphs.
