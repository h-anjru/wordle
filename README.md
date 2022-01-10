# wordle
A quick little Wordle hack in Python to play on command line.

I was introducted to Wordle today and I immediately wanted to play it without limits, so I put this together. The real trick, however, was finding an acceptable list of five-letter words to use. I have my personal qualms with teh Scrabble dictionary, but the most consistent and reliable list I could find online was a Scrabble list (https://wordfind.com/length/5-letter-words/). Because of the added difficulty of using such a wacky dictionary, I decided to add a hint to the beginning of each round: the word's Scrabble score.

I am hoping to implement this as part of my Discord bot soon and to complement it with statistics such a solve percentage and number of guesses. I would like to measure the difficulty of a word and not just its Scrabble score (the two are not very related; e.g. "abuzz" at 25 points is less difficult than "aa1ii" at 5 points), but I really don't know how I would go about that. Perhaps a better approach would be to use something less mind-bending than the Scrabble dictionary; my search for a more reasonable word list will continue.

Written in Python 3.9 using only modules from the standard library.
