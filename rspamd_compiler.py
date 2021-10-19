serial_number = 1
while serial_number < 158:
    with open('rspamd_scores', 'r', encoding = 'utf8') as f:
        with open('rspamd_compiled_scores', 'w', encoding = 'utf8') as ff:
            for line in f:
                if 'Score:' in line:
                    aa = line[line.index(' '):11]
                    ff.write('%s:%s\n' %(serial_number, aa))
                    serial_number += 1
