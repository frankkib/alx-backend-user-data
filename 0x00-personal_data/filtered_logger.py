#!/usr/bin/env python3
"""
This script demonstrates obfuscating sensitive fields in log messages.
"""

import logging
import csv
import os
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """
    Formatter class to obfuscate sensitive information in log messages.
    """
    REDACTION = "***"
    SEPARATOR = ";"

    def __init__(
            self, fields: List[str], format_str: str = logging.BASIC_FORMAT):
        super().__init__("[HOLBERTON] %(name)s%(levelname)s %(asctime)-15s: %(message)s")
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record while obfuscating specified fields.
        """
        message = super().format(record)
        for field in self.fields:
            pat = fr'(?<={re.escape(field)}=)[^{re.escape(self.SEPARATOR)}]+'
            message = re.sub(pat, self.REDACTION, message)
        return message


PII_FIELDS: List[str] = ['name', 'email', 'phone', 'ssn', 'password']


def get_logger() -> logging.Logger:
    """
    Create and configure a logger instance.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(console_handler)
    return logger


def filter_datum(fields, redaction, message, separator):
    """
    Obfuscate specified fields in a log message using regular expressions.
    Returns:
        str: The log message with specified fields obfuscated.
    """
    for field in fields:
        pattern = fr'(?<={re.escape(field)}=)[^{re.escape(separator)}]+'
        message = re.sub(pattern, redaction, message)
    return message
