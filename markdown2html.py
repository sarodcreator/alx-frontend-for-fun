#!/usr/bin/python3

import sys
import os

def markdown_to_html(markdown_file, output_file):
    # This is where the conversion logic would go
    # For now, we'll just copy the content from the markdown to the output file
    with open(markdown_file, 'r') as md:
        content = md.read()

    with open(output_file, 'w') as html:
        html.write(content)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    markdown_to_html(markdown_file, output_file)
    sys.exit(0)

