#!/usr/bin/env pyhton3
"""
function called filter_datum that returns the log message obfuscated
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    specified fields in a log message using regular expression
    """
    for field in fields:
        message = re.sub(r'(?<={}\{{)[^{}]*(?=\}})'.format(
            re.escape(field), re.escape(separator)), redaction, message)
    return message
