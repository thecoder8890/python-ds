# Python Data Structures and Algorithms

Clean, well-documented implementations of common data structures and algorithms in Python. This repository follows a consistent approach throughout all implementations, making it ideal for learning and interview preparation.

## Table of Contents

- [Overview](#overview)
- [Python Version Compatibility](#python-version-compatibility)
- [Installation](#installation)
- [Usage](#usage)
- [Structure of the Repository](#structure-of-the-repository)
  - [Data Structures](#data-structures)
  - [Algorithms](#algorithms)
  - [Bookmarks](#bookmarks)
- [Code Style and Documentation](#code-style-and-documentation)
- [Contributing](#contributing)
- [Future Improvements](#future-improvements)
- [License](#license)

## Overview

This repository contains implementations of various data structures and algorithms in Python. The code is designed to be:

- **Clean and readable**: Following PEP 8 style guidelines
- **Well-documented**: With comprehensive docstrings and comments
- **Educational**: Focusing on clarity rather than optimization
- **Interview-friendly**: Covering common interview questions and patterns

## Python Version Compatibility

The code in this repository is compatible with **Python 3.6+**. It uses modern Python features such as:

- Type hints (PEP 484)
- F-strings (Python 3.6+)
- Modern class definitions (no need for explicit inheritance from object)
- Up-to-date import conventions

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/prabhupant/python-ds.git
cd python-ds
```

No additional dependencies are required to run the code examples.

## Usage

Each implementation can be run directly as a Python script. Most files include test cases that demonstrate how to use the implementation.

For example, to run the activity selection algorithm:

```bash
python algorithms/greedy/activity_selection.py
```

You can also import the implementations into your own code:

```python
from data_structures.stack.stack_using_linked_list import Stack, Element

# Create a new stack
stack = Stack()

# Push elements onto the stack
stack.push(Element(1))
stack.push(Element(2))

# Pop an element from the stack
element = stack.pop()
print(element.value)  # Output: 2
```

## Structure of the Repository

The repository is organized into three main directories:

### Data Structures

Contains implementations of various data structures, categorized by type:

1. [Array](data_structures/array) - Array manipulations and operations
2. [Binary Search Tree](data_structures/bst) - BST implementations and operations
3. [Binary Trees](data_structures/binary_trees) - Binary tree algorithms
4. [Circular Linked List](data_structures/circular_linked_list) - Circular linked list implementations
5. [Deque](data_structures/deque) - Double-ended queue implementations
6. [Doubly Linked List](data_structures/doubly_linked_list) - Doubly linked list implementations
7. [Fenwick Tree](data_structures/fenwick_tree) - Binary indexed tree implementations
8. [Graphs](data_structures/graphs) - Graph algorithms and representations
9. [Hash](data_structures/hash) - Hash table implementations
10. [Heap](data_structures/heap) - Min and max heap implementations
11. [Linked List](data_structures/linked_list) - Singly linked list implementations
12. [Matrix](data_structures/matrix) - Matrix operations
13. [Palindromic Tree](data_structures/palindromic_tree) - Specialized tree for palindromes
14. [Queue](data_structures/queue) - Queue implementations
15. [Segment Tree](data_structures/segment_tree) - Segment tree implementations
16. [Stack](data_structures/stack) - Stack implementations
17. [Strings](data_structures/strings) - String manipulation algorithms
18. [Trie](data_structures/trie) - Trie implementations
19. [Union Find](data_structures/union_find) - Disjoint set data structure

### Algorithms

Contains implementations of various algorithms, categorized by type:

1. [Bit Manipulation](algorithms/bit_manipulation) - Bit manipulation techniques
2. [Dynamic Programming](algorithms/dynamic_programming) - DP solutions to common problems
3. [Greedy](algorithms/greedy) - Greedy algorithm implementations
4. [Math](algorithms/math) - Mathematical algorithms
5. [Miscellaneous](algorithms/miscellaneous) - Other algorithm implementations
6. [Sorting](algorithms/sorting) - Sorting algorithm implementations

### Bookmarks

Contains useful links to external resources, categorized by type:

| Category | Link |
| :-- | :--: |
| Articles | [Click Here](bookmarks/articles.md) |
| Books | [Click Here](bookmarks/books.md) |
| Topics | [Click Here](bookmarks/topics.md) |
| Tutorials | [Click Here](bookmarks/tutorials.md) |
| Videos | [Click Here](bookmarks/videos.md) |
| Misc. | [Click Here](bookmarks/misc.md) |

## Code Style and Documentation

All code in this repository follows the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide. Each implementation includes:

- A module-level docstring explaining the data structure or algorithm
- Function/method docstrings with parameters and return values
- Type hints for function parameters and return values
- Inline comments explaining complex logic
- Time and space complexity analysis

Example:

```python
def binary_search(arr: List[int], target: int) -> int:
    """
    Perform binary search on a sorted array.

    Args:
        arr: A sorted list of integers
        target: The value to search for

    Returns:
        The index of the target if found, -1 otherwise

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # Implementation details...
```

## Contributing

Contributions are always welcome! Please read the [Contributing Guidelines](CONTRIBUTING.md) before submitting a pull request.

Some ways to contribute:
- Add new data structure or algorithm implementations
- Improve existing implementations
- Add test cases
- Fix bugs
- Improve documentation

## Future Improvements

The repository is continuously evolving. Here are some planned improvements:

1. Add more queue implementations and examples
2. Expand the algorithms section with more common algorithms
3. Add more examples for graph algorithms, trees, heaps, and hash tables
4. Add unit tests for all implementations
5. Add visualization tools for data structures and algorithms

## License

This project is licensed under the [MIT License](LICENSE).
