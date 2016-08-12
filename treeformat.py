import argparse

def format_tree(text, open_identifier, close_identifier):
    lines = text.splitlines()
    output_lines = []
    curr_level = 0
    indent = 4
    for line in lines:
        if close_identifier in line:
            curr_level = max(0, curr_level - 1)

        output_lines.append("{ind}{line}".format(ind=(" " * curr_level * indent),
                                           line=line))

        if open_identifier in line:
            curr_level += 1

    return "\n".join(output_lines)

def main():

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('filename',
                        help='Input file')
    parser.add_argument('-o', '--open',
                        help='Opening identifier, e.g. "{"')
    parser.add_argument('-c', '--close',
                        help='Closing identifier, e.g. "}"')

    args = parser.parse_args()

    with open(args.filename, 'rb') as f:
        text = f.read()
    print(format_tree(text, args.open, args.close).encode('utf-8'))


if __name__ == "__main__":
    main()
