import re
import math
import sys

class RevilangInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.classes = {}

    def parse(self, line):
        line = line.strip()
        
        # Comment removal
        line = re.sub(r'#-.*$', '', line)  # One line comment
        line = re.sub(r'#.*#', '', line)  # Multi-line comment
        
        if not line:  # Skip empty lines
            return

        # Variable declaration
        if line.startswith("var +"):
            self.declare_variable(line)
        # Variable assignment
        elif "=" in line:
            self.assign_variable(line)
        # Event input
        elif line.startswith("event.input("):
            self.handle_event_input(line)
        # Event console output
        elif line.startswith("event.console-output("):
            self.handle_event_output(line)
        # Function definition
        elif line.startswith("function."):
            self.define_function(line)
        # Class definition
        elif line.startswith("property."):
            self.define_class(line)
        # Math operations
        elif line.startswith("math."):
            self.handle_math_operations(line)
        # Loop structures
        elif line.startswith("loop.for") or line.startswith("loop.as-much"):
            self.handle_loops(line)
        # Conditionals
        elif line.startswith("if ") or line.startswith("elif ") or line.startswith("else "):
            self.handle_conditions(line)

    def declare_variable(self, line):
        match = re.match(r"var \+(\w+) = (.+)", line)
        if match:
            var_name, value = match.groups()
            self.variables[var_name] = self.evaluate_value(value)
            print(f"Declared variable {var_name} = {self.variables[var_name]}")

    def assign_variable(self, line):
        match = re.match(r"(\w+) = (.+)", line)
        if match:
            var_name, value = match.groups()
            if var_name in self.variables:
                self.variables[var_name] = self.evaluate_value(value)
                print(f"Assigned {var_name} = {self.variables[var_name]}")
            else:
                print(f"Error: Variable {var_name} not declared.")

    def handle_event_input(self, line):
        # Parsing input type (number or string)
        match = re.match(r'event\.input\((str|number)\("(.+)"\)\)', line)
        if match:
            input_type, prompt = match.groups()
            user_input = input(prompt + " ")  # Display the prompt and take input
            if input_type == "number":
                try:
                    user_input = int(user_input)  # Convert to number if it's supposed to be a number
                except ValueError:
                    print("Error: Invalid number input.")
            return user_input  # Return the input value

    def handle_event_output(self, line):
        match = re.match(r"event.console-output\((.+)\)", line)
        if match:
            output = match.group(1)
            evaluated_output = self.evaluate_value(output)
            print(evaluated_output)

    def define_function(self, line):
        match = re.match(r"function\.(\w+)\((\w+)\) \{(.+)\}", line)
        if match:
            func_name, param_name, func_body = match.groups()
            self.functions[func_name] = (param_name, func_body.strip())
            print(f"Defined function {func_name}")

    def call_function(self, func_name, arg):
        if func_name in self.functions:
            param_name, func_body = self.functions[func_name]
            self.variables[param_name] = arg
            self.parse(func_body)

    def define_class(self, line):
        # This method will define classes
        match = re.match(r"property\.(\w+) /(\w+) \{(.+)\}", line)
        if match:
            class_type, class_name, class_body = match.groups()
            if class_type == "all":
                self.classes[class_name] = class_body.strip()
                self.parse(class_body.strip())
            else:
                print("Unsupported class property type.")

    def handle_math_operations(self, line):
        # Add support for math operations
        match = re.match(r"var \+(\w+) = math\.(\w+)\((.+)\)", line)
        if match:
            var_name, operation, value = match.groups()
            if operation == "sin":
                self.variables[var_name] = math.sin(float(value))
                print(f"Calculated {var_name} = {self.variables[var_name]}")

    def handle_loops(self, line):
        # Simple loop handling (for demonstration)
        if line.startswith("loop.for"):
            # For loop example
            match = re.match(r"loop\.for \(var \+(\w+) \+ (\d+)\((\w+)\s*<=\s*(\d+)\)\) \{(.+)\}", line)
            if match:
                var_name, start, condition_var, limit, loop_body = match.groups()
                start = int(start)
                limit = int(limit)
                for i in range(start, limit + 1):
                    self.variables[var_name] = i
                    self.parse(loop_body.strip())
        
        elif line.startswith("loop.as-much"):
            # While loop example
            match = re.match(r"loop\.as-much \((\w+)\) \{(.+)\}", line)
            if match:
                condition, loop_body = match.groups()
                while self.evaluate_value(condition):
                    self.parse(loop_body.strip())

    def handle_conditions(self, line):
        # Simple condition handling (if, elif, else)
        if line.startswith("if "):
            match = re.match(r"if \/(.+) \{(.+)\}", line)
            if match:
                condition, body = match.groups()
                if self.evaluate_value(condition):
                    self.parse(body.strip())
        elif line.startswith("elif "):
            match = re.match(r"elif \/(.+) \{(.+)\}", line)
            if match:
                condition, body = match.groups()
                if self.evaluate_value(condition):
                    self.parse(body.strip())
        elif line.startswith("else "):
            match = re.match(r"else \/(.+) \{(.+)\}", line)
            if match:
                body = match.groups()[1]
                self.parse(body.strip())

    def evaluate_value(self, value):
        # Evaluate the value for variables, numbers, booleans, and strings
        value = value.strip()
        if value.isdigit():
            return int(value)
        elif value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        elif value.startswith("\"") and value.endswith("\""):
            return value[1:-1]
        elif value in self.variables:
            return self.variables[value]
        return value

    def run(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                self.parse(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 interpreter.py <filename.rl>")
        sys.exit(1)

    filename = sys.argv[1]
    interpreter = RevilangInterpreter()
    interpreter.run(filename)
        
