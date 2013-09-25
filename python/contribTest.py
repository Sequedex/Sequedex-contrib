#!/usr/bin/env python
from __future__ import absolute_import,  unicode_literals,  nested_scopes,  print_function

import sys
import os

print('Hello from %s!'%os.path.realpath(__file__))
try:
   sequedexContrib = os.environ['SEQUEDEX_CONTRIB']
except KeyError:
   sequedexContrib = '$SEQUEDEX_CONTRIB'
print('Contributed programs and data from GitHub live in the %s directory.'
      %sequedexContrib)
print('You can update them using the "sequedex-pullContrib" command.')
sys.exit(0)
