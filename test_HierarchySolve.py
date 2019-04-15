import unittest
from io import StringIO
from HierarchySolve import Hierarchy, Employee


class TestStringMethods(unittest.TestCase):

    def test_parse_employee(self):
        h = Hierarchy("employee_test.txt")
        h.parse_employee("003303\tTanya\tPekarin\t000592")
        self.assertEqual(h.employee_hash["000592"], [Employee(
            "003303", "Tanya", "Pekarin", "000592")])

    def test_parse_boss(self):
        h = Hierarchy("employee_test.txt")
        h.parse_employee("000117\tRobert\tBigBoss")
        self.assertEqual(h.employee_hash, {})

    def test_parse_hierarchy(self):
        h = Hierarchy("employee_test.txt")
        h.process_hierarchy()
        self.assertEqual(h.root, Employee("1", "Robert", "BigBoss", None))
        self.assertEqual(h.employee_hash["1"],
                         [Employee("2", "Helen", "Shay", "1"), Employee("4", "Vidyasagar", "Roddick", "1")])
        self.assertEqual(h.employee_hash["2"], [Employee(
            "3", "Kathy", "Wellington", "2")])

    def test_print_hierarchy(self):
        h = Hierarchy("employee_test.txt")
        out = StringIO()
        h.print_hierarchy(out)
        hier = ["0 - [1] Robert BigBoss - Reports To []",
                "    1 - [4] Vidyasagar Roddick - Reports To [1]",
                "    1 - [2] Helen Shay - Reports To [1]",
                "        2 - [3] Kathy Wellington - Reports To [2]",
                ""
                ]

        expected = "\n".join(hier)
        self.assertEqual(out.getvalue(), expected)
        out.close()


if __name__ == "__main__":
    unittest.main()
