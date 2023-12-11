## 📝✂️ CCCut - A Unix cut command line tool implementation

It is part of the coding challenge : 
**[https://codingchallenges.fyi/challenges/challenge-cut](https://codingchallenges.fyi/challenges/challenge-cat)**

Written in: Python <img height="25px" width="22px" style="margin-bottom: -7px" src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png" width="20px"/>

It can be used to print the standard input contents or file contents to standard output.

### Options available:
* **Help** : displays the command line options available

       $ python3 cccut.py -h

* **-** : if - is given or no options is given input is taken from standard input.

       $ python3 cccut.py -f1 -
    or 

       $ head -n3 test.txt | python3 cccut.py 
* **-f1(s)** : displays the contents of the given column of each row to standard output.Here first field (1).
  
       $ python3 cccut.py -f1 sample.tsv 
    or

       $ python3 cccut.py -f2 test1.tsv test2.tsv
* **-d** : use this flag to give a custom delimiter, default is 'tab'

       $ python3 cccut.py -f1 -d, fourchords.csv

* **-f"1,2" or -f"1 2"** : displays the column(s) from 1 to 2 for each row.
    
       $ python3 cccut.py -f1,2 sample.tsv
    or

       $ python3 cccut.py -f"1 2" sample.tsv
