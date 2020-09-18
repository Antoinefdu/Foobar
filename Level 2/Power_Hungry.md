>  Power Hungry
>  ============ 
>
>  Commander Lambda's space station is HUGE. And huge space stations take a LOT of power. Huge space stations with doomsday
>   devices take even more power. To help meet the station's power needs, Commander Lambda has installed solar panels on
>    the station's outer surface. But the station sits in the middle of a quasar quantum flux field, which wreaks havoc on
>     the solar panels. You and your team of henchmen have been assigned to repair the solar panels, but you'd rather not
>      take down all of the panels at once if you can help it, since they do help power the space station and all!
>  
>  You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining
>   the maximum amount of power output per array, and to do THAT, you'll first need to figure out what the maximum output
>    of each array actually is. Write a function solution(xs) that takes a list of integers representing the power output
>     levels of each panel in an array, and returns the maximum product of some non-empty subset of those numbers. So for
>      example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would
>       be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30.  So
>        solution([2,-3,1,0,-5]) will be "30".
>  
>  Each array of solar panels contains at least 1 and no more than 50 panels, and each panel will have a power output
>   level whose absolute value is no greater than 1000 (some panels are malfunctioning so badly that they're draining
>    energy, but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to
>     produce the positive output of the multiple of their power values). The final products may be very large, so give
>      the solution as a string representation of the number.

# Reasoning : 
First off, a quick tl;dr of the question :  
> Given an array of integers, what is the highest product you can reach by multiplying a subset of this array?  

If the array is strictly composed of positive non-null integers, that's easy : you just multiply them all:  
[34, 1, 5, 12, 6, 3] ==> 34 * 1 * 5 * 12 * 6 * 3 = 36720  

Similarly, if we have an even amount of negative integers in our list, we can simply treat them as if they were positive, since (-1) * (-1) = 1  
[-34, 1, -5, -12, 6, -3] ==> -34 * 1 * -5 * -12 * 6 * -3 = 36720  

Finally, if our array contains one or more 0s, we can simply ignore them:  
[0, 34, 0, 1, 0, 5, 0, 0, 12, 0, 6, 3, 0, 0, 0] ==> 34 * 1 * 5 * 12 * 6 * 3 = 36720  

So far so good, but we are left with 2 problems to solve:
1. What do we do if there is no multiplication to do? What should our function return if the array only contains 1 integer (which could be negative
), or if the array is empty?    

    This one is pretty easy, we can just start by stating as a general rule that if the array contains 1 item, we output that item.  
Otherwise, we will output  '0 + 1 * [the algotithm applied to each item in the array]'

2. (most importantly) What do we do if we have an odd amount of negative integers? We ignore one, sure, but which one?  
Imagine a naive algorithm that would reach the end of a very long array, only to find out that he has included an odd number of negative integers
 in its product. It can't simply ignore the last negative and has to go back and look for the smallest negative integer in the array. Aoutch.

    One possible solution to this would be to, as we iterate through the array, take note of the smallest (in absolute value) negative integer that
     we've encountered so far. Then, at the end of the algo, if we realise that we've ended up with a negative solution, we divide it with that
      smallest negative. However, I wrote this a while ago, at a time when I was not familiar with the time-complexity of a sort method (O (n logn)
      )) so I started my answer by doing exactly that. The idea behind sorting the array first (in decreasing order) is that I will start by
       multiplying the integers that have the highest absolute value. Now if we ignore positive integers for a moment and focus on the negative
        ones, this means that I can essentially combine the product of those negatives in pairs, leaving out any potential odd negative which will
         by definition be the smallest one.   
         For example, let's say that out array (after sorting) looks like this [-34, -31, -30 , -16, -12, -11, -10, -7, -7, -3, -1] gives us:  
         1 * (-34 * -31) = 1054  
         * (-30 * -16) = 505920  
         * (-12 * -11) = 66781440  
         * (-10 * -7) = 467700800  
         * (-7 * -3) = 98168716800  
         leaving aside the last and smallest negative (-1).
         
As with the previous exercise, once the logic is clear, the code pretty much writes itself:

    def solution(xs):
    xs = sorted(xs, key=abs, reverse=True)
    if len(xs) == 1:
        return str(xs[0])
    else:
        output = 0
        neg_cache = 1
        for _ in xs:
            if _ < 0:
                if neg_cache == 1:
                    neg_cache *= _
                else:  # if neg_cache != 1, then it is < 0
                    output = 1 if output == 0 else output
                    output *= _ * neg_cache
                    neg_cache /= neg_cache
            elif _ > 0:
                output = 1 if output == 0 else output
                output *= _
        return str(output)

