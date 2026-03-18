import sys
from pathlib import Path
import pytest

# Add parent directory to path so we can import logic_utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from logic_utils import check_guess, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

# ===== Tests specifically for the fixed bug (hint messages) =====

def test_bug_fix_too_high_shows_lower_hint():
    """Bug fix: When guess is too high, should show 'Go LOWER!' not 'Go HIGHER!'"""
    outcome, message = check_guess(100, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_bug_fix_too_low_shows_higher_hint():
    """Bug fix: When guess is too low, should show 'Go HIGHER!' not 'Go LOWER!'"""
    outcome, message = check_guess(10, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message

# ===== Edge cases and boundary tests =====

def test_guess_one_above_secret():
    """Test when guess is just slightly above secret"""
    outcome, message = check_guess(51, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_one_below_secret():
    """Test when guess is just slightly below secret"""
    outcome, message = check_guess(49, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_large_numbers():
    """Test with large numbers"""
    outcome, message = check_guess(1000, 100)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_negative_numbers():
    """Test with negative numbers"""
    outcome, message = check_guess(-5, -10)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_zero():
    """Test with zero"""
    outcome, message = check_guess(0, 0)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_string_secret_winning_guess():
    """Test type error handling: string secret with correct guess"""
    outcome, message = check_guess("50", "50")
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_string_secret_too_high():
    """Test type error handling: string secret, guess too high (string comparison)"""
    outcome, message = check_guess("60", "50")
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_string_secret_too_low():
    """Test type error handling: string secret, guess too low (string comparison)"""
    outcome, message = check_guess("40", "50")
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_mixed_type_guess_too_high():
    """Test when guess is int but secret is string, and guess is too high"""
    outcome, message = check_guess(100, "50")
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_mixed_type_guess_too_low():
    """Test when guess is int but secret is string, and guess is too low"""
    outcome, message = check_guess(10, "50")
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


# ===== parse_guess tests =====

@pytest.mark.parametrize(
    "raw, expected",
    [
        (None, (False, None, "Enter a guess.")),
        ("", (False, None, "Enter a guess.")),
        ("   ", (False, None, "Enter a guess.")),
        ("42", (True, 42, None)),
        ("  42  ", (True, 42, None)),
        ("-7", (True, -7, None)),
        ("0", (True, 0, None)),
        ("12.9", (False, None, "That is not a number.")),
        ("abc", (False, None, "That is not a number.")),
        ("1e3", (False, None, "That is not a number.")),
    ],
)
def test_parse_guess_cases(raw, expected):
    assert parse_guess(raw) == expected


def test_parse_guess_non_string_input_is_supported_via_str_cast():
    ok, value, err = parse_guess(15)
    assert ok is True
    assert value == 15
    assert err is None


# ===== update_score tests =====

def test_update_score_win_early_attempt_awards_high_points():
    # points = 100 - 10 * (attempt_number + 1)
    # attempt 1 => +80
    assert update_score(0, "Win", 1) == 80


def test_update_score_win_has_minimum_points_floor():
    # Large attempt count should floor to +10
    assert update_score(5, "Win", 50) == 15


@pytest.mark.parametrize("attempt_number", [1, 2, 3, 10])
def test_update_score_too_high_is_always_penalized(attempt_number):
    # Regression: ensure no even-attempt bonus is applied
    assert update_score(20, "Too High", attempt_number) == 15


@pytest.mark.parametrize("attempt_number", [1, 2, 3, 10])
def test_update_score_too_low_is_always_penalized(attempt_number):
    assert update_score(20, "Too Low", attempt_number) == 15


def test_update_score_unknown_outcome_no_change():
    assert update_score(33, "Unknown", 2) == 33
