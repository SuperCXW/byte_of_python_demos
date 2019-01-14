# import sys
import os
from sys import call_tracing

print('The command line arguments are:')
# for i in sys.argv:
#     print(i)

# print('\n\nThe PYTHONPATH is', sys.path, '\n')

print(os.getcwd())

# print(call_tracing(os.getcwd(), None))

print(os.__name__)

print(__name__)

