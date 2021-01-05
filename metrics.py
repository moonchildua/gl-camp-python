#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Jan 4 18:22:02 2020
@author: Dariya Mykhaylyshyn
"""

import sys

sys.path.append('./python-package')
import psutil
from loguru import logger

@logger.catch
def main(event, context):
    try:
        general_metric = sys.argv[1]
    except Exception:
        print("Please use an argument cpu or mem to receive the result.")
        sys.exit(1)

    if  general_metric == "mem":
        print("virtual total", psutil.virtual_memory().total)
        print("virtual used", psutil.virtual_memory().used)
        print("virtual free", psutil.virtual_memory().free)
        print("virtual shared", psutil.virtual_memory().shared)
        print("swap total", psutil.swap_memory().total)
        print("swap used", psutil.swap_memory().used)
        print("swap free", psutil.swap_memory().free)

    elif general_metric == "cpu":
        cpu = psutil.cpu_times(percpu=False)
        print("system.cpu.idle", cpu.idle)
        print("system.cpu.user", cpu.user)
        print("system.cpu.guest", cpu.guest)
        print("system.cpu.iowait", cpu.iowait)
        print("system.cpu.stolen", cpu.steal)
        print("system.cpu.system", cpu.system)

    else:
        print("You enter wrong argument. Please use cpu or mem")

if __name__ == "__main__":
    main(None, None)
