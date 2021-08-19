# formatting strings with f""
# replacement field begins and ends with {}
# expressions are evaluated at runtime
# adding an equal after the expression will output "expression = value"
# conversion field: If a conversion is specified, the result of evaluating the expression is converted before formatting.
# Conversion '!s' calls str() on the result, '!r' calls repr(), and '!a' calls ascii().
# format specifier: f"result: {value:{width}.{precision}}"  # nested fields


""" TOPICS"""

# Comments
# Readablity is the single most important aspect of a program. If code is confusing, please add comments.
# Comments begin with "# ". Comments describe some or all of the following code. Use complete sentences.
# Use a empty comment line to seperate paragraphs.

# Formatting
# Read PEP 8 -- Style Guide for Python Code here: https://www.python.org/dev/peps/pep-0008/
# Use autopep8 to autoformat code.
# Here is some info on setting up autopep8: https://code.visualstudio.com/docs/python/editing

# Linting
# Linting detects errors. I suggest using pylint in vscode.
# Here is a guide to setting up linting: https://code.visualstudio.com/docs/python/linting
# Install format files extension on vs code to use pylint on directories.
# Add this to your settings.json file to enable all linting. Then, disable errors selectively.
# "python.linting.pylintArgs": [
#         "--enable=F,E,C,R,W",
#         "--disable="
#     ],

# Literals
# Here are some of the built in data types in python: https://docs.python.org/3/library/stdtypes.html
# For more specialized data types, consult this page: https://docs.python.org/3/library/datatypes.html
# int
# Integers are whole numbers. Note: leading zeros are not allowed for non-zero numbers.
# For long numbers, use underscores for readability. For example,
# 1_000_000 instead of 1000000.
# Example,
# Population = 1_000_000
#
# float
# Floating point numbers represent decimal numbers.
# 10.5 or 8.54e10 (scientific notation)
# san_antonio_longitude = 31.789
#
# str
# Denotes a string, or a collection of characters within single or double quotes.
# Multy line strings can be created using triple quotes.
# "" is equivalent to ''
# always use """ """ not ''' '''
# city = 'San Antonio'
# or
# city = "San Antonio"
# description = """San Antonio is a city in Texas.
# There is a lot happening in San Antonio."""
#
# f-strings
# Lets talk about formatted strings or f-strings
# city = "San Antonio"
# message_about_city = "The name of the city is San Antonio."
# dynamic_message_about_city = f"The name of the city is {city}".
# \n in a string designates a newline

# Docstrings
# Find information on docstring conventions here: https://www.python.org/dev/peps/pep-0257/
# I personally do not think docstrings are neccessary for everything, but in many cases,
# docstrings are very helpful for people reading your code.