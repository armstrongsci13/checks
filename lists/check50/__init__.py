from check50 import *

class lists(Checks):

  @check()
  def exists(self):
    """lists.py exists"""
    self.require("lists.py")
  
  @check("exists")
  def compiles(self):
    """lists.py compiles"""
    self.spawn("clang -o lists lists.py -lcs50 -lm).exit(0)
    
  
