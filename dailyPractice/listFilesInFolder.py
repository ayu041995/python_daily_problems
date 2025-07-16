import os

folders = input("Please provide list of folder names with spaces in between : ").split()
# print(folders)

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name : " + folder)
        break

    print(" --- listing files for folder ---" + folder)
    # print(files)

    for file in files:
        print(file)