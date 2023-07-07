#!/usr/bin/python3
"""
Keyword arguments:
argument -- description
Return: return_description
"""

from models.base_model import BaseModel


class User(BaseModel):
    "Inherits from BAseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)