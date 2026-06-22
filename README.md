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

- [ ] Describe the game's purpose.
  The purpose of the game is to guess the correct number in a limited number of guesses
- [ ] Detail which bugs you found.
  I found a bug where the hint was backwards, The even numbers were being stores as strings, and the new game button didnt work

- [ ] Explain what fixes you applied.
  I used AI to find the bug and suggest a fix. i looked over the fix and determined if it seemed acceptable. I used Ai
  to switch the hint given and store all the numbers as integers not strings.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The user enters 50
2. The game returns too low go higher
3. The user enters 75
4. The game returns too high go lower
5. The user enters 65
6. The game returns Correct!
7. The game ends after correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
PS C:\Users\gamea\GitHub\ai110-module1show-gameglitchinvestigator-starter> python -m pytest test/test_game_logic.py
================================================================================================================================================ test session starts ================================================================================================================================
platform win32 -- Python 3.12.6, pytest-9.1.0, pluggy-1.6.0
rootdir: C:\Users\gamea\GitHub\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 8 items                                                                                                                                                                                                                                                                                                     

test\test_game_logic.py ........                                                                                                                                                                                                                                                                                [100%]

================================================================================================================================================= 8 passed in 2.45s ================================================================================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
