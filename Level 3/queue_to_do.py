def solution(start, length):
    final_output = 0
    row_start = start
    row_length = length
    for _ in range(length):
        final_output ^= prefix_xor(row_start-1)^prefix_xor(row_start+row_length-1)
        row_start += length
        row_length -= 1
    return final_output


def prefix_xor(num):
    output = 0
    if (num-1)/2%2 == 0:
        output += 1
    if num%2 == 0:
        output += num
    return output


print(solution(46713, 789230))