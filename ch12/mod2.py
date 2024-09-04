import os

# double fake for testing
if os.environ.get("UNIT_TEST", ""):
    import ch12.fake_mod1 as mod1
else:
    import ch12.mod1 as mod1


def summer(x: int, y: int) -> str:
    return mod1.preamble() + f"{x + y}"
