import sys
import os

# hogelib.v2 とバージョンを明示するとそのバージョンになる
import hogelib.v2 as hogelib

if __name__ == '__main__':
  print( hogelib.version() )

  obj = hogelib.SomeClass()
  print( obj.foo() )
  print( obj.specialMethodForV2() )
  
  print( hogelib.COMMON_CONST )
