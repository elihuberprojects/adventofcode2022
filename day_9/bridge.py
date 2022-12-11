import numpy as np
import re
from typing import Dict, Set, List

move_map: Dict[str, np.ndarray] = {
    "R": np.array([0,1]),
    "L": np.array([0,-1]),
    "U": np.array([1,0]),
    "D": np.array([-1,0]),
}

def main(file: str, mode: str = "first half") -> int:

    KNOTS = 2 if mode == "first half" else 10

    tail_pos_set: Set[str] = set()

    knots_pos: List[np.ndarray] = [np.array([0,0]) for _ in range(KNOTS)]
    with open(file, 'r') as f:
        input_lines = f.readlines()

    for line in input_lines:
        move_dir = line[0]
        move_count = int(re.search(r'\d+', line).group())

        for _ in range(move_count):
            knots_pos[0] += move_map[move_dir]
            for i in range(1, KNOTS):
                dist_vec = knots_pos[i-1] - knots_pos[i]
                if np.linalg.norm(dist_vec) > 1.5:
                    move_vec = np.sign(dist_vec)
                    knots_pos[i] += move_vec

            tail_pos = knots_pos[-1]
            tail_pos_set.add(str(tail_pos[0]) + "-" + str(tail_pos[1]))

    return len(tail_pos_set)




if __name__ == "__main__":

    assert main("example.txt") == 13

    print(main("input.txt"))

    assert main("example.txt", "second half") == 1

    assert main("example_2.txt", "second half") == 36

    print( main("input.txt", "second half"))