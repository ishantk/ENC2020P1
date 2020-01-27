# Key Word Arguments -> Dictionary
def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))


fun(a=10, b=20, name="John")
