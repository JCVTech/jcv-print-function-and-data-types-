>>> print("Hello world!")
Hello world!
>>> print('my favourite colour are', 'purple', 'blue' 'green')
my favourite colour are purple bluegreen
>>> print('my favourite colour are', 'purple', 'blue', 'green')
my favourite colour are purple blue green
>>> print('Hello', 'world!')
Hello world!
>>> my_interger_var = 26
>>> print('JCV Age:' my_interger_var)
  File "<python-input-5>", line 1
    print('JCV Age:' my_interger_var)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('JCV Age:', my_interger_var)
JCV Age: 26
>>> jcv_float_var = 3.85
>>> print('JCV ND 1 GPA:', jcv_float_var)
JCV ND 1 GPA: 3.85
>>> jcv_string_var = 'JOSH COMPUTER VENTURE'
>>> print('MY NAME:', jcv_string_var)
MY NAME: JOSH COMPUTER VENTURE
>>> jcv_boolean_var = True
>>> print('JCV is a Brilliant Student? True or False:', jcv_boolean_var)
JCV is a Brilliant Student? True or False: True
>>> jcv_set_var = {26, 3.85, 'JCV', True}
>>> print('Provide all Answers respectively:', jcv_set_var)
Provide all Answers respectively: {True, 26, 3.85, 'JCV'}
>>> jcv_dictionary_var = {'CEO Name': 'Josh Computer Venture', 'Age': 26}
>>> print('Details:', jcv_dictionary_var)
Details: {'CEO Name': 'Josh Computer Venture', 'Age': 26}
>>> jcv_tuple_var = (26, 3.85, 'Josh Computer Venture')
>>> print('My age, GPA and Name:', jcv_tuple_var)
My age, GPA and Name: (26, 3.85, 'Josh Computer Venture')
>>> jcv_range_var = range(25-30)
>>> print('Age range of JCV', jcv_range_var)
Age range of JCV range(0, -5)
>>> jcv_list_var = [ 1 'JCV TECH', 1.5 'JCV FOREX', 2 'JCV TRADE']
  File "<python-input-21>", line 1
    jcv_list_var = [ 1 'JCV TECH', 1.5 'JCV FOREX', 2 'JCV TRADE']
                     ^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>> jcv_list_var = [ 1, 'JCV TECH', 1.5, 'JCV FOREX', 2, 'JCV TRADE']
>>> print('My Portfolio:', jcv_list-var)
Traceback (most recent call last):
  File "<python-input-23>", line 1, in <module>
    print('My Portfolio:', jcv_list-var)
                           ^^^^^^^^
NameError: name 'jcv_list' is not defined
>>> print('My Portfolio:', jcv_list_var)
My Portfolio: [1, 'JCV TECH', 1.5, 'JCV FOREX', 2, 'JCV TRADE']
>>> jcv_none_var = None
>>> print('Which Language does JCV speaks German, Spanish, Calabar:', jcv_none_var)
Which Language does JCV speaks German, Spanish, Calabar: None
>>> print(type (jcv_none_var))
<class 'NoneType'>
>>> print(type(jcv_list_var))
<class 'list'>
>>> print(type(jcv_tuple_var))
<class 'tuple'>
>>> print(type(jcv_float_var))
<class 'float'>
>>> isinstance('Hello World' int)
  File "<python-input-31>", line 1
    isinstance('Hello World' int)
               ^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> isinstance('Hello World', int)
False
>>> isinstance(['age', 3.4, 26], set)
False
>>>
KeyboardInterrupt
>>> print(type(['age', 3.4, 26])
...
... print(type('age', 3.4 26))
... print(type('age' 3.2)
...
  File "<python-input-34>", line 3
    print(type('age', 3.4 26))
    ^^^^^
SyntaxError: invalid syntax
>>>
>>>
>>>
