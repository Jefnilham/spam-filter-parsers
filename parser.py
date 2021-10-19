
import os
xuid = 1

with open('phishing-2020', 'r', encoding="utf8") as f:

    print_lines = False # Boolean state variable to keep track of whether we want to be printing lines or not

    for line in f:
        
        with open('headers_phishing-test', 'a', encoding="utf8") as ff:
            xuid_str = str(xuid)
            
            if line.startswith("From jose@monkey.org"):
                ff.write('S/N: %s\n' % xuid_str)
                print_lines = True # We have found an @ so we can start printing lines
                xuid += 1
                
                    
            if print_lines:
                ff.write(line)
                print(line)
                                
