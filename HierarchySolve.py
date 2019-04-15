from collections import namedtuple, defaultdict
from sys import stdout

Employee = namedtuple(
    "Employee", ("id", "first_name", "last_name", "manager_id"))


class Hierarchy:
    def __init__(self, path):
        self.file = path
        self.employee_hash = defaultdict(list)
        self.root = None

    def process_hierarchy(self):
        print("hello")
        with open(self.file) as f:
            for line in f:
                self.parse_employee(line)

    def parse_employee(self, line):

        parsed = line.strip().split("\t")
        # print("--------------")
        # print(line)
        # print(len(parsed))
        # print(parsed)
        if (len(parsed) == 4):
            self.employee_hash[parsed[3]].append(Employee(*parsed))
        else:
            self.root = Employee(parsed[0], parsed[1], parsed[2], None)

    def print_hierarchy(self, out=stdout):
        self.process_hierarchy()
        stack = []
        stack.append((0, self.root))

        spacers = []
        while(stack):
            [level, emp] = stack.pop()
            try:
                spacer = spacers[level]
            except IndexError:
                spacer = "".join(["    " for x in range(level)])
                spacers.append(spacer)
            manager_id = emp.manager_id if emp.manager_id is not None else ""
            output = f"{spacer}{level} - [{emp.id}] {emp.first_name} {emp.last_name} - Reports To [{manager_id}]\n"
            out.write(output)

            new_nodes = self.employee_hash.get(emp.id)
            if new_nodes:
                for emp in new_nodes:
                    stack.append((level + 1, emp))

        # print("run")
        # hierarchy = Hierarchy()
        # hierarchy.process_hierarchy()
