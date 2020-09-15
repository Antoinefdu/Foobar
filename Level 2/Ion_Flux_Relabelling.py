'''Oh no! Commander Lambda's latest experiment to improve the efficiency of her LAMBCHOP doomsday device has backfired spectacularly.
She had been improving the structure of the ion flux converter tree, but something went terribly wrong and the flux chains exploded.
Some of the ion flux converters survived the explosion intact, but others had their position labels blasted off.
She's having her henchmen rebuild the ion flux converter tree by hand, but you think you can do it much more quickly - quickly enough,
perhaps, to earn a promotion!

Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one.
To label them, she performed a post-order traversal of the tree of converters and labeled each converter with the order of that converter
in the traversal, starting at 1. For example, a tree of 7 converters would look like the following:

      7
    /   \
  3      6
 /  \   / \
1   2  4   5
Write a function answer(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers representing different
 flux converters - which returns a list of integers p where each element in p is the label of the converter that sits on top of the respective
 converter in q, or -1 if there is no such converter. For example, answer(3, [1, 4, 7]) would return the converters above the converters
 at indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].

The domain of the integer h is 1 <= h <= 30, where
h = 1 represents a perfect binary tree containing only the root,
h = 2 represents a perfect binary tree with the root and two leaf nodes,
h = 3 represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above),
and so forth.
The lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.'''

def solution(h, q):

    def top_of_subtree(h):
        return 2**h-1

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

    final_output = []
    for item in q:
        if item == top_of_subtree(h):
            final_output.append(-1)
        else:
            final_output.append(analyse_node(h-1, item, 0))
    return final_output


print(solution(3, [7, 3, 5, 1]))

