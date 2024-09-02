"""
There are number of people who will be attending ACM_ICPC World Finals.
Each of them may be well versed in a number of topics.
Given a list of topics known by each attendee, presented as binary strings,
determine the maximum number of topics a 2-person team can know.
Each subject has a column in the binary string, and a '1' means the subject
is known while '0' means it is not. Also determine the number of teams that know
the maximum number of topics.
Return an interger array with two elements. The first is the maximum number of
topics knwon, and the second is the number of teams that know that number of topics

# Objective
    The goal is to determine the maximum number of topics any team of two attendees can 
    know between them and to find how many teams can achieve this maximum.

# Example

    n = 3

    topics = ['10101', '11110', '00010']

    The attendee data is aligned for clarity below:

    '''
    10101
    11110
    00010
    '''

    These are all possible teams that can be formed:

    '''
    (1, 2)  [1, 2, 3, 4, 5]
    (1, 3)  [1, 3, 4, 5]
    (2, 3)  [1, 2, 3, 4]
    '''

# Function Description

    The function has the following parameter(s):
        - string topic: a string of binary digits

# Return

    - int[2]: the maximum topics and the number of teams that know that many topics

# Input Format

    The first line contains two space-separated integers n and m, where n is the number
    of attendees and m is the number of topics.

    Each fo the next n lines contains a binary string of length m.

# Constraints

    2 <= n <= 500
    1 <= m <= 500

# Team Knowledge Calculation:

    When forming a team of two, the combined knowledge of the team is determined by 
    the bitwise OR operation on their respective binary strings. This is because 
    the OR operation results in a '1' if either of the bits being compared is '1', 
    reflecting the fact that if either member knows a topic, then the team knows it.

    For example, if one member knows topics represented by 10101 and another knows 11110,
    the team collectively knows topics represented by 11111 because each bit position in
    the resultant string is set to '1' if either corresponding bit in the original strings

# Sample Input
    4 5
    10101
    11100
    11010
    00101

# Sample Output

    5
    2

# Explanation

    Calculating topics know for all permutations of 2 attendees we get:
    
    (1, 2) -> 4
    (1, 3) -> 5
    (1, 4) -> 3
    (2, 3) -> 4
    (2, 4) -> 4
    (3, 4) -> 5

    The 2 teams (1, 3) and (3, 4) know all 5 topics which is maximal.

"""

import os


def acm_team(topic):
    print()
    for i, topic_i in enumerate(topic):
        for t in topic[i + 1 :]:
            print(topic_i, t)
            int1, int2 = int(topic_i, 2), int(t, 2)
            combined_int = int1 | int2

    return topic


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acm_team(topic)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
