import datetime
import os
import shutil


def copy_input_files_in_output_dir(input_dir: str, output_dir: str):
    files = get_files_from_directory(input_dir)

    for file in files:
        if os.path.exists(os.path.join(input_dir, file)) and not os.path.exists(os.path.join(output_dir, file)):
            shutil.copy(os.path.join(input_directory, file), output_directory)


def rename_files(directory: str, digits_in_name: int):
    files = get_files_from_directory(directory)
    files.sort(key=sort_function)
    for index, file in enumerate(files):
        index += 1
        _, extension = os.path.splitext(file)

        prefix = ''
        if len(str(index)) < digits_in_name:
            prefix = '0' * (digits_in_name - len(str(index)))

        new_file = prefix + str(index) + extension
        shutil.move(os.path.join(directory, file), os.path.join(directory, new_file))


def change_extension_in_directory(directory: str, extension: str):
    files = get_files_from_directory(directory)

    for file in files:
        filename = os.path.splitext(file)
        new_filename = filename[0] + extension
        shutil.move(os.path.join(directory, file), os.path.join(directory, new_filename))

def check_dir_exist(*directories):
    for directory in directories:
        if not os.path.exists(directory):
            raise Exception(f'Directory does not exist: {directory}')


def get_files_from_directory(directory: str):
    check_dir_exist(directory)
    return os.listdir(directory)

def sort_function(elem: str):
    dot_index = elem.index('.')
    index = int(elem[:dot_index])
    return index

if __name__ == '__main__':
    input_directory = os.path.join(os.getcwd(), 'input_files')
    output_directory = os.path.join(os.getcwd(), 'output_files')
    check_dir_exist(input_directory, output_directory)

    now_date = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
    os.mkdir(os.path.join(output_directory, now_date))
    output_directory = os.path.join(output_directory, now_date)

    copy_input_files_in_output_dir(input_directory, output_directory)
    rename_files(output_directory, 3)
    # change_extension_in_directory(output_directory, '.png')
