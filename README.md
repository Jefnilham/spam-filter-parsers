# spam-filter-parsers
Helps user parse emails from jose's phishing emails data set

parser.py helps to insert a serial number at the beginning of each email in a data set. This serial number is taken from the X-UID of the email in the data set.

spamassassin_scorer.py creates a temporary file to store an email from the data set. The temporary file is then passed to spamassassin to check for spam. The temporary file is then cleared for the next iteration in a loop and every spamassassin output is appended to the first output, giving a compiled text file. This was done as spamassassin can only check one email at a time.

spamassassin_compiler simply compiles spam-scores of each email to be used for data manipulations e.g. checking against other spam filters.
