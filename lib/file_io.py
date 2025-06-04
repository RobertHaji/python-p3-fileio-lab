

def write_file(file_name, file_content):
    """
    Writes the given content to a .txt file, overwriting any existing content.
    """
    file_path = f"{file_name}.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(file_content)

def append_file(file_name, append_content):
    """
    Appends the given content to the end of a .txt file.
    """
    file_path = f"{file_name}.txt"
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(append_content)


def read_file(file_name):
    """
    Reads and returns the content of a .txt file.
    """
    file_path = f"{file_name}.txt"
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()