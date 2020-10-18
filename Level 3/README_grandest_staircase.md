* set boundaries : what's the max first step height, what's the min first step height?
* try by hand. Represent it visually and try to determine a pattern
* notice that there is a pattern of repetition after the first step. Meaning that we can "lock" a first step and then look up the amount of
possible ladders with the remaining bricks. This is particularly useful because we can use the fibonacci trick : loop through numbers from 1 to n,
log each result, and use those previous results to quickly determine the next results. Doing it this way and not the other way around prevents the
computer from repeat an amount of calculations that increases exponentially with the height of n.
* now that we know that, we need to find a new notation. Switching from Gimp to Excel and using the "x+y+z" notation
* at this point we need to break one of the rules: the one that states that a 1 step pile of bricks is not a staircase. That is because we realise
that most of the results will be used to inform further calculations, and in those scenarios, including a staircase of length 1 is perfectly fine.
So we will ignore this rule and simply subtract 1 when returning the final result.
* now we face a much bigger problem, which is that from n/2 to the lowest first step (calculated above), we have to subtract the sub-results that
have a first step that is higher than the current first step we're dealing with.

https://docs.google.com/spreadsheets/d/1bOaPDEBwJsRjAMoun2K-o3cTh2ES9fOSmiQuOaM9bak/edit?usp=sharing