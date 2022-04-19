import re


def Rename(new_directory, current_file_name, file_extension):
    regex_search = re.search(r'(\([0-9]+\))', current_file_name)
    if new_directory.joinpath(f'{current_file_name}{file_extension}').exists():
        if regex_search:
            file_num = re.sub('[()]', '', regex_search.group(0))
            file_name_no_num = re.sub('[()]', '', re.sub(regex_search.group(0), '', current_file_name)).strip()
            new_num = int(file_num) + 1
            new_file_name = f'{file_name_no_num} ({new_num})'
        else:
            new_file_name = f'{current_file_name} (1)'
    else:
        return f'{current_file_name}{file_extension}'

    if new_directory.joinpath(f'{new_file_name}{file_extension}').exists():
        return Rename(new_directory, new_file_name, file_extension)
    else:
        return f'{new_file_name}{file_extension}'

