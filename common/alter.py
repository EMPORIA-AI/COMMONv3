#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: Elastic-2.0
# Copyright (c) 12020 - 12022 HE, Emporia.AI Pte Ltd

__banner__ = """













""" # __banner__

from typing import Any, IO, Optional, List, Dict
from .base import *

#
# alters, typically taxes and success fees on the exchange have access to
# pricing information.  by convention where taxes are applied after, the
# buyer agrees to pay these edits.
#

class Alter(ObjectBase):

    #
    # 'alter_v1.0 abi
    #
    # : main apply-alter ;
    #
    # 'Charity/Oceans classification
    # <TRUE> is-optional 1.0 rate-percent
    # 'https://seashepherd.org charge-url
    # '33VL8dzvoXbzshUWAPvrhiAiX3tBAdPPmL remit-btc
    #

    """


    """

    id: str = ""
    name: str = ""
    tags: str = ""

    vkey: str = ""

    where_id: str = ""

    program: str = ""
    storage: str = ""

    def get_letter(self):
        return 'A'
