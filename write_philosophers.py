def main():
    outfile = open("philosophers.txt", "w")

    outfile.write("John Locke\n")
    outfile.write("David Hume\n")
    outfile.write("Edmund Burke\n")

    outfile.close()


def add_my_name():
    # How to open in append mode
    outfile = open("philosophers.txt", "a")

    outfile.write("Collin Bursch\n")

    outfile.close()


main()
add_my_name()
