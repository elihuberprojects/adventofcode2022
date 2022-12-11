import re
from typing import List, Dict

DISK_SPACE = 70000000
UPDATE_SIZE = 30000000

def main(file: str, mode: str = "first half") -> int:
    with open(file, 'r') as f:
        input_lines = f.readlines()

    currently_active_dirs: List[str] = []

    dir_size_dict: Dict[str, int] = {}

    all_dirs = []

    for line in input_lines:
        if line.startswith("$ cd"):
            cd_match = line.replace("$ cd ", "").replace("\n", "")
            if cd_match != "..":
                currently_active_dirs.append(cd_match)
            else:
                currently_active_dirs.pop()

            continue

        size_match = re.search(r'\d+', line)
        if size_match:
            size_match = int(size_match.group())
            for i in range(len(currently_active_dirs)):

                dir = "/".join(currently_active_dirs[:i+1])
                if dir in dir_size_dict.keys():
                    dir_size_dict[dir] += size_match
                else:
                    dir_size_dict[dir] = size_match

    if mode == "first half":

        return sum([x for x in dir_size_dict.values() if x <= 100000])

    else: 

        currently_taken_space = dir_size_dict["/"]
        currently_free_space = DISK_SPACE - currently_taken_space
        needed_additional_free_space = UPDATE_SIZE - currently_free_space

        return min([x for x in dir_size_dict.values() if x >= needed_additional_free_space])



if __name__ == "__main__":

    assert main("example.txt") == 95437

    print(main("input.txt"))

    assert main("example.txt", "second half") == 24933642

    print( main("input.txt", "second half"))