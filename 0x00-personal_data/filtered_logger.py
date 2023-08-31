#!/usr/bin/env python3
"""
function called filter_datum that returns the log message obfuscated
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    specified fields in a log message using regular expression
    """
    for field in fields:
        pattern = fr'(?<={re.escape(field)}=)[^{re.escape(separator)}]+'
        message = re.sub(pattern, redaction, message)
    return message
