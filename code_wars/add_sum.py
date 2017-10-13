# Adds all the numbers from 1 to the given integer
# Returns False if parameter is negative

def add_all(int):
    if int < 0:
        return(False)
    else:
        return sum(range(int + 1))


add_all(100)
