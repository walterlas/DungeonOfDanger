# DungeonOfDanger
Python 3 re-do of The Dungeon of Danger

The Dungeon of Danger
By Howard Berenban (c) 1983

From the book, "Mostly BASIC: Applications for your Atari, Book 2"

So, here we go again.

Notes:
02/24/2020: The GOTO is strong with this one. To the point where I need to keep track
of what BASIC line I'm going from, to which one I'm going to. Variable names are iffy
as I don't know what all of them do, yet. And some just seem to magically appear. My
brain is breaking.

02/26/2020: I don't normally say this but: Oh. My. God. I may actually have to map
this one out. Not the game, but the program. There are so many GOTOs and GOSUBS. There's
even an 'ON x GOSUB', which I hope works the way I think it does. I mean, I'm looking at 
two lines right now that are between two sections that I know the purpose of. These two lines
are, I kid you not, a GOSUB followed by a GOTO. Why? Why would anyone do that? To make
matters worse, there are lines that GOSUB to a spot, which then has conditional GOTO statements,
which eventually end in a RETURN. My defs all have returns, so there's no telling where 
it's going to end up. This thing will be a debugging nightmare. While I was stuck in 
traffic yesterday, I was thinking of making a "goto" and "gosub" routine that would
then go through a bunch of IF/ELSE statements to go to the correct section. I laughed,
but now I'm thinking it may be the way to go. At least temporarily.
For instance, I could call goto(1100) and the goto function could do an IF x == 1100: fight()
It's stupid..... but it may be the way to go. At least until I can get a handle on how
things are supposed to work. The mystery variables are bad enough.


