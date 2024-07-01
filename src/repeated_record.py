import json

import read_write_json 

def isrepeated(key,n):
    """checks whether input is already in
    db or not

    Args:
        id (int): roll of student or id of teacher

    Returns:
        bool: True id or roll is repeated
    """

    is_repeated = False
    all_records = []
    if key == "Id":
        all_records = read_write_json.read_from_json_file("data/teacher.json", all_records)
    if key == "roll":
        all_records = read_write_json.read_from_json_file("data/student.json", all_records)
     

    for each_record in all_records:
        if key == "roll":
            if each_record["roll"] == n:
                is_repeated = True
                break
        if key == "Id":
            if each_record["Id"] == n:
                is_repeated = True
                break

    return is_repeated

if __name__ == "__main__":
    print(isrepeated("Id", 41))

        