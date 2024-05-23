# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 09:58:53 2021

@author: william
"""

import sys 

i1= eval(input(sys.argv))
i2= eval(input(sys.argv))
r= i1 + i2
print("%s + %s becomes %s\n with value %s" % \
      (type(i1), type(i2), type(r), r))