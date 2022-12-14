from typing import List, Callable, Optional
import math

class Monkey():
    def __init__(self, starting_items: List[int], operation: Callable[[int], int], test_modulo: int, mode: str = "first half") -> None:

        self.starting_items = starting_items
        self.operation = operation
        self.test_modulo = test_modulo
        self.mode = mode

        self.test_true_target: Optional[Monkey] = None
        self.test_false_target: Optional[Monkey] = None
        self.magic_number: Optional[int] = None

        self.inspection_counter: int = 0

    def inspect(self, item: int) -> int:
        self.inspection_counter += 1
        return self.operation(item)

    def relief(self, item: int) -> int:
        if self.mode == "first half":
            return int(item/3)
        else:
            return item % self.magic_number

    def test(self, item: int):
        if item % self.test_modulo == 0:
            self.test_true_target.starting_items.append(item)
        else:
            self.test_false_target.starting_items.append(item)

    def process_item(self, item: int):
        self.test(self.relief(self.inspect(item)))

    def process_all_items(self):
        for item in self.starting_items:
            self.process_item(item)
        self.starting_items = []

def get_example_monkeys() -> List[Monkey]:

    monkey_0 = Monkey(starting_items=[79, 98], operation= lambda x: x * 19, test_modulo=23)
    monkey_1 = Monkey(starting_items=[54, 65, 75, 74], operation= lambda x: x + 6, test_modulo=19)
    monkey_2 = Monkey(starting_items=[79, 60, 97], operation= lambda x: x * x, test_modulo=13)
    monkey_3 = Monkey(starting_items=[74], operation= lambda x: x + 3, test_modulo=17)

    monkey_0.test_true_target = monkey_2
    monkey_0.test_false_target = monkey_3

    monkey_1.test_true_target = monkey_2
    monkey_1.test_false_target = monkey_0

    monkey_2.test_true_target = monkey_1
    monkey_2.test_false_target = monkey_3

    monkey_3.test_true_target = monkey_0
    monkey_3.test_false_target = monkey_1

    return [monkey_0, monkey_1, monkey_2, monkey_3]

def get_input_monkeys() -> List[Monkey]:
    monkey_0 = Monkey(starting_items=[65, 78], operation= lambda x: x * 3, test_modulo=5)
    monkey_1 = Monkey(starting_items=[54, 78, 86, 79, 73, 64, 85, 88], operation= lambda x: x + 8, test_modulo=11)
    monkey_2 = Monkey(starting_items=[69, 97, 77, 88, 87], operation= lambda x: x + 2, test_modulo=2)
    monkey_3 = Monkey(starting_items=[99], operation= lambda x: x + 4, test_modulo=13)
    monkey_4 = Monkey(starting_items=[60, 57, 52], operation= lambda x: x * 19, test_modulo=7)
    monkey_5 = Monkey(starting_items=[91, 82, 85, 73, 84, 53], operation= lambda x: x + 5, test_modulo=3)
    monkey_6 = Monkey(starting_items=[88, 74, 68, 56], operation= lambda x: x * x, test_modulo=17)
    monkey_7 = Monkey(starting_items=[54, 82, 72, 71, 53, 99, 67], operation= lambda x: x + 1, test_modulo=19)

    monkey_0.test_true_target = monkey_2
    monkey_0.test_false_target = monkey_3

    monkey_1.test_true_target = monkey_4
    monkey_1.test_false_target = monkey_7

    monkey_2.test_true_target = monkey_5
    monkey_2.test_false_target = monkey_3

    monkey_3.test_true_target = monkey_1
    monkey_3.test_false_target = monkey_5

    monkey_4.test_true_target = monkey_7
    monkey_4.test_false_target = monkey_6

    monkey_5.test_true_target = monkey_4
    monkey_5.test_false_target = monkey_1

    monkey_6.test_true_target = monkey_0
    monkey_6.test_false_target = monkey_2

    monkey_7.test_true_target = monkey_6
    monkey_7.test_false_target = monkey_0

    return [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]


def main(use_example_monkeys: bool = False, mode: str = "first half"):

    monkey_list = get_example_monkeys() if use_example_monkeys else get_input_monkeys()

    MAX_ROUNDS: int = 20 if mode == "first half" else 10000

    if mode != "first half":
        magic_number = math.prod([monkey.test_modulo for monkey in monkey_list])
        for monkey in monkey_list:
            monkey.magic_number = magic_number
            monkey.mode = mode

    for _ in range(MAX_ROUNDS):
        for monkey in monkey_list:
            monkey.process_all_items()

    inspection_counters = sorted([monkey.inspection_counter for monkey in monkey_list])

    print(inspection_counters)

    return inspection_counters[-1] * inspection_counters[-2]

if __name__ == "__main__":

    assert main(use_example_monkeys=True) == 10605

    print(main())

    assert main(use_example_monkeys=True, mode="second half") == 2713310158

    print(main(mode="second half"))
