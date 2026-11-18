
"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.

Application: DJ music library search system.
"""


def linear_search(lst, target, stats=None):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    if stats is not None:
        stats["comparisons"] = 0

    # Search each element from the beginning of the list.
    for index in range(len(lst)):

        if stats is not None:
            stats["comparisons"] += 1

        # Return the index if the target is found.
        if lst[index] == target:
            return index

    # Linear search has O(n) time complexity because
    # it may need to check every element in the list.

    # Return -1 if the target does not exist.
    return -1


def binary_search(lst, target, stats=None):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    low = 0
    high = len(lst) - 1

    if stats is not None:
        stats["comparisons"] = 0

    while low <= high:

        # Find the middle index of the search range.
        mid = (low + high) // 2
        current = lst[mid]

        if stats is not None:
            stats["comparisons"] += 1

        if current == target:
            return mid

        elif current < target:
            # Ignore the left half of the search range.
            low = mid + 1

        else:
            # Ignore the right half of the search range.
            high = mid - 1

    # Binary search has O(log n) time complexity because
    # each iteration eliminates roughly half of the
    # remaining elements.

    # Return -1 if the target does not exist.
    return -1


def compare_searches(lst, target, expected_index):
    """
    Compare the results and number of elements checked
    by both search algorithms.
    """

    linear_stats = {}
    binary_stats = {}

    linear_index = linear_search(lst, target, linear_stats)
    binary_index = binary_search(lst, target, binary_stats)

    print(f"\nSearching for: {target}")

    print(f"Linear search index: {linear_index}")
    print(f"Linear search comparisons: "
          f"{linear_stats['comparisons']}")

    print(f"Binary search index: {binary_index}")
    print(f"Binary search comparisons: "
          f"{binary_stats['comparisons']}")

    # Verify that both algorithms return the correct index.
    assert linear_index == expected_index
    assert binary_index == expected_index


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")
    print("Application: DJ Music Library")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    small_library = [
        "After Hours",
        "Bassline",
        "Control",
        "Dark Room",
        "Echoes",
        "Frequency",
        "Midnight",
        "Pulse",
        "Rush",
        "Voltage"
    ]

    print(f"Dataset: {small_library}")
    print(f"Dataset size: {len(small_library)}")

    # Search for a song that exists in the library.
    # Both algorithms should return index 7.
    compare_searches(small_library, "Pulse", 7)

    # Search for a song that does not exist.
    # Both algorithms should return -1.
    compare_searches(small_library, "Unknown Track", -1)

    # Binary search checks fewer elements because
    # the music library is sorted alphabetically.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # Generate a simulated music library of 10,000 tracks.
    # Leading zeros keep the track names sorted.
    large_library = [
        f"Track {number:05d}"
        for number in range(1, 10001)
    ]

    print(f"Dataset size: {len(large_library)}")

    # Search for the final track in the library.
    compare_searches(large_library, "Track 10000", 9999)

    # Search for a track that does not exist.
    compare_searches(large_library, "Track 10001", -1)

    # Linear search must check all 10,000 elements
    # in these examples. Binary search only checks
    # 14 elements because it repeatedly divides the
    # search range in half.

    # As the dataset grows, binary search becomes
    # significantly more efficient than linear search.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Empty list.
    # Both algorithms return -1 without checking any elements.
    print("\nEdge Case 1: Empty List")
    compare_searches([], "Pulse", -1)

    # Edge case 2: Single-element list.
    # Both algorithms find the target at index 0.
    print("\nEdge Case 2: Single-Element List")
    compare_searches(["Pulse"], "Pulse", 0)

    # Edge case 3: Missing value in a single-element list.
    # Both algorithms return -1.
    print("\nEdge Case 3: Missing Value")
    compare_searches(["Pulse"], "Voltage", -1)

    # Edge case 4: Target at the first position.
    # Linear search is faster in comparisons because
    # it immediately finds the target.
    print("\nEdge Case 4: First Position")
    compare_searches(small_library, "After Hours", 0)

    # Edge case 5: Target at the last position.
    # Binary search checks fewer elements than linear search.
    print("\nEdge Case 5: Last Position")
    compare_searches(small_library, "Voltage", 9)

    print("\n=== ALL TESTS PASSED ===")


if __name__ == "__main__":
    main()
