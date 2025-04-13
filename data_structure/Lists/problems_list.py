"""
    This file contains problem code related to the list.
    """

""" 
    Problem 1: Valid subsequence
    Condition: 
    1)Upper Bound is O(n)
    2) return True when the list is subsequence of the array which has same order and element
    Ex) [1,2,3], [2,4] is subsequence of [1,2,3,4,5], and [1,3,2] is not.
    """

def is_valid_subsequence(array, sequence):
    array_index = 0
    sequence_index = 0
    while array_index < len(array) and sequence_index < len(sequence):
        if array[array_index] == sequence[sequence_index]:
            sequence_index += 1
        array_index += 1
    return sequence_index == len(sequence)


array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
sub1 = [1,2,3,4,5]
sub2 = [3,5,7,8,9,13]
sub3 = [5,2,3,57,20]

print("sub1")
print("True =", is_valid_subsequence(array,sub1))

print("sub2")
print("True =", is_valid_subsequence(array,sub2))

print("sub3")
print("False =", is_valid_subsequence(array,sub3))