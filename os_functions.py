import os


def get_current_dir():
    cwd = os.getcwd()
    return cwd


def create_directory(directory_name, parent_dir=os.getcwd()):
    parent_dir_path = os.path.abspath(os.path.join(parent_dir, os.pardir))
    directory_path = os.path.join(parent_dir_path, directory_name)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def list_directory_contents(path=os.getcwd()):
    return os.listdir(path)


def remove_file(file_name: str, folder_path: str = os.getcwd()) -> None:
    os.chdir(folder_path)
    os.remove(file_name)


def create_file(file_name, content="This text is default", dir_path=os.getcwd()):
    parent_dir = os.path.abspath(os.path.join(dir_path, os.pardir))
    file_path = os.path.join(parent_dir, file_name)
    with open(file_path, 'w') as f:
        f.write(content)


def rename_file_or_folder(current_name, new_name):
    try:
        # Check if the file or folder exists
        if os.path.exists(current_name):
            # Join the current directory with the current name to get the full path
            current_path = os.path.join(os.getcwd(), current_name)

            # Join the current directory with the new name to get the full path for the new name
            new_path = os.path.join(os.getcwd(), new_name)

            # Rename the file or folder
            os.rename(current_path, new_path)

        else:
            print(f"The file or folder '{current_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def check_file_existence(file_name):
    result = os.path.exists(file_name)  # giving the name of the file as a parameter.
    return result


def get_file_size(file_name):
    if os.path.exists(file_name):
        size = os.path.getsize(file_name)
        return size

