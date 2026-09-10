from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    # check_guess returns (outcome, message), not just the outcome string
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_hint_tells_player_to_go_lower():
    # Regression test: the hint text was previously swapped, telling the
    # player to go HIGHER when their guess was already too high.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()

def test_too_low_hint_tells_player_to_go_higher():
    # Regression test: the hint text was previously swapped, telling the
    # player to go LOWER when their guess was already too low.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()
    assert "LOWER" not in message.upper()


# --- Edge case inputs: decimals, negative numbers, extremely large values ---

def test_decimal_guess_is_truncated_not_rounded():
    # parse_guess uses int(float(raw)), which truncates toward zero instead
    # of rounding. "50.9" becomes 50, not 51 -- documenting this behavior so
    # it's a deliberate choice rather than a silent surprise.
    ok, guess_int, err = parse_guess("50.9")
    assert ok is True
    assert guess_int == 50
    assert err is None

def test_decimal_guess_truncation_can_give_misleading_hint():
    # Because "50.9" truncates to 50, a player who types the closest
    # possible decimal to a secret of 51 still gets told to go higher.
    ok, guess_int, _ = parse_guess("50.9")
    assert ok is True
    outcome, message = check_guess(guess_int, 51)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()

def test_negative_guess_is_accepted_and_treated_as_too_low():
    # Negative numbers parse successfully (no bounds check against the
    # difficulty range), and since the secret is always >= 1, a negative
    # guess should always come back "Too Low" rather than erroring.
    ok, guess_int, err = parse_guess("-5")
    assert ok is True
    assert guess_int == -5
    assert err is None

    outcome, message = check_guess(guess_int, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()

def test_extremely_large_integer_guess_does_not_crash():
    # Plain large integers are fine thanks to Python's arbitrary-precision
    # ints -- this should parse and compare without raising.
    huge = "9" * 300
    ok, guess_int, err = parse_guess(huge)
    assert ok is True
    assert guess_int == int(huge)
    assert err is None

    outcome, _ = check_guess(guess_int, 50)
    assert outcome == "Too High"

def test_extremely_large_decimal_guess_degrades_gracefully():
    # A huge decimal (more digits than a float can represent) overflows to
    # inf when parsed with float(), and int(float('inf')) raises
    # OverflowError. parse_guess's blanket except should catch this and
    # report it as an invalid guess instead of crashing the app.
    huge_decimal = ("9" * 400) + ".5"
    ok, guess_int, err = parse_guess(huge_decimal)
    assert ok is False
    assert guess_int is None
    assert err == "That is not a number."
