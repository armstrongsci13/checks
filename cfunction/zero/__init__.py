import check50
import check50.c

@check50.check()
def exists():
    """function0.c exists."""
    check50.exists("function0.c")

@check50.check(exists)
def compiles():
    """function0.c compiles."""
    check50.c.compile("function0.c", lcs50=True)

@check50.check(compiles)
