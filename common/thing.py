#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: Elastic-2.0
# Copyright (c) 12020 - 12022 HE, Emporia.AI Pte Ltd

__banner__ = """













""" # __banner__

from typing import Any, IO, Optional, List, Dict
from .base import *

class Thing(ObjectBase):

    #
    # 'thing_v1.0 abi
    #
    # : genre init-genre ;
    #

    """

    """

    id: str = ""
    name: str = ""
    tags: str = ""

    vkey: str = ""

    genre_id: str = ""
    rpc_json: str = ""

    broker_id = ""
    holder_id = ""

    program: str = ""
    storage: str = ""

    def get_letter(self):
        return 'T'

