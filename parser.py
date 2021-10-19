
import os
xuid = 1
with open('phishing-2020', 'r', encoding="utf8") as f:
    
    # boolean flag whether we want to printing lines or not
    print_lines = False 

    for line in f: 
        with open('headers_phishing-test', 'a', encoding="utf8") as ff:
            xuid_str = str(xuid)
            
            # find an indicator
            if line.startswith("From jose@monkey.org"):
                ff.write('S/N: %s\n' % xuid_str)
                
                # boolean flag to print
                print_lines = True 
                xuid += 1
                
                    
            if print_lines:
                ff.write(line)
                print(line)
                                
