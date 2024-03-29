import unittest


class CombinationLock:
    Code = "12345"

    def __init__(self, combination):
        self.status = "LOCKED"
        self.reset = True

    def reset(self):
        self.status = "LOCKED"
        self.reset = True

    def enter_digit(self, digit):
        if self.reset:
            self.status = ""
            self.reset = False
        self.status += str(digit)
        if not CombinationLock.Code.startswith(self.status):
            self.status = "ERROR"
        elif self.status == CombinationLock.Code:
            self.status = "OPEN"


class FirstTestSuite(unittest.TestCase):
    def test_success(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual("LOCKED", cl.status)
        cl.enter_digit(1)
        self.assertEqual("1", cl.status)
        cl.enter_digit(2)
        self.assertEqual("12", cl.status)
        cl.enter_digit(3)
        self.assertEqual("123", cl.status)
        cl.enter_digit(4)
        self.assertEqual("1234", cl.status)
        cl.enter_digit(5)
        self.assertEqual("OPEN", cl.status)

    def test_failure(self):
        cl = CombinationLock([1, 2, 3])
        self.assertEqual("LOCKED", cl.status)
        cl.enter_digit(1)
        self.assertEqual("1", cl.status)
        cl.enter_digit(2)
        self.assertEqual("12", cl.status)
        cl.enter_digit(5)
        self.assertEqual("ERROR", cl.status)
