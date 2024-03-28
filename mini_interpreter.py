class Interpreter:
    def __init__(self) -> None:
        self.stack = []
        self.envirnment = {}

    # the interpreter works with pushing and poping to stack so we use list for it
    def LOAD_VALUE(self, number):
        self.stack.append(number)

    # we use load value so add number to stack
    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def ADD_TWO_VALUES(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)
    # these three methods are the instructions that the interpreter understants

    def STORE_NAME(self, name):
        val = self.stack.pop()
        self.envirnment[name] = val

    def LOAD_NAME(self, name):
        val = self.envirnment[name]
        self.stack.append(val)

    def pase_arguments(self, instruction, argument, to_be_executed):
        """to understand what the argument to each instruction means."""
        numbers = ["LOAD_VALUE"]
        names = ["LOAD_NAME", "STORE_NAME"]

        if instruction in numbers:
            argument = to_be_executed["numbers"][argument]
        
        elif instruction in names:
            argument = to_be_executed["names"][argument]
        
        return argument

    def run_code(self, to_be_executed):
        """runs the code"""
        instructions = to_be_executed["instructions"]
        numbers = to_be_executed["numbers"]
        for each_step in instructions:
            instruction, argument = each_step
            argument = self.pase_arguments(instruction, argument, to_be_executed)
            bytecode_method = getattr(self, instruction)
            if argument is None:
                bytecode_method()
            else:
                bytecode_method(argument)

if __name__ == "__main__":

    to_execute = {
        "instructions": [
            ("LOAD_VALUE", 0),  # the first number
            ("LOAD_VALUE", 1),  # the second number
            ("ADD_TWO_VALUES", None),
            ("PRINT_ANSWER", None),
        ],
        "numbers": [7, 5],
    }

    to_execute_2 = {
        "instructions": [("LOAD_VALUE", 0),
                         ("LOAD_VALUE", 1),
                         ("ADD_TWO_VALUES", None),
                         ("LOAD_VALUE", 2),
                         ("ADD_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [7, 5, 8] }


    what_to_execute = {
        "instructions": [("LOAD_VALUE", 0),
                         ("STORE_NAME", 0),
                         ("LOAD_VALUE", 1),
                         ("STORE_NAME", 1),
                         ("LOAD_NAME", 0),
                         ("LOAD_NAME", 1),
                         ("ADD_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [12, 10],
        "names":   ["a", "b"] }

    interpreter = Interpreter()
    interpreter.run_code(what_to_execute)
