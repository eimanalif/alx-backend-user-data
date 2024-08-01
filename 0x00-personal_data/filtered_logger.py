#!/usr/bin/env python3
""" a function called filter_datum that returns the log message obfuscated"""
import logging
import re
from typing import List


def filter_datum(
         fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    ''' replace log data'''
    pattern = f"({'|'.join(fields)})=([^{separator}]*)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
