def is_provide_variable(var):
    if var.isidentifier():
        return True
    else:
        return False
print(is_provide_variable('hello_world')) #True
print(is_provide_variable('hello world')) #False