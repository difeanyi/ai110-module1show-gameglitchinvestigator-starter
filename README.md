# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

**Purpose:** Glitchy Guesser is a Streamlit number-guessing game. Pick a difficulty, and the app picks a secret number in that range; you guess repeatedly, get a "too high"/"too low" hint after each try, and win by landing on the exact number before you run out of attempts.

**Bugs found:**
1. The "too high"/"too low" hints were swapped, telling you to go higher when you'd already guessed too high (and vice versa).
2. The secret number was cast to a string on every other attempt, which made the hint comparison fall back to lexicographic string comparison (e.g. `"9" > "10"`) instead of numeric comparison, giving the wrong hint direction and making it feel like a correct guess was never recognized.
3. `app.py` had its own duplicate copies of the game logic functions, while the matching functions in `logic_utils.py` were unimplemented and unused, so the game logic wasn't unit tested at all.
4. Three of the starter tests compared `check_guess`'s return value directly to a plain string, but `check_guess` actually returns a `(outcome, message)` tuple, so those tests were failing even though the logic they were meant to check was correct.
5. The "New Game 🔁" button calls `st.ren()`, which doesn't exist on the Streamlit API (should be `st.rerun()`) — clicking it currently crashes the app. *(Not yet fixed.)*

**Fixes applied:**
- Moved the real game logic into `logic_utils.py` and had `app.py` import it, so the logic is unit tested instead of duplicated.
- Corrected the hint messages in `check_guess` so "Too High" tells you to go lower and "Too Low" tells you to go higher.
- Removed the string-casting of the secret in `app.py` so guesses are always compared as integers.
- Fixed the three broken tests to unpack the `(outcome, message)` tuple instead of comparing it to a bare string.
- Added regression tests covering both hint directions so the swapped-hint bug can't silently come back.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Install dependencies and launch the app: `python -m streamlit run app.py`. It opens in your browser at `localhost:8501`.
2. In the sidebar, pick a difficulty (Easy, Normal, or Hard). The range and number of attempts allowed update to match.
3. Expand "Developer Debug Info" to reveal the secret number, your attempt count, and score as you play.
4. Type a guess into "Enter your guess" and click "Submit Guess 🚀".
5. Read the hint: "Go LOWER" appears when your guess is above the secret, and "Go HIGHER" appears when it's below.
6. Keep guessing and following the hint direction until you land on the exact secret number.
7. On a correct guess, the app shows balloons, a "You won!" message with your final score, and stops accepting further guesses.
8. Click "New Game 🔁" to reset with a fresh secret number and play again.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
collected 10 items                                                                  

tests/test_game_logic.py::test_winning_guess PASSED                           [ 10%]
tests/test_game_logic.py::test_guess_too_high PASSED                          [ 20%]
tests/test_game_logic.py::test_guess_too_low PASSED                           [ 30%]
tests/test_game_logic.py::test_too_high_hint_tells_player_to_go_lower PASSED  [ 40%]
tests/test_game_logic.py::test_too_low_hint_tells_player_to_go_higher PASSED  [ 50%]
tests/test_game_logic.py::test_decimal_guess_is_truncated_not_rounded PASSED  [ 60%]
tests/test_game_logic.py::test_decimal_guess_truncation_can_give_misleading_hint PASSED [ 70%]
tests/test_game_logic.py::test_negative_guess_is_accepted_and_treated_as_too_low PASSED [ 80%]
tests/test_game_logic.py::test_extremely_large_integer_guess_does_not_crash PASSED [90%]
tests/test_game_logic.py::test_extremely_large_decimal_guess_degrades_gracefully PASSED [100%]
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
