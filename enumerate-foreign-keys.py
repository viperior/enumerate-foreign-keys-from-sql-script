import re

input_file_path = './in/input.sql'
output_file_path = './out/output.txt'

print('Enumerating foreign keys in script located at:')
print(input_file_path)

with open(input_file_path, 'r') as input_file:
    line_count = 0
    foreign_key_count = 0

    for line in input_file:
        clean_line = line.strip()
        regex = r'FOREIGN\sKEY'
        matches = re.findall(regex, clean_line)

        if(len(matches) > 0):
            foreign_key_count += 1

            with open(output_file_path, 'a') as output_file:
                output_file.write(clean_line + '\n')

        line_count += 1

print(str(line_count) + ' lines checked.')
print(str(foreign_key_count) + ' foreign keys found.')
print('Foreign key list written to ' + output_file_path)
