"""
Activity Selection Problem

This module implements the activity selection problem using a greedy algorithm.
The problem is to select the maximum number of activities that can be performed
by a single person, assuming that a person can only work on a single activity at a time.

Time Complexity: O(n log n) where n is the number of activities
Space Complexity: O(n)
"""
from typing import List, Tuple


def find_activities(activities: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Find the maximum number of activities that can be performed by a single person.

    Args:
        activities: A list of activities where each activity is represented as a tuple (start_time, end_time)

    Returns:
        A list of selected activities in the order they should be performed

    Example:
        >>> find_activities([(5, 9), (1, 2), (3, 4), (0, 6), (5, 7), (8, 9)])
        [(1, 2), (3, 4), (5, 7), (8, 9)]
    """
    if not activities:
        return []

    n = len(activities)
    selected = []

    # Sort activities by end time
    activities.sort(key=lambda x: x[1])

    i = 0

    # Since it is a greedy algorithm, the first activity is always
    # selected because it is the most optimal choice at that point
    selected.append(activities[i])

    for j in range(1, n):
        start_time_next_activity = activities[j][0]
        end_time_prev_activity = activities[i][1]

        # If the start time of the next activity is greater than or equal to
        # the end time of the previously selected activity, select this activity
        if start_time_next_activity >= end_time_prev_activity:
            selected.append(activities[j])
            i = j

    return selected


if __name__ == "__main__":
    # Test case
    activities = [(5, 9), (1, 2), (3, 4), (0, 6), (5, 7), (8, 9)]
    print(f"Activities: {activities}")
    print(f"Selected activities: {find_activities(activities)}")
