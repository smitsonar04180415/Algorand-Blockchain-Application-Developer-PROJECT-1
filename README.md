# Simple Blockchain

A very basic, beginner-friendly blockchain in plain Python (no dependencies).

## What it shows
- A **block** holds data, a timestamp, the previous block's hash, and its own hash.
- Blocks are **chained** by storing the previous block's hash.
- **Proof of work**: a block is only valid if its hash starts with N zeros.
- **Validation**: changing any old block breaks every hash after it.

## Run
```bash
python main.py
python -m unittest -v
```
