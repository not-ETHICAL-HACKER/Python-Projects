import argparse
from core import encrypt, decrypt


def parse_args():
    parser = argparse.ArgumentParser(
        description="Caesar cipher encryption/decryption tool"
    )

    parser.add_argument(
        "mode",
        choices=["encrypt", "decrypt"],
        help="Operation to perform"
    )

    parser.add_argument(
        "text",
        help="Text to process"
    )

    parser.add_argument(
        "--shift",
        type=int,
        required=True,
        help="Shift value (integer)"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    if args.mode == "encrypt":
        result = encrypt(args.text, args.shift)
    else:
        result = decrypt(args.text, args.shift)

    print(result)


if __name__ == "__main__":
    main()
