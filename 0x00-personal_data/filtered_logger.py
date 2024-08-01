#!/usr/bin/env python3
""" a function called filter_datum that returns the log message obfuscated"""
import logging
import re


def filter_datum(fields, redaction, message, separator):
    ''' replace log data'''
    pattern = f"({'|'.join(fields)})=([^{separator}]*)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
