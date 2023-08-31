#!/usr/bin/env python3
"""
function called filter_datum that returns the log message obfuscated
"""
import re
import logging


def filter_datum(fields, redaction, message, separator):
    """
    specified fields in a log message using regular expression
    """
    for field in fields:
        message = re.sub(r'(?<={}\{{)[^{}]*(?=\}})'.format(
            re.escape(field), re.escape(separator)), redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list):
        """Formatter initializer"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Returns the formattered string"""
        message = super().format(record)
        return filter_datum(
                self.fields, self.REDACTION, message, self.SEPARATOR)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger():
    """
    Logger function that returns a logging.Logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.SetFormatter(formatter)

    logger.addHandler(handler)

    return logger


if __name__ == "__main__":
    logger = get_logger()

    with open("user_data.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            log_message = ", ".join(
                    f"{key}: {value}" for key, value in row.items())
            logger.info(log_message)
