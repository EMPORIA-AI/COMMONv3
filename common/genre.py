#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: Elastic-2.0
# Copyright (c) 12020 - 12022 HE, Emporia.AI Pte Ltd

__banner__ = """













""" # __banner__

from typing import Any, IO, Optional, List, Dict
from .base import *

class Genre(ObjectBase):

    #
    # 'genre_v1.0 abi
    #
    # : main
    # 'Drinks/Human major 'Energy/Sugar_Free minor
    # ("Red Bull") brand 'ML unit 250 size 4 count
    # ;
    #

    """

    """

    id: str = ""
    name: str = ""
    tags: str = ""
    program: str = ""
    storage: str = ""

    def get_letter(self):
        return 'G'
