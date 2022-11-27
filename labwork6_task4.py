from typing import List
import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file, delimiter: str = ',', new_line: str = '\n') -> List[dict]:
    with open(file, 'r') as file:
        columns = file.readline().split(new_line)[0].split(delimiter)
        values = ''.join(file.readlines()).split(new_line)[:-1]
        res = []
        dict_res = {}
        n = 0
        while n < len(values):
            lst_ = values[n].split(delimiter)
            for i in range(len(lst_)):
                dict_res[columns[i]] = lst_[i]
            dict_res_copy = dict_res.copy()
            res.append(dict_res_copy)
            n += 1
        return res


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
