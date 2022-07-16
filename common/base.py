#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: Elastic-2.0
# Copyright (c) 12020 - 12022 HE, Emporia.AI Pte Ltd

__banner__ = """













""" # __banner__

from typing import Any, IO, Optional, List, Dict
from pydantic import BaseModel

class ObjectBase(BaseModel):

    def locate(action, database, factory, obj_name, objects):
        results = []
        for object in objects:
            results.append(object)
        return results

    def search(action, database, factory, obj_name, objects):
        results = []
        for object in objects:
            results.append(object)
        return results

    def verify(self, persist):
        return []

