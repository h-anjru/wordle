# wordle
This is a quick little Wordle hack in Python to play on command line, written in Python 3.9 using only modules from the standard library.

I was introduced to Wordle today (2022 Jan 09) and I immediately wanted to play it without limits, so I put this together. The real trick, however, was finding an acceptable list of five-letter words to use. I have my personal qualms with the Scrabble dictionary, but the most consistent and reliable list I could find online was a Scrabble list (https://wordfind.com/length/5-letter-words/). Because of the added difficulty of using such a wacky dictionary, I decided to add a hint to the beginning of each round: the word's Scrabble score.

I am hoping to implement this as part of my Discord bot soon and to complement it with statistics such a solve percentage and number of guesses. I would like to measure the difficulty of a word and not just its Scrabble score (the two are not related; e.g. "abuzz" at 25 points is less difficult than "aalii" at 5 points), but I really don't know how I would go about that. I could try to remove ridiculous words, but the list at current is 8914 words long. Perhaps a better approach would be to use something less mind-bending than the Scrabble list, if I can find one.

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