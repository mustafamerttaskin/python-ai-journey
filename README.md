# python-ai-journey

![Python](https://img.shields.io/badge/python-3.x-blue)

A running log of small Python exercises as I build up from fundamentals
toward data analysis and automation. Each file is a self-contained daily
exercise, kept as-is (including any earlier ones) so the progression stays
visible.

## Contents

| File | What it covers |
|------|-----------------|
| `day1.py` | First script — basic `print` output. |
| `day2.py` | Reads student names and grades from `grades.txt`, computes the class average, classifies each student as pass/fail against a threshold entered at runtime, and writes the results to `result.txt`. Covers file I/O, functions, and basic data processing. |

## Running

```bash
python day2.py
# Prompts for a passing grade, then reads grades.txt and writes result.txt
```

## Why this repo exists

I use this as a changelog of what I'm learning — each new file is a step up
in scope (I/O → data processing → algorithms). Longer-term goal is to work
up to small ML/algorithm experiments as the series continues.
