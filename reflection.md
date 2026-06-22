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

  When I input 100 and keep attempting the hint flips back and forth

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input     | Expected Behavior   | Actual Behavior                            | Console Output / Error |
| --------- | ------------------- | ------------------------------------------ | ---------------------- |
| number 12 | Higher hint         | Lower hint                                 |                        |
| new game  | restart the game    | restarts game but cannot input any numbers |                        |
| none      | displays attempts 8 | displays attempts 7                        |                        |
| 100       | displays lower or winner | flips hint between higher and lower   |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  I used claude at first since its built in but Its answers were almost never correct. I switched to chatGPT on my browser.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

It fixed the higher lower error by changing the text. I tested the changes and now the hint works correctly.

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I asked ai to add an import and it wanted to delete the entire file i was importing to.

GPT found the fix to the numbers being converted to strings

"The bug is in this section:

if st.session_state.attempts % 2 == 0:
    secret = str(st.session_state.secret)
else:
    secret = st.session_state.secret

On every even-numbered attempt, you're converting secret to a string." 

"Fix

Remove the conversion entirely:

secret = st.session_state.secret"


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I tested it more rigourously. Making sure I couldnt reproduce it and it didnt break anything else

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  Fixing the string conversion of the even guesses. I tested it by checking the hint was correct with different
  types of integers, even, odd, min, max etc. It showed me there was stuff I didnt see that the AI caught 

- Did AI help you design or understand any tests? How?
  Ai helped me create some pytests and learn how to at least run them.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Its like a framework that creates a quick temporary website so you dont have to use html. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  This was the first time i reverted branches in git. Also I learned how to use claude and that I prefer GPT. Claude hardly got any prompts correct.

- What is one thing you would do differently next time you work with AI on a coding task?
  Learn how to change the model type on claude.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  I have used it for a little bit but I understand how AI is replacing the implementation part. Leaving humands the design
  part. AI is a good tool but thats all it is, A tool. You need to know how to use it and how to prompt it.

  Ok why did it say to make multiple commits at the end of the Project description...
