import json
from typing import Union, List
from enum import Enum

def first_half(file: str) -> int:

    with open(file, 'r') as f:
        input_lines = f.readlines()
        grouped_lines = list(get_groups(input_lines))

    correct_indices_sum = 0

    for idx, groups in enumerate(grouped_lines):
        comp = check_correct_order(left=groups[0], right = groups[1])
        if comp == ComparisonResult.LEFT_SMALLER:
            correct_indices_sum += idx + 1

    return correct_indices_sum

def second_half(file: str) -> int:
    with open(file, 'r') as f:
        input_lines = f.readlines()

    original_packets: List = []

    sorted_packets: List = []
    
    for line in input_lines:
        if line != "\n":
            original_packets.append(json.loads(line.strip()))

    for op in original_packets:
        _ = insert_in_sorted_list(op, sorted_packets)


    first_idx = insert_in_sorted_list([[2]], sorted_packets) + 1
    second_idx = insert_in_sorted_list([[6]], sorted_packets) + 1

    return first_idx * second_idx

def insert_in_sorted_list(op, sorted_packets) -> int:

    for idx, sp in enumerate(sorted_packets):
        if check_correct_order(op, sp) == ComparisonResult.LEFT_SMALLER:
            sorted_packets.insert(idx, op)
            return idx
            
    sorted_packets.append(op)
    return len(sorted_packets)


def get_groups(input_lines):
    group = []
    for line in input_lines:
        if line == "\n":
            if group:
                yield group
                group = []
        else:
            group.append(json.loads(line.strip()))
    if group:
        yield group


class ComparisonResult(Enum):
    LEFT_SMALLER = "left"
    RIGHT_SMALLER = "right"
    EQUAL = "equal"

def check_correct_order(left: Union[List, int], right: Union[List, int]) -> ComparisonResult:

    left = [left] if isinstance(left, int) else left
    right = [right] if isinstance(right, int) else right

    if left == right:
        return ComparisonResult.EQUAL
        
    left_longer = len(left) > len(right)

    # truncate to same length
    if left_longer:
        left = left[:len(right)]
    else:
        right = right[:len(left)]

    if is_int_list(left) and is_int_list(right):

        for i in range(len(left)):
            if left[i] < right[i]:
                return ComparisonResult.LEFT_SMALLER
            elif left[i] > right[i]:
                return ComparisonResult.RIGHT_SMALLER

    else:
        for i in range(len(left)):
            comp = check_correct_order(left[i], right[i])
            if comp != ComparisonResult.EQUAL:
                return comp

    return ComparisonResult.RIGHT_SMALLER if left_longer else ComparisonResult.LEFT_SMALLER


def is_int_list(list: List) -> bool:
    return all([isinstance(x, int) for x in list])

if __name__ == "__main__":

    assert first_half("example.txt") == 13

    print(first_half("input.txt"))

    assert second_half("example.txt") == 140

    print(second_half("input.txt"))
