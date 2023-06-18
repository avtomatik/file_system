# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:43:02 2020

@author: Alexander Mikhailov
"""

import os

file_names = tuple(
    file_name for file_name in os.listdir() if file_name != 'scripts.zip'
)
