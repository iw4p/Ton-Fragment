try:
    from .helpers.server import *
    from .models.numbers.numbers import Numbers
except ImportError:
    from helpers.server import *
    from src.fragments.models.numbers.numbers import Numbers

x = Numbers("status", "sort", 1)
print(x.res())