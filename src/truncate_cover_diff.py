path = "docs/table.txt"
file = open(path, "w")
file.write("This is a table\n")
file.write("1 2 3\n")
file.close()
file = open(path, "w")
# Open the file in write mode,but not write anything, the file will be truncated
file.close()