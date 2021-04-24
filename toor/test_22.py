file_read = open("./toor/001.txt")
file_write = open("./toor/002.txt", "w")

# while True:
#     text = file.readline()
#
#     if not text:
#         break
#
#     print(text, end="")

while True:
    text = file_read.readline()

    if not text:
        break
    file_write.write(text)


file_read.close()
file_write.close()
