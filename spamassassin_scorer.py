import os

# iterate 157 times as we know there are 157 emails
for serial_number in range (1, 158):
    
    # boolean flag
    print_lines = False
    
    # setting indicators per iteration
    serial_number_string = str(serial_number)
    full_serial_number = 'S/N: ' + serial_number_string + '\n'
    next_serial_number = serial_number + 1
    next_serial_number_string = str(next_serial_number)
    full_next_serial_number = 'S/N: ' + next_serial_number_string + '\n'
    
    # open and read the parsed phishing-2020 text file
    with open('headers_phishing-test', 'r', encoding = 'utf8') as f:
        
        # open to append on an empty text file. Its temporary because we only want 1 email per text file to be sent to spamassassin since it can only do on one email at a time
        with open('temp_spamassassin', 'a', encoding = 'utf8') as ff:
            for line in f:
                if full_serial_number in line:
                    
                    # add serial number to output: spamassassin_scores
                    with open('spamassassin_scores', 'a', encoding = 'utf8') as fff:
                        fff.write(full_serial_number)
                        fff.close()
                    next(f)
                    
                    # set boolean flag to write out this email content only
                    print_lines = True

                elif line.startswith(full_next_serial_number):
                    print_lines = False

                if print_lines:
                    ff.write(line)
                    print(line)
            ff.close()
            
            # run the bash command from within python to execute Spamassassin and append to the serialized spamassassin_scores file
            os.system('spamassassin temp_spamassassin >> spamassassin_scores')
    
    # clears content of temp file to append again in next iteration
    with open('temp_spamassassin', 'w', encoding = 'utf8') as fff:
        fff.close()
    serial_number += 1

