# Calculator App

This is a simple command-line calculator application written in Python. It can evaluate mathematical expressions provided as a string argument.

## Usage

To run the calculator, execute the `main.py` file with a mathematical expression enclosed in quotes as an argument:

```bash
python main.py "3 + 5 * (10 - 2) / 2"
```

## Example

```bash
python main.py "10 / 2 + 3"
```

Output:

```json
{
  "expression": "10 / 2 + 3",
  "result": 8.0
}
```

## Error Handling

The calculator handles basic errors such as invalid expressions.

```bash
python main.py "3 + "
```

Output:

```
Error: Invalid expression
```
