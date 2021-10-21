def display_chars(file_path, num_chars):
    file = open(file_path)
    data = file.read(num_chars)
    file.close()
    print(data)


def display_line(file_path):
    file = open(file_path)
    line = file.readline(1).strip()
    file.close()
    print(line)


def display_text(file_path):
    file = open(file_path)
    data = file.read()
    file.close()
    print(data)


def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run()
