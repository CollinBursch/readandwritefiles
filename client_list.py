# Open and read file
infile = open("clients.txt", "r")
# client_file = infile.read()

# for loop, set counter to have numebrs increase down the lsit of clients
counter = 1
for client in infile:
    print(counter, ". ", client.rstrip("\n"), sep="")
    counter += 1
