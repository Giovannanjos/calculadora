
import unittest

from calculator.history import add_entry, format_history


class TestHistory(unittest.TestCase):

    def test_add_entry(self):
        history = []

        add_entry(history, "+", 10, 5, 15)

        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["result"], 15)
        self.assertEqual(history[0]["operation"], "+")

    def test_format_empty_history(self):
        self.assertEqual(
            format_history([]),
            "Nenhum cálculo realizado ainda."
        )

    def test_format_history(self):
        history = []
        add_entry(history, "+", 10, 5, 15)

        result = format_history(history)

        self.assertIn("10 + 5 = 15", result)


if __name__ == "__main__":
    unittest.main()
