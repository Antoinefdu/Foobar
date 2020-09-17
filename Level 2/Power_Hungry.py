def solution(xs):
    xs = sorted(xs, key=abs, reverse=True)  # making sure that the only negative we leave in cache is the smallest one
    if len(xs) == 1:
        return str(xs[0])
    else:
        output = 0  # we will redefine this as 1 as soon as we find an integer that is > 0, or 2 that are < 0
        neg_cache = 1
        for _ in xs:
            if _ < 0:
                if neg_cache == 1:
                    neg_cache *= _
                else:  # if neg_cache != 1, then it is < 0
                    output = 1 if output == 0 else output
                    output *= _ * neg_cache
                    neg_cache /= neg_cache  # neg_cache set back to 1
            elif _ > 0:
                output = 1 if output == 0 else output
                output *= _
        return str(output)


print(solution([0, 1]))
print(solution([0, 0, 0, 0, 0, -1]))
print(solution([0, 0, 0, 0, 0, 0]))
print(solution([-1, -1]))
print(solution([-1, -2, -4]))
print(solution([2, 0, 2, 2, 0]))
print(solution([-2, -3, 4, -5]))
print(solution([2, -3, 1, 0, -5]))
print(solution([34, 1, 5, 12, 6, 3]))
print(solution([-2]))
print(solution([]))
print(solution([-34, -31, -30 , -16, -12, -11, -10, -7, -7, -3, -1] ))