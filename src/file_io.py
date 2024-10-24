# Description: File I/O operations in Python
path = "docs/example.txt"

try:
    # Open file in read mode
    file = open(path, "r")
    print(file.read())
    # Append to file
    # 'a': Open for writing. The file is created if it does not exist. The file is seeked to the end before each write.
    # 'w': Open for writing. The file is created if it does not exist. If the file exists it truncates the file.
    file = open(path, "a")
    file.write("nmsl")
except IOError:
    print(
        "IOError occurred, The cause may be the file does not exist or the file is not readable."
    )
    file.close()
file.close()
