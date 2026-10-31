def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()


def read_file_into_list(file_name):
    file_list = []
    with open(file_name) as file:
        for line in file:
            file_list.append(line)
    return file_list


def write_first_line_to_file(file_contents, output_filename):
    content = file_contents.splitlines()[0]
    with open(output_filename, 'w') as file:
        file.write(content)


def read_even_numbered_lines(file_name):
    # WRITE SOLUTION HERE
    content_list = []
    with open(file_name, 'r') as file:
        for key, line in enumerate(file, start=1):
            if (key % 2 == 0):
                content_list.append(line)
    return content_list


def read_file_in_reverse(file_name):
    line_list = []
    with open(file_name, 'r') as file:
        for k, line in enumerate(file):
            line_list.append(line)
        line_list.reverse()
    return line_list

def main():
    file_contents = read_file("sampletext.txt")
    print("File Contents:\n", file_contents)

    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "output.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))


if __name__ == "__main__":
    main()
