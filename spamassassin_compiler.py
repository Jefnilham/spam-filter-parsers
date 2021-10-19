serial_number = 1
while serial_number < 158:
    with open('spamassassin_scores', 'r', encoding = 'utf8') as f:
        with open('spamassassin_compiled_scores', 'w', encoding = 'utf8') as ff:
            for line in f:
                
                # find a match from spamassassin_scores file
                if 'X-Spam-Status' in line:
                    
                    # if found, take only the score
                    aa = line[line.index('='):line.index('required')]
                    aa = aa[1:]
                    ff.write('%s: %s\n' %(serial_number, aa))
                    serial_number += 1
