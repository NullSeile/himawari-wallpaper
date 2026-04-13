import os
import sys
import subprocess

args = sys.argv

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

output = subprocess.check_output([
    'chafa',
    '--fit-width',
    '--scale', 'max',
    '-c', '16',
    '-f', 'symbols',
    '--glyph-file', 'PxPlus_IBM_VGA_8x16.ttf',
    '--symbols', 'imported',
    'lastest.png',
]).decode('utf-8')

# height = int(subprocess.check_output([
#     'tput', 'lines'
# ]))

height = int(args[2])

rows = output.split('\n')


if len(rows) > height:
    diff = len(rows) - height
    rows = rows[diff // 2:-diff // 2]

print('\n'.join(rows))
print(len(rows), height)
print(args)

