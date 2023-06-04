#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:37:25 2022

@author: green-machine
"""


from lib import get_names

PATH_SRC = '/home/green-machine/production'
PATH_EXP = '/home/green-machine/web'


file_names_dir_src = get_names(PATH_SRC)
file_names_dir_dst = get_names(PATH_EXP)
print(file_names_dir_dst)
