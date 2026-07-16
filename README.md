# NeetCode Submissions

My accepted solutions to [NeetCode.io](https://neetcode.io) problems, synced from the NeetCode GitHub integration.

## Overview

This repository is an archive of my problem submissions from NeetCode.io. It currently holds **267 submission files across 182 problems**, all under the **Data Structures & Algorithms** track and all written in **Python**. Problems span the common interview topics covered by NeetCode: arrays and hashing, two pointers, sliding window, stacks, binary search, linked lists, trees, tries, heaps, backtracking, graphs, dynamic programming, greedy, intervals, and bit manipulation.

## How it's organized

Solutions are grouped by track folder, then by problem slug. Each attempt is saved as a separate numbered file, so a problem with multiple accepted attempts keeps all of them:

```
Data Structures & Algorithms/
  <problem-slug>/
    submission-0.py   # an accepted attempt
    submission-2.py   # a later attempt for the same problem
  ...
```

Example: `Data Structures & Algorithms/two-integer-sum/submission-3.py`

The `submission-N` number is the index assigned by NeetCode's sync, not a ranking — a single problem folder may contain any subset of numbered attempts.

## How to navigate

- Browse the `Data Structures & Algorithms/` folder and open the folder matching the problem slug (e.g. `binary-search`, `word-ladder`, `lru-cache`).
- Slugs mirror the problem names on NeetCode.io, so you can find the corresponding problem and video explanation there.
- Multiple `submission-*.py` files in one folder are alternative or iterated solutions to the same problem.

## Tech stack

- **Python 3** — every solution in this repository.

## Project structure

```
.
├── Data Structures & Algorithms/   # 182 problem folders, one per NeetCode problem
│   └── <problem-slug>/             # numbered submission-*.py files
└── README.md
```
