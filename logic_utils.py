def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    text = str(raw).strip()
    if text == "":
        return False, None, "Enter a guess."

    try:
        value = int(text)
    except ValueError:
        return False, None, "That is not a number."

    # FIX: Parse only trimmed whole-number input; removed float-to-int truncation
    # (e.g., "12.9" -> 12) and narrowed exception handling to ValueError.
    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        # Handle mixed types by attempting numeric comparison
        try:
            guess_num = float(guess) if isinstance(guess, str) else guess
            secret_num = float(secret) if isinstance(secret, str) else secret
            if guess_num == secret_num:
                return "Win", "🎉 Correct!"
            if guess_num > secret_num:
                return "Too High", "📉 Go LOWER!"
            else:
                return "Too Low", "📈 Go HIGHER!"
        except (ValueError, TypeError):
            # Fall back to string comparison
            g = str(guess)
            if g == secret:
                return "Win", "🎉 Correct!"
            if g > secret:
                return "Too High", "📉 Go LOWER!"
            return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
    # FIX: Removed the even attempt bonus for "Too High" guesses. Both incorrect
    # guesses (Too High and Too Low) should be penalized equally. The previous logic
    # incorrectly rewarded guesses on even attempts regardless of correctness.
