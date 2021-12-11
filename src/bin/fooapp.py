#!/usr/bin/env python3
from carcano.foolist import *

import os
import logging
import logging.config

log_config_paths = [
    os.path.dirname(os.path.realpath(__file__))+'/logging.conf',
    '/etc/fooapp/logging.conf']

log_enabled = False

for log_config_file in log_config_paths:
    if os.path.isfile(log_config_file):
        log_enabled = True
        break
if log_enabled is True:
    logging.config.fileConfig(
        fname=log_config_file,
        disable_existing_loggers=False
    )
    logger = logging.getLogger(__name__)
    logging.info(__file__+': started')

os_list = Foolist()
os_list.unique = True
os_list.append('RedHat', True)
os_list.append('Suse', True)
os_list.append('CentOS', False)
os_list.append('CentOS', False)
print("Print the list:")
for os in os_list:
    print(os)
print("Print the list in ascending order:")
for os in sorted(os_list):
    print(os)
os_list.remove('CentOS')
os_list.append('Rocky Linux', False)
print("Print the list - after the removal of CentOS:")
for os in os_list:
    print(os)

print("Print the list in descending order:")
for os in sorted(os_list, reverse=True):
    print(os)
if log_enabled is True:
    logging.info(__file__+': finished')
