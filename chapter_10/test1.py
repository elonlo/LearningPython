try:
    float(['float() dese not', 'likes lists', 2])
except TypeError, diag:
    type(diag)
    print diag
