def oops():
    result = [(x, y) for x in range(10) for y in range(5) if x * y > 10]
    """
        creates a list of tuples that 
    """


    return ((x, y, z)
            for x in range(5)
            for y in range(5)
            if x != y
            for z in range(5)
            if y != z
            )

result = oops()

for i in result:
    print(i)
