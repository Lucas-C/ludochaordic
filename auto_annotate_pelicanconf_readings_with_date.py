#!/usr/bin/env python
from os import chdir, path
from subprocess import check_output
try:  # Optional dependency:
    from tqdm import tqdm
except ImportError:
    tqdm = lambda _: _

TARGET_FILE = 'pelicanconf.py'

chdir(path.dirname(path.realpath(__file__)))

with open(TARGET_FILE) as target_file:
    file_lines = target_file.readlines()
readings_start_line = next(i for i, s in enumerate(file_lines) if s == 'READINGS = (\n')
readings_end_line = next(i for i, s in enumerate(file_lines) if s == ')  # ends READINGS\n')
new_readings_lines = []
for readings_line in tqdm(file_lines[readings_start_line+1:readings_end_line]):
    reading_dict = eval(readings_line)[0]
    reading_dict['date'] = check_output(('git', 'log', '-S', reading_dict['img_url'], '--pretty=%cd', '--date=short', '--', TARGET_FILE)).decode().strip()
    new_readings_lines.append('    {},\n'.format(reading_dict))
# Now replacing lines in original file:
file_lines[readings_start_line+1:readings_end_line] = new_readings_lines
with open(TARGET_FILE, 'w') as target_file:
    target_file.write(''.join(file_lines))
