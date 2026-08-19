print("A5.16----list of all built-in function of python")
import builtins

for name, obj in vars(builtins).items():
    if callable(obj) and not isinstance(obj, type):
        print(name)
        
