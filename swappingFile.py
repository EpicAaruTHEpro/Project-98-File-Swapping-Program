def swapFile () :
    file_1 = input("What is the first file to be swapped")
    file_2 = input("What is the second file to be swapped")
    with open(file_1) as a:
        data_a = a.read()
    with open(file_2) as b:
        data_b = b.read()
    with open(file_1, 'w') as a:
        a.write(data_b)
    with open(file_2, 'w') as b:
        b.write(data_a)
swapFile()
