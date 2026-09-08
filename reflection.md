# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
-When you make a guess, the hint says go higher when the right number is supposed to be lower
- When u guess 100, the hint says go higher
-When you guess the correct number, the game doesnt stop so you cant even win
- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 60 | Hint says "Go lower" (guess was above the secret) | Hint says "Go higher" | No error thrown, but the guess is actually lower than 60, so the hint direction is wrong |
| 59 (correct guess) | Game shows "That's correct!" and ends | Hint still says "Go higher" and the game keeps going | No error thrown, but a correct guess should stop the game, not prompt another guess |
| 100 | Hint says "Go lower" (or "Can't go any higher than that!") since 100 is the max | Hint says "Go higher" | No error thrown, but the guess can't go any higher than 100, so the hint direction is wrong |

---

## 2. How did you use AI as a teammate?

-I used Claude code for help with this section. I first went through and noticed what was wrong with the app first , then i asked claude the best ways ti fix the errors.
- Claude recommneded the check_guess function to be flipped so the correct numbers give hints for higher and lower.
- Claude did say that the st.rerun should be replaced with a different helper function, but after looking into it, the change was not needed.
- I then re ran the app with the changes made and the app ran well with the bugs being fixed

---

## 3. Debugging and testing your fixes

-  -I decided a bug was fixed when I would save my recent changes and run the app again. If the changes were present, the fix worked
  - One test we ran was using pytest. The test was just to check if the higher/lower logic was working correcetly 
  
- Did AI help you design or understand any tests? How? - Claude AI helped me design the pytest and I was able to understand the test on my own. The test was made by asking Claude to look through my recent changes in app.py and create a py.test with the new logic

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
