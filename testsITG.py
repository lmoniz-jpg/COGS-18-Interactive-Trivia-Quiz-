"""Unit tests to test functionality of project."""

import unittest
import module


class TestGetQuestions(unittest.TestCase):
    """Tests for the get_questions function."""

    def test_returns_correct_number(self):
        """get_questions(n) should return exactly n questions."""
        questions = module.get_questions(3)
        self.assertEqual(len(questions), 3)

    def test_default_returns_five(self):
        """Default call should return 5 questions."""
        questions = module.get_questions()
        self.assertEqual(len(questions), 5)

    def test_questions_have_required_keys(self):
        """Every question dict must have 'question', 'choices', and 'answer'."""
        questions = module.get_questions(5)
        for q in questions:
            self.assertIn("question", q)
            self.assertIn("choices", q)
            self.assertIn("answer", q)

    def test_each_question_has_four_choices(self):
        """Each question should have exactly 4 answer choices."""
        questions = module.get_questions(5)
        for q in questions:
            self.assertEqual(len(q["choices"]), 4)

    def test_raises_value_error_for_zero(self):
        """Should raise ValueError when n=0."""
        with self.assertRaises(ValueError):
            module.get_questions(0)

    def test_raises_value_error_for_too_many(self):
        """Should raise ValueError when n exceeds question bank size."""
        with self.assertRaises(ValueError):
            module.get_questions(999)

    def test_no_shuffle_returns_same_order(self):
        """With shuffle=False, order should be consistent (first n questions)."""
        q1 = module.get_questions(3, shuffle=False)
        q2 = module.get_questions(3, shuffle=False)
        self.assertEqual(q1, q2)


class TestCheckAnswer(unittest.TestCase):
    """Tests for the check_answer function."""

    def setUp(self):
        """Set up a sample question for reuse across tests."""
        self.sample_q = {
            "question": "What color is the sky?",
            "choices": ["Red", "Blue", "Green", "Yellow"],
            "answer": 1,  # "Blue" is correct
        }

    def test_correct_answer_returns_true(self):
        """Correct answer index should return True."""
        self.assertTrue(module.check_answer(self.sample_q, 1))

    def test_wrong_answer_returns_false(self):
        """Any wrong answer index should return False."""
        self.assertFalse(module.check_answer(self.sample_q, 0))
        self.assertFalse(module.check_answer(self.sample_q, 2))
        self.assertFalse(module.check_answer(self.sample_q, 3))

    def test_returns_bool_type(self):
        """Return value should be a bool."""
        result = module.check_answer(self.sample_q, 1)
        self.assertIsInstance(result, bool)


class TestCalculateScore(unittest.TestCase):
    """Tests for the calculate_score function."""

    def test_all_correct(self):
        """All True results should give 100% and correct == total."""
        score = module.calculate_score([True, True, True])
        self.assertEqual(score["correct"], 3)
        self.assertEqual(score["total"], 3)
        self.assertEqual(score["percentage"], 100.0)

    def test_all_incorrect(self):
        """All False results should give 0%."""
        score = module.calculate_score([False, False, False])
        self.assertEqual(score["correct"], 0)
        self.assertEqual(score["percentage"], 0.0)

    def test_mixed_results(self):
        """Mixed results should calculate the right percentage."""
        score = module.calculate_score([True, False, True, True])
        self.assertEqual(score["correct"], 3)
        self.assertEqual(score["total"], 4)
        self.assertAlmostEqual(score["percentage"], 75.0)

    def test_single_correct(self):
        """Single correct answer should give 100%."""
        score = module.calculate_score([True])
        self.assertEqual(score["percentage"], 100.0)

    def test_raises_on_empty_list(self):
        """Should raise ValueError for an empty list."""
        with self.assertRaises(ValueError):
            module.calculate_score([])

    def test_returns_dict_with_correct_keys(self):
        """Result should be a dict with 'correct', 'total', 'percentage'."""
        score = module.calculate_score([True, False])
        self.assertIn("correct", score)
        self.assertIn("total", score)
        self.assertIn("percentage", score)


class TestGetGrade(unittest.TestCase):
    """Tests for the get_grade function."""

    def test_a_grade(self):
        """90 and above should return 'A'."""
        self.assertEqual(module.get_grade(100.0), "A")
        self.assertEqual(module.get_grade(90.0), "A")
        self.assertEqual(module.get_grade(95.5), "A")

    def test_b_grade(self):
        """80-89.9 should return 'B'."""
        self.assertEqual(module.get_grade(80.0), "B")
        self.assertEqual(module.get_grade(85.0), "B")
        self.assertEqual(module.get_grade(89.9), "B")

    def test_c_grade(self):
        """70-79.9 should return 'C'."""
        self.assertEqual(module.get_grade(70.0), "C")
        self.assertEqual(module.get_grade(75.0), "C")

    def test_d_grade(self):
        """60-69.9 should return 'D'."""
        self.assertEqual(module.get_grade(60.0), "D")
        self.assertEqual(module.get_grade(65.0), "D")

    def test_f_grade(self):
        """Below 60 should return 'F'."""
        self.assertEqual(module.get_grade(59.9), "F")
        self.assertEqual(module.get_grade(0.0), "F")
        self.assertEqual(module.get_grade(50.0), "F")

    def test_raises_on_invalid_percentage(self):
        """Should raise ValueError for percentages outside [0, 100]."""
        with self.assertRaises(ValueError):
            module.get_grade(-1.0)
        with self.assertRaises(ValueError):
            module.get_grade(101.0)


if __name__ == "__main__":
    unittest.main()
