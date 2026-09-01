# Caesar Cipher

Version: v1 (13/12/2025)

## Description

A Python implementation of the Caesar cipher that supports:

- Uppercase and lowercase letters
- Arbitrary positive and negative shifts
- Proper wraparound (Z → A)
- Non-letter characters preserved

## Usage

### Encrypt

```bash
python cli.py encrypt "Hello, World!" --shift 3
