import argparse


def main():
    parser = argparse.ArgumentParser(description="Pastedev client")
    parser.add_argument('--apply', nargs='*',
                        help="Apply <change_id> to <file>")
    parser.add_argument('--diff', nargs='*',
                        help="Diff of <change_id> and <file>")
    args = parser.parse_args()

    file_apply = args.apply
    diff = args.diff

    print file_apply, diff
