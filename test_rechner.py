import unittest

from rechner import formatiere, rechne


class RechnerTest(unittest.TestCase):
    def test_addieren(self):
        self.assertEqual(rechne(2, 3, "add"), 5)

    def test_subtrahieren(self):
        self.assertEqual(rechne(10, 4, "sub"), 6)

    def test_multiplizieren(self):
        self.assertEqual(rechne(6, 7, "mul"), 42)

    def test_dividieren(self):
        self.assertEqual(rechne(10, 4, "div"), 2.5)

    def test_division_durch_null(self):
        with self.assertRaises(ValueError):
            rechne(1, 0, "div")

    def test_unbekannte_operation(self):
        with self.assertRaises(ValueError):
            rechne(1, 2, "wurzel")

    def test_formatiere_ganze_zahl(self):
        self.assertEqual(formatiere(42.0), 42)
        self.assertEqual(formatiere(2.5), 2.5)


if __name__ == "__main__":
    unittest.main()
