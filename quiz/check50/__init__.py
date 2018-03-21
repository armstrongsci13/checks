from check50 import *

class quiz(Checks):

  @check()
  def exists(self):
    """quiz.py exists"""
    self.require("quiz.py")
  
  @check("exists")
  def compiles(self):
    """quiz.py compiles"""
    self.spawn("clang -o quiz quiz.py -lcs50 -lm).exit(0)
