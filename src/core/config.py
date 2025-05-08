#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 20:00:00 2025

@author: alexandermikhailov
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

DIR = os.getenv('DIR')
PATH = Path(DIR)

PATH_CTR = Path(DIR)
PATH_DST = Path(DIR)
PATH_SRC = Path(DIR)
PATH_TST = Path(DIR)
PATH_LOG = Path(DIR)
