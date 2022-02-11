# nyu-ai-lab-1

NYU Artificial Intelligence Course Lab 1: Build a generic hill-climbing solver.

## Prerequisite

- Python 3.8+

## Getting-started

### Switch to Python 3.8 on CIMS machines

The Python version has to at least have Protocol support, thus requiring Python 3.8+.

```bash
module load python-3.8
```

If successful, the command `python3 --version` should give you:

```bash
$ python3 --version
Python 3.8.6
```

### Script usages

> The main entrance is a python script, not a binary. It is in Shebang style,
> thus can be executed directly.

Use `./hill_climb -h` command to see the usage:

```
usage: hill_climb [-h] [-n N] [-k K] [--verbose] [--sideways SIDEWAYS]
                  [--restarts RESTARTS]

A generic hill climbing solver written in Python. Has built-in support
for N-Queens and Knapsack problems.

optional arguments:
  -h, --help           show this help message and exit
  -n N                 N queens problem only: number of queens
  -k K                 Knapsack problem only: input json filename
  --verbose            verbose output
  --sideways SIDEWAYS  number of sideways moves allowed
  --restarts RESTARTS  number of random restarts allowed
```

Use `-n N` to use N-Queens solver, or `-k K` to use Knapsack solver.

Examples:

```bash
$ ./hill_climb -n 4
```

```bash
$ ./hill_climb -k knapsack.json --verbose
```

```bash
$ ./hill_climb -k knapsack.json --verbose --sideways 5
```

## Project structure

```
project
├─hill_climbing                 hill_climbing python module
│  ├─__init__.py                    Module initialization
│  ├─hill_climbing.py               Generic Hill climbing solver and state protocol
│  ├─knapsack.py                    Knapsack problem state class
│  └─n_queens.py                    N-Queens problem state class
│
├─hill_climb                    Main entrance python script (shebang style)
└─README.md                     The file you're reading
```
