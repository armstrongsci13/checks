import check50
import check50.c

@check50.check()
def exists():
    """function1.c exists."""
    check50.exists("function1.c")

@check50.check(exists)
def compiles():
    """function1.c compiles."""
    check50.c.compile("function1.c", lcs50=True)
