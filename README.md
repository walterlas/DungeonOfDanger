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

03/03/2020: OK. It is now basically working. There are probably still a lot of bugs where
I didn't get the branching correct. In fact, I think there's an entire section I haven't
even put in yet. I'm not sure how that gets called, but it may not be too hard to figure
out. Still need to tune the screen clearing and pauses, though. If you're wondering why
there's a lot of pauses and why there's so many '.' in the text, it's because that's how
the original is. If I finish the original version, I may branch off and make a "plus" 
version that will fix all that. Also, I really need to figure out some variables, still.
It's kind of weird to be this far in and still not know what some do. Like, I think 
the game ending when you run of turns works, but I haven't the faintest idea of where
the maximum moves is defined. Go figure.

03/04/2020: Every once in a while I like to sort of start over. This means creating a new
file and then going over the old code and re-implementing it wherever I see that I can
do things better. Or catch a glaring mistake. It was in doing this (dod4.py), that I 
realized that dod3.py wasn't going to work correctly. It's kind of amazing it works
at all. Even still, there are some things that don't seem right to me. For instance,
the starting hit points can be way higher than they're supposed to be. I may have to
run the Atari800 emulator and do some experimenting to see what may be going on. Other
than that, I think I have a handle on things now. Sure, there are still variables that
don't make sense to me (they aren't very descriptive in the BASIC listing). And, after
searching the PDF for the variables, they don't seem to do anything there, either. So
they may end up on the cutting room floor, so to speak.

