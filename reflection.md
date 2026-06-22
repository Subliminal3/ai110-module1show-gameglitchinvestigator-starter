# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  Everything appeared normal. I could make guesses.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  Go higher and go lower were backwards

  the new game button is broken. when i click it the attempts reset but i cannot input anymore numbers

  The attempts left is 1 less than it should be. and the answer is revealed on the second to last attempt. Indexing issue im guessing

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input     | Expected Behavior   | Actual Behavior                            | Console Output / Error |
| --------- | ------------------- | ------------------------------------------ | ---------------------- |
| number 12 | Higher hint         | Lower hint                                 |                        |
| new game  | restart the game    | restarts game but cannot input any numbers |                        |
| none      | displays attempts 8 | displays attempts 7                        |                        |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

It fixed the higher lower error by changing the text. I tested the changes and now the hint works correctly.

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).



---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
