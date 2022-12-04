from typing import List
import string

priority_list = string.ascii_lowercase + string.ascii_uppercase

def main(file: str, mode: str = "first half") -> int:
    with open(file, 'r') as f:
        input_lines = f.readlines()

    priority_sum: int = 0

    if mode == "first half":

        for line in input_lines:

            wrong_item = find_wrong_item(line)
            priority = priority_list.index(wrong_item) + 1
            priority_sum += priority

    else:

        group_list: List[str] = []

        for count, line in enumerate(input_lines):

            group_list += [line]

            if  (count+1) % 3 == 0:
                shared_item = find_shared_item(group_list)
                priority = priority_list.index(shared_item) + 1
                priority_sum += priority
            
                group_list = []


    return priority_sum       
        
def find_wrong_item(line: str) -> str:

    middle_position = int(len(line)/2)
    first_half = line[:middle_position]
    second_half = line[middle_position:]

    for c in first_half:
        if c in second_half:
            return c

def find_shared_item(group_list: List[str]) -> str:
    for c in group_list[0]:
        if (c in group_list[1]) & (c in group_list[2]):
            return c

if __name__ == "__main__":

    assert main("example.txt") == 157

    print(main("input.txt"))

    assert main("example.txt", "second half") == 70

    print( main("input.txt", "second half"))