# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**


I asked the Ai tool to make 3 new test cases for any isues the game might face in testing
**What did the agent do?**
The AI agent came up with 3 new test cases that could end up breaking the game, after reading and verifying these test cases i executed the testing


**What did you have to verify or fix manually?**
I only had to verify if these "issues" were actaully something that could cause problems with the game and they actually did


---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Decimal guesses (e.g. "50.9") | "identify three potential 'edge case' inputs (e.g., negative numbers, decimals, or extremely large values) that might still break my game" then "lets generate a suite of pytest cases that verifies these test case inputs" | `test_decimal_guess_is_truncated_not_rounded` and `test_decimal_guess_truncation_can_give_misleading_hint` — asserts `parse_guess("50.9")` truncates to `50` instead of rounding, and that this can produce a misleading "Go HIGHER!" hint when the secret is `51` | Yes | `parse_guess` uses `int(float(raw))`, which truncates toward zero rather than rounding. The test confirmed this is real behavior, not a hypothetical, so I know it's a design choice worth revisiting later rather than a bug I imagined. |
| Negative numbers (e.g. "-5") | Same prompts as above | `test_negative_guess_is_accepted_and_treated_as_too_low` — asserts `parse_guess("-5")` succeeds and `check_guess(-5, secret)` always returns "Too Low" | Yes | There's no bounds check against the difficulty range before comparing, so negative guesses are silently accepted. It doesn't crash, but it confirmed the game will never reject an obviously out-of-range guess. |
| Extremely large values (huge int and huge decimal) | Same prompts as above | `test_extremely_large_integer_guess_does_not_crash` and `test_extremely_large_decimal_guess_degrades_gracefully` — asserts a 300-digit integer guess compares fine, and a 400-digit decimal guess (which overflows `float()` to `inf`) is caught and reported as "That is not a number." | Yes | Python's arbitrary-precision ints handle huge plain integers with no issue. Huge decimals overflow `float()` and raise `OverflowError`, which `parse_guess`'s blanket `except Exception` catches — so both cases degrade gracefully instead of crashing the app. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
identify three potential "edge case" inputs (e.g., negative numbers, decimals, or extremely large values) that might still break my game.
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
