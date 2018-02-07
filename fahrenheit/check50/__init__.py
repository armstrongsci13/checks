from check50 import *

class Fahrenheit(Checks):

  @check()
  def exists(self):
    """fahrenheit.py exists"""
    self.require("fahrenheit.py")
  
  @check("exists")
  def compiles(self):
    """fahrenheit.py compiles"""
    self.spawn("clang -o fahrenheit fahrenheit.py -lcs50 -lm).exit(0)
    
  @check("compiles")
  def test_neg40_(self)
    """Input of -40 yeilds output of 4"""
    self.spawn("python fahrenheit.py").stdin("-40").stout("-40", "-40").exit(0)
