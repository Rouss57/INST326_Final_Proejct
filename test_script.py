import pytest
from io import StringIO
from unittest.mock import patch
from Final_project import MultipleChoiceQuestion, Quiz

# Helper function to simulate user input
def simulate_user_input(inputs):
    return lambda _: inputs.pop(0)

def test_invalid_user_input():
    # Create a mock question
    question = MultipleChoiceQuestion("Test Question", {'A': "Agree", 'N': "Neutral", 'D': "Disagree"})

    # Simulate user input: first invalid, then valid
    user_inputs = ['InvalidChoice', 'A']
    
    # Patching input() with mock input
    with patch('builtins.input', simulate_user_input(user_inputs)):
        # Create a quiz with the mock question
        quiz = Quiz([question])

        # Simulate taking the quiz
        quiz.take_quiz()

        # Assert that the response was added
        assert quiz.responses == ['A']

# Run the tests
if __name__ == '__main__':
    pytest.main()
