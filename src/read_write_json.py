import json

def read_from_json_file(file_path, file_list):
    try:
        with open(file_path, "r") as file:
            file_list = json.load(file)
    except:
        pass

    return file_list

def write_to_json_file(file_path, file_list):
    with open(file_path, "w") as file:
        json.dump(file_list, file, indent=4)