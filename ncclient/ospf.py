# set up ospf for one router
import os
from ncclient import manager
from rich import print

if __name__ == "__main__":
  device = {
    "host": "192.168.1.23",
    "port": 830,
    "username": "valerie",
    "password": "cisco:,
    "hostkey_verify": False,
  }

with manager.connec(**device) as nconf:
  print(list(nconf.server_capabilities))

with manager.connect(**device) as nconf:
  nc_pley = nconf.get_config(source="running")
  print(type(nc_reply))


