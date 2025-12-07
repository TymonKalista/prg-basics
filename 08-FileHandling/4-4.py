f = open("it_company.csv")

while True:
    for _ in range(5):
        line = f.readline()
        if not line:
            f.close()
            exit()
        print(line.strip())

    input("Press Enter key...")

