# This file contains snippets of Standard Library Modules

# Maintaining the order of a Dictionary
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c#'
favorite_languages['mike'] = 'go'
favorite_languages['fred'] = 'python'

for name, language, in favorite_languages.items()
    print(name.title() + " 's favorite language is " language.title() + ".")