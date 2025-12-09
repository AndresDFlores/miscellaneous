from collections import deque


#  recursion: current iteration output is next iteration input
def get_fibonacci(sequence:deque):

    #  append sum to sequence deque
    sequence.append(sum(sequence))
    print(sequence)

    #  recursive calculation
    get_fibonacci(sequence)


#  initialize deque container to keep O(1)
sequence = deque(maxlen=2)  # limit to 2 items in a deque
sequence.extend([0, 1])


#  this will crash at iter 1,000 because it calculates infinitely
get_fibonacci(sequence)