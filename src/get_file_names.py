#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 17:26:00 2022

@author: green-machine
"""

import os


def get_file_names(matchers: tuple[str]) -> tuple[str]:
    """
    Comprehension Filter for Files in Folder

    Parameters
    ----------
        matchers : tuple[str]
    Returns
    -------
        tuple[str]
    """
    # =========================================================================
    # TODO: any OR all
    # =========================================================================
    return tuple(
        file_name for file_name in os.listdir() if all(match in file_name for match in matchers)
    )
