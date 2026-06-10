# Focus Tasks Blocker

Productivity CLI app that blocks distracting websites while you work and unlocks them as a reward for completing tasks. Built in Python for the **CS50P** final project.

## How it works

1. You add tasks with name, priority, category, and deadline in the Extras menu
2. Start a focus session — the app blocks sites defined in code by modifying the Windows `hosts` file
3. As you complete tasks, the app gives you a configurable **relax time** (default 20 min) where sites are unblocked
4. A random motivational quote is printed after every task check

## Features

- Website blocking/unblocking via Windows `hosts` file
- Task management — add, view, and complete tasks stored in `Tasks.json`
- Relax time system — completing a task unlocks sites for a set amount of minutes
- Productivity graph — bar chart of completed tasks per day (Matplotlib)
- Custom quotes — add your own motivational quotes to `Reflexions.txt`
- Configurable relax time

## Tech stack

| Library | Use |
|---|---|
| `datetime` | Track task completion time and relax time countdown |
| `json` | Read/write task list to `Tasks.json` |
| `random` | Pick a random motivational quote |
| `time` | Sleep during relax period |
| `tabulate` | Display task list as a formatted table |
| `matplotlib` | Bar chart of completed tasks per day |

## Project structure

```
focus-tasks/
├── src/
│   └── project.py
├── tests/
│   └── test_project.py
├── data/
│   ├── Reflexions.txt
│   └── Tasks.json
└── README.md
```

## How to run

**Windows only** — website blocking requires modifying the system `hosts` file, which needs administrator privileges.

```bash
pip install tabulate matplotlib
python src/project.py
```

## Tests

```bash
pytest tests/test_project.py
```

## Academic context

Final project for **CS50's Introduction to Programming with Python (CS50P)** — 2025.
