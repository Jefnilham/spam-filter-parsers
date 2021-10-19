import os

for serial_number in range (1, 158):
    print_lines = False
    serial_number_string = str(serial_number)
    full_serial_number = 'S/N: ' + serial_number_string + '\n'
    next_serial_number = serial_number + 1
    next_serial_number_string = str(next_serial_number)
    full_next_serial_number = 'S/N: ' + next_serial_number_string + '\n'
    with open('headers_phishing-test', 'r', encoding = 'utf8') as f:
        with open('temp', 'a', encoding = 'utf8') as ff:
            for line in f:
                if full_serial_number in line:
                    with open('rspamd_scores', 'a', encoding = 'utf8') as fff:
                        fff.write(full_serial_number)
                        fff.close()
                    next(f)
                    print_lines = True

                elif line.startswith(full_next_serial_number):
                    print_lines = False

                if print_lines:
                    ff.write(line)
                    print(line)
            ff.close()
            os.system('rspamc < temp >> rspamd_scores')
    
    with open('temp', 'w', encoding = 'utf8') as fff:
        fff.close()
    serial_number += 1

