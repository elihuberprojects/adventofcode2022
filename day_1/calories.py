from typing import List

def main(file: str, mode: str = "first half") -> int:
    with open(file, 'r') as f:
        input_lines = f.readlines()


    current_sum: int = 0
    all_sums: List[int] = []
    for line in input_lines:
        if line.strip():
            current_sum += int(line)

        else:
            all_sums += [current_sum]

            current_sum = 0

    all_sums += [current_sum] # add very last group


    if mode == "first half":
        return max(all_sums)
    else:
        return sum(sorted(all_sums, reverse=True)[:3])

if __name__ == "__main__":

    assert main("example.txt") == 24000

    print(main("input.txt"))

    assert main("example.txt", "second half") == 45000

    print( main("input.txt", "second half"))