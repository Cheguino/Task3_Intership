Rock-Paper-Scissors game

A script that implements a generalized rock-paper-scissors game (with the supports of arbitrary odd number of arbitrary combinations).

When launched with command line parameters it accepts an odd number ≥ 3 non-repeating strings (if the arguments are incorrect, you must display a neat error message—what exactly is wrong and an example of how to do it right). These passed strings are moves (for example, Rock Paper Scissors or Rock Paper Scissors Lizard Spock or 1 2 3 4 5 6 7 8 9).

The script generates a cryptographically strong random key (SecureRandom, RandomNumberGenerator, etc. - mandatory) with a length of at least 256 bits, makes own (computer's) move, calculates HMAC (based on SHA2 or SHA3) from the own move as a message with the generated key, displays the HMAC to the user. After that the user gets "menu" 1 - Stone, 2 - Scissors, ...., 0 - Exit. The user makes his choice (in case of incorrect input, the "menu" is displayed again). The script shows who won, the move of the computer and the original key.
.

.

.

rock Spock paper lizard scissors

HMAC: 9ED68097B2D5D9A968E85BD7094C75D00F96680DC43CDD6918168A8F50DE8507

Available moves:

1 - rock

2 - Spock

3 - paper

4 - lizard

5 - scissors

0 - exit

? - help

Enter your move: 3

Your move: paper

Computer move: rock

You win!

HMAC key: BD9BE48334BB9C5EC263953DA54727F707E95544739FCE7359C267E734E380A2



