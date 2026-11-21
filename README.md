# Simple Calculator

A simple command-line calculator written in Python.
Supports four basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features

- Enter two numbers (supports decimals, e.g. `3.5`)
- Choose an operation:
  1. Addition (`+`)
  2. Subtraction (`-`)
  3. Multiplication (`*`)
  4. Division (`/`)
- Division by zero check
- Error message for invalid operation choice

## How to Run

Make sure you have Python installed, then run:

```bash
python3 calculator.py
```

## Example

```text
Enter first number: 10.5
Enter second number: 2

select an operation
1 ------- +
2 ------- -
3 ------- *
4 ------- /

1
12.5
```

## Notes

- The program uses `float` for input, so it works with whole numbers and decimals.
- Division by zero is handled with a message instead of crashing.

## License

This is a beginner practice project. Feel free to use and modify it.
