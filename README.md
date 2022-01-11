# wordle
This is a quick little Wordle hack in Python to play on command line, written in Python 3.9 using only modules from the standard library.

I was introduced to Wordle today (2022 Jan 09) and I immediately wanted to play it without limits, so I put this together.

This game has also been adapted to my Discord bot. You can find it here: https://crimso.bot/

## Example gameplay
```
$ python3 wordle.py
Try to guess the five-letter word!
Letter in word: 🟨 // Letter in correct spot: 🟩
To see eliminated letters, type "letters"
To end the game, type "I give up"

Your guess: tries
❌❌❌🟨🟩
Your guess: meals
❌🟨🟩❌🟩
Your guess: apple
🟨❌❌🟩🟩
Your guess: letters
[a] b  c  d [e] f  g  h  ·
 j  k [l] ·  ·  ·  ·  q  ·
 ·  ·  u  v  w  x  y  z
Your guess: ladle
❌🟩❌🟩🟩
Your guess: cable
❌🟩🟩🟩🟩
Your guess: fable
Congratulations!
❌❌❌🟨❌ - tries
🟨🟨❌❌❌ - lemon
🟨❌❌🟩🟩 - apple
❌🟩❌🟩🟩 - ladle
❌🟩🟩🟩🟩 - cable
🟩🟩🟩🟩🟩 - fable
```
