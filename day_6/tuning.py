EXAMPLES_DICT = {
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb": (7, 19),
    "bvwbjplbgvbhsrlpgdmjqwftvncz": (5, 23),
    "nppdvjthqldpwncqszvftbrmjlhg": (6, 23),
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": (10, 29),
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": (11, 26),
}

from input import INPUT_SIGNAL

def main(signal: str, mode: str = "first half") -> int:

    needed_distict_chars = 4 if mode == "first half" else 14
     
    for pos in range(needed_distict_chars, len(signal) + 1):
        chars = signal[pos-needed_distict_chars: pos]
        if len(set(chars)) == needed_distict_chars:
            return pos

if __name__ == "__main__":

    for signal, expected_marker in EXAMPLES_DICT.items():
        assert main(signal=signal) == expected_marker[0]

    print(main(signal=INPUT_SIGNAL))

    for signal, expected_marker in EXAMPLES_DICT.items():
        assert main(signal=signal, mode = "second half") == expected_marker[1]

    print(main(signal=INPUT_SIGNAL, mode="second half"))
