from typing import List
import re


def main(file: str, mode: str = "first half") -> str:
    with open(file, 'r') as f:
        input_lines = f.readlines()

    amount_of_stacks: int = 0

    for line in input_lines:
        if line.startswith(" 1"):
            amount_of_stacks = int(line[-3])

    list_of_stacks: List[List[str]] = [[] for _ in range(amount_of_stacks)]

    for line in input_lines:

        # Build up the starting stack
        if line.strip().startswith("["):
            for stack_index, pos in enumerate(range(1, amount_of_stacks * 4, 4)):
                char = line[pos]
                if not char == " ":
                    list_of_stacks[stack_index].insert(0, char)

        
        # Do the moves
        if line.startswith("move"):
            all_numbers = [int(s) for s in re.findall(r'\d+',line)]

            if mode == "first half":
                for _ in range(all_numbers[0]):
                    popped_char = list_of_stacks[all_numbers[1] - 1].pop()
                    list_of_stacks[all_numbers[2] - 1].append(popped_char)

            else:
                popped_chars = list_of_stacks[all_numbers[1] - 1][-all_numbers[0]:]
                del list_of_stacks[all_numbers[1] - 1][-all_numbers[0]:]
                list_of_stacks[all_numbers[2] - 1].extend(popped_chars)

    return "".join([stack.pop() for stack in list_of_stacks])


if __name__ == "__main__":

    assert main("example.txt") == "CMZ"

    print(main("input.txt"))

    assert main("example.txt", "second half") == "MCD"

    print( main("input.txt", "second half"))