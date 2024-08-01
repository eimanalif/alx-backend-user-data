#!/usr/bin/env python3
""" a function called filter_datum that returns the log message obfuscated"""
import logging
import re
from typing import List
import mysql.connector
import os

PII_FIELDS = ("name", "email", "phone", "ssn", "password")

def filter_datum(
         fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    ''' replace log data'''
    pattern = f"({'|'.join(fields)})=([^{separator}]*)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    FORMAT_FIELDS = ('name', 'levelname', 'asctime', 'message')
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """formats a LogRecord"""
        original_message = super(
            RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, original_message, self.SEPARATOR)



def get_logger() -> logging.Logger:
    """Creates new logger for user data"""
    logger = logging.getLogger("user_data")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.addHandler(stream_handler)
    return logger

if __name__ == "__main__":
    main()
