# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

* It showed the homepage for the game glitch game.
* There was a short description with instructions and number pf attempts left.
* There was also a developer debug infor which shows the secret number, score, number of attempts, current score and the history of inputs.
* At first the input section for guessing was not loading up.

- List at least two concrete bugs you noticed at the start

* The hints were backwards and not helpful most times in getting the secret number. For example when the secret number is greater than what was guessed, the hints could say go lower and vice versa which is misleading.
* The new game was not resetting the history and did not allow for new hunts or new submissions.
* The range for the medium difficulty was larger than that of the hard difficulty which most likely should not be.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Copilot in VS Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The AI was able to correctly fix the current score updates as some cases when attempts were even the score was still increased even when the guess was incorrect and I was able to verify that the score increases when the guess was correct and is not when the guess was incorrect

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  The first refactor for the `check_guess()` function worked for most test cases but did not work when the guess is an integer and the secreet a string as it returned an inappropraite response as per the logic, I verified this using a roboust test suite covering a lot of test cases.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I decided a bug was fixed after reviewing and testing myself and then asking the agent to provide a roboust test suite that covers as many test cases and made sure all the test cases are passed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  An example is `test_bug_fix_too_low_shows_higher_hint()` it tests the `chech_guess()` function in <a>ai110-module1show-gameglitchinvestigator-starter/logic_utils.py</a> to make sure that when an integer guess is made and is lower than the secret number the code returns an appropraite result/hint that tells the player the guess is 'Too Low' and should 'Go Higher'.
- Did AI help you design or understand any tests? How?
  I promted the Agent to provide multiple test cases testing various normal as well as edge cases to be ran with pytest.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
