# Project Party #

A simple console application for randomizing party members, intended for use in Eiyuden Chronicles, but should work perfectly fine for Suikoden as well.

## "Setup" ##
Simply create a file called "roster.txt" that contains a list of recruitable characters in the root folder, and the application will create the appropriate .json file.

All characters will be assumed to be combatants, so any character can be disabled in-app with the "toggle" command, or by manually editing the "combatant" property in the .json file.

## Commands ##
*All commands can be repeated by separating the arguments with a ","*

* ### Randomize X###
Will randomly select up to X characters from all recruited characters who are also combatants (unless they've been disabled).

**"Randomize 6"** will randomly select 6 eligible party members from the roster.  
**"Randomize"** will randomly select 5 eligible party members from the roster.

*If X is invalid, or not provided, the command will randomize up to 5 party members.*

* ### Recruit X ###
Will recruit a character that contains X in their name, as long as there is only one match.

**"Recruit Yuferius"** will recruit Yufierius VII, despite "VII" not being provided.  
**"Recruit i"** will not recruit anyone, since there are multiple characters that contain the letter "i".

*Assuming the order is the same, and that characters are removed when recruited, the number refers to the recruited characters position in a deck of cards (Collector Cards Add-On)*

* ### Toggle X ###
Will toggle the enabled state of a character that contains X in their name, as long as there is only one match.

**"Toggle Yuferius"** will disable/enable Yuferius VII, despite "VII" not being provided.  
**"Toggle i"** will not toggle anyone, since there are multiple characters that contain the letter "i".
