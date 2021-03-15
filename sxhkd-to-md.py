import argparse
from os.path import expanduser

home = expanduser("~")
defaultPath = f'{home}/.config/sxhkd/sxhkdrc'
defaultOut = f'{home}/sxhkd-keybidings.md'

parser = argparse.ArgumentParser("sxhkd-to-md")
parser.add_argument(
    "--path", help=f"Specify path to sxhkdrc (default is {defaultPath})", default=defaultPath)
parser.add_argument(
    "--out", help=f"Where the markdown will be saved (default is {defaultOut})", default=defaultOut)
args = parser.parse_args()


def line_to_md(line, last_line):
    if(last_line.startswith('#') and line.startswith('#') and len(line) > 2):
        return f"\n## {line.replace('#', '')}\nDescription | Key | Command\n------------ | ------------- | -------------\n"
    if line.startswith('#') and len(line) > 2:
        line = line.replace('#', '').strip()
        return f'{line} | '
    if line.startswith('\t'):
        line = line.replace('\t', '').strip()
        return f'{line} \n'
    if(len(line.strip()) > 1):
        line = line.strip()
        return f'{line} | '
    return ''


with open(args.path) as f:
    content = f.readlines()
    md = '# Sxhkd keybindings\n\n'
    last_line = ''
    for line in content:
        md += line_to_md(line, last_line)
        last_line = line
    md_file = open(args.out, 'w')
    md_file.write(md)
    print(f"File successfully saved on {args.out}!")
