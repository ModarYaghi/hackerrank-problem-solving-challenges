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

# Sample Input      # Sample Output
    4 5                     5
    10101                   2
    11100
    11010
    00101

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


def acm_team(attendees_topics):
    """
    Calculate the mximum number of topics a team of two can know
    and how many teams can know that many topics.

    Args:
        attendees_topics (list of str): A list where each string represents the topics
        known ny an attendee as a binary string.

    Returns:
        tuple: A tuple containing two elements:
            - The maximum number of topics any two attendees can collectively know.
            - The count of teams that know the maximum number of topics.
    """

    # This list will store the number of topics that each uniqu pair of attendees can know
    known_topics_per_team = []

    # Compare each attendee with every other attendee that follows them in the list
    for i, first_attendee_topics in enumerate(attendees_topics):
        for second_attendee_topics in attendees_topics[i + 1 :]:
            # Convert the binary strings to integers for bitwise operations
            first_topics_int = int(
                first_attendee_topics, 2
            )  # 2 here is to specify the bease of the number system of the parameter
            second_topics_int = int(second_attendee_topics, 2)

            # Perform bitwise OR to combine the topics known by both attendees
            combined_topics = first_topics_int | second_topics_int

            # Count the number of 1's in the binary representation of the result, representing the total topics known
            topics_known = bin(combined_topics).count("1")

            # Append the result to the list
            known_topics_per_team.append(topics_known)

    # Calculate the maximum number of topics known by any team
    max_topics_known = (
        max(known_topics_per_team) if known_topics_per_team else 0
    )  # though not necessary, handling edge cases for empty list or list with only one topic where no team can be formed

    # Count how many teams know that maximum number of topics
    max_topics_team_count = (
        known_topics_per_team.count(max_topics_known)
        if max_topics_known
        else 0  # though not necessary, handling edge cases
    )

    # Return the results as a tuple
    return (max_topics_known, max_topics_team_count)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    attendees_topic = []

    for _ in range(n):
        topic_item = input()
        attendees_topic.append(topic_item)

    result = acm_team(attendees_topic)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
