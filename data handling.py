def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."

def main():
    filename = "sample.txt"

    # Write content to the file
    content_to_write = "Hello, this is some content that will be written to the file.\n"
    write_to_file(filename, content_to_write)

    # Append content to the file
    content_to_append = "This is additional content that will be appended to the file.\n"
    append_to_file(filename, content_to_append)

    # Read and print content from the file
    file_content = read_from_file(filename)
    print("File Content:")
    print(file_content)

if __name__ == "__main__":
    main()
