>Ion Flux Relabelling
>====================
>Oh no! Commander Lambda's latest experiment to improve the efficiency of her LAMBCHOP doomsday device has backfired
> spectacularly.
She had been improving the structure of the ion flux converter tree, but something went terribly wrong and the flux chains exploded.
Some of the ion flux converters survived the explosion intact, but others had their position labels blasted off.
She's having her henchmen rebuild the ion flux converter tree by hand, but you think you can do it much more quickly - quickly enough,
perhaps, to earn a promotion!
Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one.
To label them, she performed a post-order traversal of the tree of converters and labeled each converter with the order of that converter
in the traversal, starting at 1. For example, a tree of 7 converters would look like the following:
>
>           7
>         /   \
>       3      6
>      / \    / \
>     1   2  4   5
>Write a function answer(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers representing different
 flux converters - which returns a list of integers p where each element in p is the label of the converter that sits on top of the respective
 converter in q, or -1 if there is no such converter. For example, answer(3, [1, 4, 7]) would return the converters above the converters
 at indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].
>
>The domain of the integer h is 1 <= h <= 30, where
h = 1 represents a perfect binary tree containing only the root,
h = 2 represents a perfect binary tree with the root and two leaf nodes,
h = 3 represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above),
and so forth.
The lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.

# Reasoning:

First of all a bit of context: a binary search tree is a form of data structure where each node is connected to 2 other nodes. So in essence, each
 node is an object with 3 properties: a value, a left connection and a right connection.   
So in the tree they give as example,  
the node 7 has for value "7", left connector 3 and right connector 6  
the node 3 has for value "3", left connector 1 and right connector 2  
the node 6 has for value "6", left connector 4 and right connector 5  

Now they call this tree a "perfect" binary tree, which means that the lowest level of the tree is completely filled with numbers. Because that's
 not always the case with binary trees. In non-perfect trees, sometimes nodes have only one branch.  
And finally they mention that the trees are filled following a "post-order traversal", meaning that, starting with the bottom left, we will go
 through that tree following the order "left-right-root" (root means "up" in this case. You have to imagine an upside-down tree, the top node is
  the "root", the lowest level are the "leaves")  


in the question they give you an example for a perfect binary tree of height 3 (so 3 "floors" if you will). I'll draw a height 5 below to help you
 visualise the whole "post-order traversal" thing:  

                                       31
                         /                           \
                     15                                  30
              /            \                       /            \
           7                 14                 22                29
        /     \           /      \            /     \          /       \
       3       6        10        13        18       21       25       28
     /  \     /  \     /  \      /  \      /  \     /  \     /  \     /  \
    1    2   4    5   8    9   11    12  16   17   19  20   23   24  26   27



and so just by looking closely at this tree, you can start noticing some patterns:

1) if you look at the left-most numbers, they seem to be powers of 2, -1.   
Meaning that if you want to calculate the value of the left-most node at height 1, it's 2^1-1 = 1  
height 2   : 2^2-1 = 3  
height 3   : 2^3-1 = 7   
height 4   : 2^4-1 = 15    
height 26 : 2^26-1 = 67108863  

2) similarly, and still and still reading each "level" of the tree from left to right, the second value is always the double of the first  
height 1   : 1 ==> 2  
height 2   : 3 ==> 6  
height 3   : 7 ==> 14  
height 4   : 15 ==> 30  
height 26 : 67108863 ==> 134217726

3) very simple pattern : in any subtree, the root is equal to the right node + 1  
15 = 14+1  
22 = 21+1  
25 = 24+1  
31 = 30+1  
etc  

    and finally we need a rule to find the value of the nodes that are not the first or second left-most of their height, and for that we need rule #4:  

