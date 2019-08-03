import sys
import os
import hogelib as hogelib

if __name__ == '__main__':
  print( hogelib.version() )

  obj = hogelib.SomeClass()
  print( obj.foo() )
