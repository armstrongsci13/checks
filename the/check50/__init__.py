from check50 import *

class the(Checks):

  @check()
  def exists(self):
    """the.py exists"""
    self.require("the.py")
  
  @check("exists")
  def compiles(self):
    """the.py compiles"""
    self.spawn("clang -o the the.py -lcs50 -lm).exit(0)
