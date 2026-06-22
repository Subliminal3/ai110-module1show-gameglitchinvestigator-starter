import pytest
from app import check_guess


@pytest.mark.parametrize(
    "guess,secret,expected_outcome,expected_message",
    [
        (50, 50, "Win", "🎉 Correct!"),
        (75, 50, "Too High", "📉 Go LOWER!"),
        (25, 50, "Too Low", "📈 Go HIGHER!"),
        (0, 50, "Too Low", "📈 Go HIGHER!"),
        (-10, 50, "Too Low", "📈 Go HIGHER!"),
        (1000, 50, "Too High", "📉 Go LOWER!"),
        (100, 99, "Too High", "📉 Go LOWER!"),
        (99, 100, "Too Low", "📈 Go HIGHER!"),
    ],
)
def test_check_guess(guess, secret, expected_outcome, expected_message):
    outcome, message = check_guess(guess, secret)

    assert outcome == expected_outcome
    assert message == expected_message