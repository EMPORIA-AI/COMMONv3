#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: Elastic-2.0
# Copyright (c) 12020 - 12022 HE, Emporia.AI Pte Ltd

__banner__ = """













""" # __banner__

from typing import Any, IO, Optional, List, Dict
from .base import *
from enum import Enum

class Scope(Enum):
    Galaxy = 0
    Planet = 1
    Country = 2
    State = 3
    City = 4
    Suburb = 5
    Street = 6
    Building = 7
    Apartment = 8
    Individual = 9

scopes = {}
for scope in Scope:
    scopes[str(scope)[6:]] = scope

class Where(ObjectBase):

    """

'where_1.0 abi

: main
'AU country 'NSW state 'Coolamon city
'///enablers.aromas.import w3w
;

    """

    id: str = ""
    w3w: str = ""
    name: str = ""
    tags: str = ""
    scope: str = ""

    under_id: str = ""

    program: str = ""
    storage: str = ""

    def verify(self, tables):

        results = []

        if not self.under_id == "":
            if not self.under_id in tables.wheres:
                results.append([self, "under_id key not able to be resolved"])

        if not self.scope == "":
            if not self.scope in scopes:
                results.append([self, "scope is not on suppoted list"])

        return results

    def get_letter(self):
        return 'W'
