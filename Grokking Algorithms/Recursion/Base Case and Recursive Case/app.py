# Recursive but not base case so creates an endless loop
#def countdown(i):
#    print(i)
#    countdown(i-1)

#countdown(3)

# Correct version of code above
def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i-1)

countdown(3)