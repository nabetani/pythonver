import sys
import os

# hogelib.v1 と書いてもよいが、バージョンを省略すると v1 になる
import hogelib as hogelib

if __name__ == '__main__':
  print( hogelib.version() )

  obj = hogelib.SomeClass()
  print( obj.foo() )

  print( hogelib.COMMON_CONST )
