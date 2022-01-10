# wordle
This is a quick little Wordle hack in Python to play on command line, written in Python 3.9 using only modules from the standard library.

I was introduced to Wordle today (2022 Jan 09) and I immediately wanted to play it without limits, so I put this together.

## Example gameplay
```
$ python3 wordle.py
Try to guess the five-letter word!
Scrabble (US) score: 7
To see eliminated letters, type "letters"
To end the game, type "I give up"

Your guess: bread
❌🟨🟨❌❌
Your guess: remit 
🟩🟩❌❌❌
Your guess: renew
🟩🟩❌🟩❌
Your guess: letters
 a  b  c  · [e] f  g  h  · 
 j  k  l  ·  ·  o  p  q [r]
 s  ·  u  v  ·  x  y  z
Your guess: revel
🟩🟩❌🟩🟩
Your guess: rebel
🟩🟩❌🟩🟩
Your guess: repel
Congratulations!
❌🟨🟨❌❌
🟩🟩❌❌❌
🟩🟩❌🟩❌
🟩🟩❌🟩🟩
🟩🟩❌🟩🟩
🟩🟩🟩🟩🟩
```