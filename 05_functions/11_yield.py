# return
# When you use return in a function, it sends back one value and then the function stops completely.
def numbers():
    return 1
    return 2   # ❌ never runs


# yield
# When you use yield, the function doesn’t finish right away.
# It pauses and remembers where it left off.
# Next time you ask it for a value, it continues from there.
def numbers():
    yield 1
    yield 2
    yield 3

# Now if you do:
for n in numbers():
    print(n)


# Easy way to think about it
# return → give me one value, stop forever.
# yield → give me one value, pause, and wait until I ask again.