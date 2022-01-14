# wordle
This is a quick little Wordle hack in Python to play on command line, written in Python 3.9 using only modules from the standard library.

I was introduced to Wordle today (2022 Jan 09) and I immediately wanted to play it without limits, so I put this together.

This game has been adapted to my Discord chat bot! You can find it here: https://crimso.bot/

## Example gameplay
```
$ python3 wordle.py
╔═══════════════════════════════════════╗
║  WORDLE: Guess the five-letter word!  ║
╚═══════════════════════════════════════╝
 If your letter is somewhere in word: +
 If your letter is in the right spot: $

 To see the letterboard, type "letters"
 To end, either win or type "I give up"


Your guess: tries 
- - - + +
Your guess: soled
$ + + + -
Your guess: letters
 a  b  c  - [e] f  g  h  - 
 j  k [l] m  n [o] p  q  -
[s] -  u  v  w  x  y  z
Your guess: slope
Congratulations!
- - - + + · tries
$ + + + - · soled
$ $ $ $ $ · slope
```
