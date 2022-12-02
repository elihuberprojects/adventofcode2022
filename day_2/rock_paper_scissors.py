from typing import Dict

HAND_POSITION: Dict[str, int] = {
    "A": 1,
    "B": 2,
    "C": 3,
}

MOVE_DIFF_POINTS_MAP: Dict[int, int] = {
    0: 3,
    1: 6,
    2: 0,
}

INV_MOVE_DIFF_POINTS_MAP = {v: k for k, v in MOVE_DIFF_POINTS_MAP.items()}

WANTED_POINTS_ENCODING: Dict[str, int] = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}


def main(file: str, mode: str = "first half") -> int:
    with open(file, 'r') as f:
        input_lines = f.readlines()

    total_points: int = 0

    for line in input_lines:
        first_char = line[0]
        second_char = line[2]

        if mode == "first half":

            my_move = HAND_POSITION[chr(ord(second_char) - 23)] # Map X,Y,Z to A,B,C
            move_diff = my_move - HAND_POSITION[first_char]
            total_points += MOVE_DIFF_POINTS_MAP[move_diff % 3] + my_move # use modulo for "looping" around the dict (e.g. -2 -> 1)
        
        elif mode == "second half":

            wanted_points = WANTED_POINTS_ENCODING[second_char]
            needed_move_diff = INV_MOVE_DIFF_POINTS_MAP[wanted_points]
            my_move = (HAND_POSITION[first_char] + needed_move_diff) % 3
            my_move = 3 if my_move == 0 else my_move # stupid fix for the modulo, which returns 0 for scissors move, whereas we expect 3
            total_points += wanted_points + my_move

    return total_points



if __name__ == "__main__":

    assert main("example.txt") == 15

    print(main("input.txt"))

    assert main("example.txt", "second half") == 12

    print( main("input.txt", "second half"))