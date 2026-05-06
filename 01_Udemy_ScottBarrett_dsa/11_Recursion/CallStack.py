def funcThree():
    print('Three')

def funcTwo():
    funcThree()
    print("Two")

def funcOne():
    funcTwo()
    print('One')


funcOne()



# Debug this to know exactly how this callStack works in detail.