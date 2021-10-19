serial_number = 1
while serial_number < 158:
    with open('spamassassin_scores', 'r', encoding = 'utf8') as f:
        with open('spamassassin_compiled_scores', 'w', encoding = 'utf8') as ff:
            for line in f:
                if 'X-Spam-Status' in line:
                    aa = line[line.index('='):line.index('required')]
                    aa = aa[1:]
                    ff.write('%s: %s\n' %(serial_number, aa))
                    serial_number += 1
