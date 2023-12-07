# ccwc (coding challenge word count)
 
In this project, I built my own version of unix command line tool: __wc__

It is part one of the coding challenge: [Write Your Own wc Tool](https://codingchallenges.fyi/challenges/challenge-wc)

Written in : Python 

It can be used to get the word count, byte count, character count and line count of a given file.

## Commands available

- **Help**: display the command line options available

    `$ ccwc.py -h`


- **-c [file_name | stdin]**: displays the number of bytes in the given input file / standard input
    - With a file name:
  
      `$ ccwc.py -c test.txt`
    - With standard input:
  
      `cat test.txt | ccwc.py -c`


- **-l [file_name | stdin]**: displays the number of lines in the given input file / standard input
    - With a file name:
  
      `$ ccwc.py -l test.txt`
    - With standard input:
  
      `cat test.txt | ccwc.py -l`


- **-w [file_name | stdin]**: displays the number of words in the given input file / standard input
    - With a file name:
  
      `$ ccwc.py -w test.txt`
    - With standard input:
  
      `cat test.txt | ccwc.py -w`


- **-m [file_name | stdin]**: displays the characters in the given input file / standard input
    - With a file name:
  
      `$ ccwc.py -m test.txt`
    - With standard input:
  
      `cat test.txt | ccwc.py -m`


- **[file_name | stdin]**: no flags given, only a file name: displays the number of lines, number of bytes and number of characters
in the given input file / standard input
    - With a file name:
  
      `$ ccwc.py test.txt`
    - With standard input:
  
      `cat test.txt | ccwc.py`
