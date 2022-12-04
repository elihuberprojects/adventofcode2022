import re

def main(file: str, mode: str = "first half") -> int:
    with open(file, 'r') as f:
        input_lines = f.readlines()

    full_cover_pairs: int = 0
    overlap_pairs: int = 0

    for line in input_lines:
        all_numbers = [int(s) for s in re.findall(r'\d+',line)]

        is_full_cover_pair = (all_numbers[2] - all_numbers[0]) * (all_numbers[3] - all_numbers[1]) <= 0
        no_overlap = (all_numbers[1] < all_numbers[2]) | (all_numbers[3] < all_numbers[0])

        full_cover_pairs += is_full_cover_pair
        overlap_pairs += not no_overlap

    return full_cover_pairs if mode == "first half" else overlap_pairs

if __name__ == "__main__":

    assert main("example.txt") == 2

    print(main("input.txt"))

    assert main("example.txt", "second half") == 4

    print( main("input.txt", "second half"))