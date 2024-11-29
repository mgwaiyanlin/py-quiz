GLOBAL_VAR = 10

def print_global():
    global GLOBAL_VAR
    GLOBAL_VAR += 11
    print(GLOBAL_VAR)

# print(GLOBAL_VAR)
print_global()

