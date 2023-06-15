# Написать скрипт, вставляющий [+,-] в промежуток между цифрами от 9 до 0, чтобы получилось 200
import random
import time


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time} seconds")
        return result

    return wrapper


class EquationFinder:

    def __init__(self, result_aim: int):
        self.aim = result_aim
        self.max_iter = 10000
        self.list_len = None
        self.results = []

    @measure_execution_time
    def processing(self, sequence: str):
        self.list_len = len(sequence)
        try_value = 0
        while self.max_iter > try_value:
            res_stack = self._generate_rnd_stack(sequence)
            res_value = self._calculate_expression(res_stack)

            if res_value == self.aim:
                expression_str = ''.join([str(x) for x in res_stack])

                if expression_str not in self.results:
                    self.results.append(expression_str)

            try_value += 1

    def _generate_rnd_stack(self, sequence: str):
        start_index, end_index = 0, 1
        expression_stack = list()

        max_index = len(sequence) - 1
        while max_index >= start_index:
            value = int(sequence[start_index:end_index])
            if self.aim > value and len(sequence) > end_index:
                end_index += 1
                continue
            end_index -= 1

            if start_index != end_index:
                rnd_end_index = random.randint(start_index + 1, end_index)
                rnd_value = int(sequence[start_index:rnd_end_index])
                rnd_choice = random.choice(["+", "-", "+"])

                expression_stack += [rnd_value, rnd_choice]
                start_index, end_index = rnd_end_index, rnd_end_index + 1
            else:
                expression_stack.append(int(sequence[end_index]))
                start_index, end_index = start_index + 1, end_index + 2

        return expression_stack

    @staticmethod
    def _calculate_expression(stack: list):
        res = stack[0]

        for index in range(1, len(stack), 2):
            operator = stack[index]
            operand = stack[index + 1]

            res = res + operand if operator == '+' else res - operand

        return res

    def print_result(self):
        print(f"Results for {self.max_iter} tries:")
        [print(x) for x in self.results]


if __name__ == "__main__":
    res_aim = 200
    start_sequence = ''.join([str(x) for x in range(9, -1, -1)])

    e_finder = EquationFinder(res_aim)
    e_finder.processing(start_sequence)
    e_finder.print_result()
