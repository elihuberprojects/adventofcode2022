from typing import List

def main(file: str, mode: str = "first half") -> int:

    value_history: List[int] = []

    interesting_indexes = [20, 60, 100, 140, 180, 220]

    with open(file, 'r') as f:
        input_lines = f.readlines()

    with open(f'output_{file}', 'w') as f:
        for line in input_lines:

            if len(value_history) % 40 == 0:
                f.write("\n")

            current_value = value_history[-1] if value_history else 1
            f.write("#") if current_value - 1 <= len(value_history) % 40 <= current_value + 1 else f.write(".")
            value_history.append(current_value)

            if line.startswith("addx"):

                if len(value_history) % 40 == 0:
                    f.write("\n")
                f.write("#") if current_value - 1 <= len(value_history) % 40 <= current_value + 1 else f.write(".")
                v = int(line.replace("addx", "").strip())
                value_history.append(current_value + v)
                
    return sum([value_history[i-2] * i for i in interesting_indexes]) 
    # -1 as the cycle counter starts with 1, and another -1 as we want the values DURING the 20th cycle 
    # (which means at value 19, which means at list index 18)

if __name__ == "__main__":

    assert main("example.txt") == 13140

    print(main("input.txt"))