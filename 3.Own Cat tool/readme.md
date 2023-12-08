## 📝😺 CCCat - A Unix cat command line tool implementation

It is part of the coding challenge : 
**[https://codingchallenges.fyi/challenges/challenge-cat]()**

Written in: Python <img height="25px" width="22px" style="margin-bottom: -7px" src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png" width="20px"/>

It can be used to print the standard input contents or file contents to standard output.

### Options available:
* **Help** : displays the command line options available

       $ python3 cccat.py -h

* **-** : if - is given or no options is given input is taken from standard input.

       $ python3 cccat.py -
    or 

       $ head -n3 test.txt | python3 cccat.py 
* **filename(s)** : displays the contents of the given file(s) to standard output.
  
       $ python3 cccat.py test.txt 
    or

       $ python3 cccat.py test.txt test2.txt
* **-n** : displays the line numbers before each line.

       $ python3 cccat.py -n test.txt

* **-b** : displays the line numbers before each line excluding empty lines.
    
       $ python3 cccat.py -b test.txt
