import unittest

import solver

# Defining constants
VALID_EQUATIONS = [
    ("-3+4/2", -1),
    ("-3*4/2", -6),
    ("-10+10", 0),
    ("10-1-9", 0),
    ("40/4/2", 5),
    ("1+2+30", 33),
    ("3+21/3", 10),
    ("40/4+2", 12),
    ("16+4*2", 24),
    ("2/1*40", 80),
]

INVALID_EQUATIONS = [
    ("1+2/30", None),
    ("2/3*10", None),
]


# Main tests class
class TestSolver(unittest.TestCase):
    def test_valid_equations(self):
        """Test valid equations against their solutions"""

        for equation, solution in VALID_EQUATIONS:
            self.assertEqual(solver.solve(equation), solution)

    def test_invalid_equations(self):
        """Test invalid equations against None"""

        for equation, solution in INVALID_EQUATIONS:
            self.assertEqual(solver.solve(equation), solution)


if __name__ == "__main__":
    unittest.main()
