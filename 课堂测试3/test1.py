def print_name(fn, ln, mn=""): 
    if mn == "":
        print(fn + " " + ln)
    else:
        print(fn + " " + mn + " " + ln)

print_name("jimi","hendrix")
print_name("john","hooker","lee")