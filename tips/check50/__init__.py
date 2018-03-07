from check50 import *

class the(Checks):

  @check()
  def exists(self):
    """tips.py exists"""
    self.require("the.py")
  
  @check("exists")
  def compiles(self):
    """tips.py compiles"""
    self.spawn("clang -o tips tips.py -lcs50 -lm).exit(0)
