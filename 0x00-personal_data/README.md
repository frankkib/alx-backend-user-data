0x00. Personal data
Back-end
Authentification
 By: Emmanuel Turlay, Staff Software Engineer at Cruise
 Weight: 1
 Project will start Aug 30, 2023 6:00 AM, must end by Sep 1, 2023 6:00 AM
 Checker will be released at Aug 30, 2023 6:00 PM
 Manual QA review must be done (request it when you are done with the project)
 An auto review will be launched at the deadline


Resources
Read or watch:

What Is PII, non-PII, and Personal Data?
logging documentation
bcrypt package
Logging to Files, Setting Levels, and Formatting
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

Examples of Personally Identifiable Information (PII)
How to implement a log filter that will obfuscate PII fields
How to encrypt a password and check the validity of an input password
How to authenticate to a database using environment variables
Requirements
All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/env python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle style (version 2.5)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
All your functions should be type annotated
Tasks
0. Regex-ing
mandatory
Write a function called filter_datum that returns the log message obfuscated:

Arguments:
fields: a list of strings representing all fields to obfuscate
redaction: a string representing by what the field will be obfuscated
message: a string representing the log line
separator: a string representing by which character is separating all fields in the log line (message)
The function should use a regex to replace occurrences of certain field values.
filter_datum should be less than 5 lines long and use re.sub to perform the substitution with a single regex.
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))

bob@dylan:~$
bob@dylan:~$ ./main.py
name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x00-personal_data
File: filtered_logger.py
  
1. Log formatter
mandatory
Copy the following code into filtered_logger.py.

import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
Update the class to accept a list of strings fields constructor argument.

Implement the format method to filter values in incoming log records using filter_datum. Values for fields in fields should be filtered.

DO NOT extrapolate FORMAT manually. The format method should be less than 5 lines long.

