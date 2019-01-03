'''
The primary unit test file for guess my number
'''

import time
import unittest
import unittest.mock
from src.GuessMyNumber import GuessMyNumber as gmn
import io
import sys

SLOW_TEST_THRESHOLD = 0.1

class TestGetRandomNumber(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        if elapsed > SLOW_TEST_THRESHOLD:
            print(f'{self.id()}: {round(elapsed,2)}s')

    def test_get_random_number(self):
        game = gmn()
        num = game.get_random_number()
        self.assertIsInstance(num, int)
        self.assertGreater(num, 0)
        self.assertLess(num, 51)

class TestPrintPastGuesses(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        if elapsed > SLOW_TEST_THRESHOLD:
            print(f'{self.id()}: {round(elapsed,2)}s')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_past_guesses_empty(self, mock_stdout):
        game = gmn()
        past_guesses = []
        past_notes = dict({})
        game.print_past_guesses(past_guesses, past_notes)
        self.assertEqual(len(mock_stdout.getvalue()), 0)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_past_guesses_full(self, mock_stdout):
        game = gmn()
        past_guesses = [1,2,3]
        past_notes = dict({1:'one', 2:'two', 3:'three'})
        game.print_past_guesses(past_guesses, past_notes)
        expected = 'Past guesses: \n1: one\n2: two\n3: three'
        self.assertEqual(mock_stdout.getvalue(), expected)

class TestCheckGuess(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        if elapsed > SLOW_TEST_THRESHOLD:
            print(f'{self.id()}: {round(elapsed,2)}s')

    def test_check_guess_invalid(self):
        game = gmn()
        current_guess = 'invalid'
        correct_answer = 0
        last_guess = -1
        result = game.check_guess(current_guess, correct_answer, last_guess)
        self.assertFalse(result)

    def test_check_guess_quit(self):
        game = gmn()
        current_guess = 'Q'
        correct_answer = 0
        last_guess = -1
        result = game.check_guess(current_guess, correct_answer, last_guess)
        self.assertTrue(result)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_guess_equal(self, mock_stdout):
        game = gmn()
        current_guess = 25
        correct_answer = 25
        last_guess = -1
        result = game.check_guess(current_guess, correct_answer, last_guess)
        expected_output = "That is correct."
        self.assertTrue(result)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_guess_far_away_first(self, mock_stdout):
        game = gmn()
        current_guess = 1
        correct_answer = 37
        last_guess = -1
        result = game.check_guess(current_guess, correct_answer, last_guess)
        expected_output = "You're freezing. Try again"
        self.assertIsNone(result)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_guess_far_away_second_colder(self, mock_stdout):
        game = gmn()
        current_guess = 1
        correct_answer = 40
        last_guess = 5
        result = game.check_guess(current_guess, correct_answer, last_guess)
        expected_output = "Getting cooler, try again."
        self.assertIsNone(result)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_guess_far_away_second_warmer(self, mock_stdout):
        game = gmn()
        current_guess = 5
        correct_answer = 40
        last_guess = 1
        result = game.check_guess(current_guess, correct_answer, last_guess)
        expected_output = "Getting warmer! Try again"
        self.assertIsNone(result)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_guess_close_first(self, mock_stdout):
        game = gmn()
        current_guess = 36
        correct_answer = 37
        last_guess = -1
        result = game.check_guess(current_guess, correct_answer, last_guess)
        expected_output = "You're hot. Try again."
        self.assertIsNone(result)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_guess_close_second(self, mock_stdout):
        game = gmn()
        current_guess = 36
        correct_answer = 37
        last_guess = 1
        result = game.check_guess(current_guess, correct_answer, last_guess)
        expected_output = "You're hot. Try again."
        self.assertIsNone(result)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_guess_closer_second(self, mock_stdout):
        game = gmn()
        current_guess = 5
        correct_answer = 11
        last_guess = 1
        result = game.check_guess(current_guess, correct_answer, last_guess)
        expected_output = "Getting warmer! Try again"
        self.assertIsNone(result)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_guess_further_second(self, mock_stdout):
        game = gmn()
        current_guess = 1
        correct_answer = 11
        last_guess = 5
        result = game.check_guess(current_guess, correct_answer, last_guess)
        expected_output = "Getting cooler, try again."
        self.assertIsNone(result)
        self.assertEqual(expected_output, mock_stdout.getvalue())