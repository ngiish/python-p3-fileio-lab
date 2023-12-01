def write_file(file_name="test_file", file_content="This is a test content."):
    with open(f'{file_name}.txt', 'w') as file:
        file.write(file_content)

def append_file(file_name="test_file", append_content="\nAppended content."):
    with open(f'{file_name}.txt', 'a') as file:
        file.write(append_content)

def read_file(file_name="test_file"):
    with open(f'{file_name}.txt', 'r') as file:
        return file.read()

write_file()
append_file()
read_file()