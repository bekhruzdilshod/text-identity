# Copyright © 2021 Bekhruz Iskandarzoda. All rights reserved.

import argparse
import difflib
import colorama
import textract

colorama.init()


def out_red(text):
    print(f"{colorama.Fore.RED}{colorama.Style.BRIGHT}{text}")


def out_yellow(text):
    print(f"{colorama.Fore.YELLOW}{colorama.Style.BRIGHT}{text}")


def out_green(text):
    print(f"{colorama.Fore.GREEN}{colorama.Style.BRIGHT}{text}")


def validate_files(first_file: str, second_file: str):
    if first_file and second_file:
        return True
    else:
        return False


def identity_percent(first_file: str, second_file: str):
    # import docx
    import textract

    first_text = textract.process(f"./{first_file}")
    second_text = textract.process(f"./{second_file}")

    result = difflib.SequenceMatcher(None, first_text, second_text)
    ratio = round(result.ratio() * 100, 2)
    if ratio > 75:
        out_green(f"Identity percent between two files: {ratio}%")
    elif ratio > 50:
        out_yellow(f"Identity percent between two files: {ratio}%")
    else:
        out_red(f"Identity percent between two files: {ratio}%")


parser = argparse.ArgumentParser(description="Script helps you to get a percent of two texts matching.")
parser.add_argument('-first', type=str, help="First file path")
parser.add_argument('-second', type=str, help='Second file path')

args = parser.parse_args()

# Validation each file
if validate_files(args.first, args.second):
    identity_percent(args.first, args.second)