Country_Names = ['India', 'russia', 'China', 'Kroatia', 'Ukrain', 'Sweeden', 'England', 'US', 'Iraq', 'Iran', 'Iraq']


def writefile():
    import random
    nums = 5000000
    f = open("TestingDictionary.txt", "w")
    for i in range(nums):
        f.write(random.choice(Country_Names)+'\n')
    f.close()


def readfile():
    count = []
    for c in Country_Names:
        count.append(0)
        print("In count")
    f = open("TestingDictionary.txt", "r")
    for line in f:
        line = line.split()
        if line != "":
            count[Country_Names.index(line)] += 1
            print("Updating count")
    f.close()
    print(count)


def readfiledict():
    count = {}
    for c in Country_Names:
        count["c"] = 0
    with open("TestingDictionary.txt", "r") as f:
        for line in f:
            line = line.split()
            count['line'] += 1
    f.close()
    print(count)

    


