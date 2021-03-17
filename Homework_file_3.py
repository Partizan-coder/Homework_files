import os


def get_file(file_count):
    for i in range(file_count):
        i += 1
        file_path = os.path.join(os.getcwd(), 'Result.txt')
        with open(file_path, 'a') as file:
            file_name = 'File_' + str(i) + '.txt'
            file_path = os.path.join(os.getcwd(), file_name)
            with open(file_path, 'r') as f:
                file.write(file_name + "\n")
                file_name = os.path.basename(file_path).split('.')[0]
                file.write(file_name + "\n")
                for line in f:
                    line = line
                    file.write(line)
            if i != file_count:
                file.write("\n")
    return


def get_clear_file():
    file_path = os.path.join(os.getcwd(), 'Result.txt')
    with open(file_path, 'w') as f:
        f.write("")
    return


get_clear_file()
files_count = 3
get_file(files_count)
