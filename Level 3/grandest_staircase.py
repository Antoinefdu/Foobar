'''The Grandest Staircase Of Them All
==================================

With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order to make a grand
entrance,  she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how to build the best staircase EVER.

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (
for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with
each amount of bricks, so she can pick the one with the most options.

Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the
previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having
a height of 1: (# indicates a brick)

#
##
21

When N = 4, you still only have 1 staircase choice:

#
#
##
31

But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2),
as shown below:

#
#
#
##
41

#
##
##
32

Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n
bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!'''


def solution(n):
    log_dict = {0: [1], 1: [1]}
    i=2
    while i <= n:
        lowest_first_step = round((2*i)**(1/2))
        nval = []
        start = 0
        for j in range(int((i-lowest_first_step)+1)):
            if j > (i-1)//2:
                start += i%2+1 if start == 0 else 2
            jval = sum(log_dict[j][start:])
            nval.append(jval)
        log_dict[i] = nval
        i += 1
    print(log_dict)
    return sum(log_dict[n])-1


print(solution(200))


'''
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

'''