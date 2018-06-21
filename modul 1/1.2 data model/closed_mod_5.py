def closest_mod_5(x):
    return x if x % 5 == 0 else x + 5 - (x % 5)