4) The distance between any node and its left-most counterpart is the value of the highest subtree that they don't have in common.  
for example, the distance between the node 22 and its left-most counterpart (7) is 15, the highest subtree that they don't have in common.  
the distance between 6 and 13 is 7, the highest subtree that they don't have in common. Now how do we calculate that without looking at the tree
? Very simply, since we know the height of the tree (say, we're working on a tree of height 5), we can start from the top and work our way down
 each left-most node until we find a left-most node whose value is smaller than the number we're analysing.   
For example, looking at node "22" and starting from level 5,  
"Is 22 bigger than 2^5-1 (31)? Nope. Alright, moving down to level 4.  
Is 22 bigger than 2^4-1 (15)? Yep. Then the left-most counterpart of 22 is 22-15 = 7."  

but you can also use this rule several times in a row. For example, 23: what's its left-most counterpart? Well, what's the highest subtree that 23
 doesn't belong to? 23 is smaller than 31 but bigger than 15.  
So let's remove 15 from 23 and put it aside for now. Say "temporary_solution" = 15 and 23 becomes 8  
Now same process again, 8 : what's the highest subtree that it doesn't belong to?   
8 < 31   
8 < 15   
8 > 7  
so now we can set aside 7, which we add to our "temporary_solution". So 8 becomes 1, and temporary solution becomes 15+7=22  
So now I can do the exercise (which in this case is "return the value of the parent node) on node 1. I'll get 3. Then add "temporary_solution" and
 I get 22+3 = 25, the parent node of node 22.  

btw, what I did right there (doing the same operations on an item over and over again) that's called a recursive process. It can be very dangerous
 in some scenarios because it can throw your computer in an infinite loop, but sometimes (like here) it can save you and your computer a lot of
  time and energy.  


So all we gotta do now is actually answer the question ("return the value of the parent node") for each node given to us, assuming that the node we
're analysing is either the left-most (or "left branch") or the second left-most ("right branch") of its height.  

If we are dealing with a left branch, well first of all that's very easy to determine. The first left branch is always 2^h-1 at height h (rule#1)  
and how do we determine the parent node from there? Simply by multiplying by 2 to get the value of the right branch, (rule #2), then adding 1 (rule #3)

If it's the right branch, well first how do we know that a node is the first right branch of its height? Simply by using rule #2 : if the value of
 the node is exactly 2 times the left-branch of its height, then it's the right branch.  
2   = (2^1-1)*2  
6   = (2^2-1)*2  
14 = (2^3-1)*2  
30 = (2^4-1)*2  
etc  
and so all we have to do, as discussed in rule #3, is add 1  
2 => 3 ; 6 => 6 ; 14 => 15, etc  


so from that point onwards, the code writes itself.   
First I defined a function "top of subtree" with a parameter h and which returns 2^h+1. because I knew that I would need to do that operation a lot
 of times  

def top_of_subtree(h):  
      return 2**h-1  

then I define the main function "analyse node", that will take as parameter the value of the node (n), a "output" parameter that will be set to 0
 by default and will serve as a cache for when I call the function recursively (remember the example above, when I started with 23, then I set
  apart 15, then 7. Well 15 and 7 will go to the cache), and finally the height (h) of the subtree I'm analysing. I will always start from the
   maximum height of the tree, which will be given to me in each input, then work my way down in increments of h-1. I'll spare you the details, but
    it looks like this  
    
    def analyse_node(h, n, output):  
            if n == top_of_subtree(h) * 2:  
                '''item is top of right subtree'''  
                output += n + 1  
            elif n == top_of_subtree(h):
                '''item is top of left subtree'''
                output += n + top_of_subtree(h) + 1
            elif n > top_of_subtree(h):
                '''item is under the right subtree'''
                n = n-top_of_subtree(h)
                output += top_of_subtree(h)
                h = h-1
                output = analyse_node(h, n, output)
            elif n < top_of_subtree(h):
                '''item is under the left subtree'''
                h = h-1
                output = analyse_node(h, n, output)
            return output


And now all I have to do is put those 2 functions in my main "solution" function, create an empty list ("final_output") where I'll put my answers
 for each node, then a little "for loop" that will cycle through each node given to me in the input and will put the answer into final_output  


and we get a solution that fits under 25 lines:

    def solution(h, q):
        def top_of_subtree(h):
            return 2**h-1
        def analyse_node(h, n, output):
            if n == top_of_subtree(h) * 2:
                output += n + 1
            elif n == top_of_subtree(h):
                output += n + top_of_subtree(h) + 1
            elif n > top_of_subtree(h):
                n = n-top_of_subtree(h)
                output += top_of_subtree(h)
                h = h-1
                output = analyse_node(h, n, output)
            elif n < top_of_subtree(h):
                h = h-1
                output = analyse_node(h, n, output)
            return output
        final_output = []
        for item in q:
            if item == top_of_subtree(h):
                final_output.append(-1)
            else:
                final_output.append(analyse_node(h-1, item, 0))
        return final_output