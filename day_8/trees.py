import numpy as np

def main(file: str, mode: str = "first half") -> int:

    np_array = np.genfromtxt(file, delimiter=1, dtype=int)

    shape = np_array.shape

    if mode == "first half":

        visible_trees: int = shape[0] * 2 + shape[1] * 2 - 4
        for i in range(1, shape[0] - 1):
            for j in range(1, shape[1] - 1):
                val = np_array[i, j]

                max_tree_left = np_array[i, :j].max()
                max_tree_right = np_array[i, j+1:].max()
                max_tree_up = np_array[:i, j].max()
                max_tree_down = np_array[i+1:, j].max()
                smallest_max_tree = min(max_tree_left, max_tree_right, max_tree_up, max_tree_down)

                visible_trees += int(val>smallest_max_tree)

        return visible_trees

    else:

        max_scenic_score: int = 0
        
        for i in range(1, shape[0] - 1):
            for j in range(1, shape[1] - 1):
                val = np_array[i, j]

                trees_left = np_array[i, :j]
                blocking_trees_left = np.where(trees_left >= val)
                first_blocking_tree_left = np.max(blocking_trees_left) if np.any(blocking_trees_left) else 0
                dist_left = j - first_blocking_tree_left

                trees_right = np_array[i, j+1:]
                blocking_trees_right = np.where(trees_right >= val)
                dist_right = (np.min(blocking_trees_right) + 1) if len(blocking_trees_right[0]) else (shape[1] - j - 1)

                trees_up = np_array[:i, j]
                blocking_trees_up = np.where(trees_up >= val)
                first_blocking_tree_up = np.max(blocking_trees_up) if np.any(blocking_trees_up) else 0
                dist_up = i - first_blocking_tree_up

                trees_down = np_array[i+1:, j]
                blocking_trees_down = np.where(trees_down >= val)
                dist_down = (np.min(blocking_trees_down) + 1) if len(blocking_trees_down[0]) else (shape[0] - i - 1)

                scenic_score = dist_left * dist_right * dist_up * dist_down

                max_scenic_score = max(max_scenic_score, scenic_score)

        return max_scenic_score
            
if __name__ == "__main__":

    assert main("example.txt") == 21

    print(main("input.txt"))

    assert main("example.txt", "second half") == 8

    print( main("input.txt", "second half"))