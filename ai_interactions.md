# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

I tried Claude for the first time and was disappointed. I eventually switched back to the browser version of GPT which worked good.


**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

Claude - "When I enter 100 as the guess it flips the hint between higehr and lower even though it  should usually be lower"

GPT - "I have a file that is a simple number checker Just tell me the bugs i ask about and how to fix them The first one is 100 flips the higher lower hint back and forth when it should be going lower" Then i gave it both files

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

It reverted a change it made earlier that was correct. 

Claude - 
"Got it. Issue: the logic in check_guess after TypeError catch is still wrong. When g > secret (string comparison), you return "Too High" but the emoji says "Go HIGHER" — should be "Go LOWER".

String comparison "100" > "50" is False (lexicographic: "1" < "5"), so it hits the last return with wrong emoji direction.

Fix: in the TypeError block, swap the emoji directions back."


GPT- "The bug is in this section:

if st.session_state.attempts % 2 == 0:
    secret = str(st.session_state.secret)
else:
    secret = st.session_state.secret

On every even-numbered attempt, you're converting secret to a string." 

"Fix

Remove the conversion entirely:

secret = st.session_state.secret"

That was correct



**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

I had to reject the suggestion from Claude since it didnt give me the correct output.

GPT gave me the correct fix

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
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
