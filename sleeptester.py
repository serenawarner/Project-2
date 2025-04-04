from time import sleep as wait



test_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
bigtest = [test_array, test_array, test_array, test_array, test_array]

for j in bigtest:
    for i in test_array:
        print(test_array[i])
        wait(0.1)
    print("\n")
    wait(0.1)

