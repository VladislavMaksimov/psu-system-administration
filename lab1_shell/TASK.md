# Task 1. Shell scripts

1) The script counts the number of files in the tree and prints them in descending order of name length. The path to the root directory is passed to the script as an argument.
2) The script periodically deletes all temporary files in the tree. All actions are written to a file.

    Log record format:  
    date and time: deleted files

    For example:  
    02/15/09T21: 00: file1 file2 file3
    
    The path to the root directory and the filename extension are passed to the script as arguments.
3) The script prints numbers from 1 to a random number from 100 to 200. The script prints "Fizz" instead of numbers that are multiples of 3 and "Buzz" instead of numbers that are multiples of 5. If a number is multiple of 3 and 5 at one time the script prints "FizzBuzz".
4) The script transliterates names of subdirectories from Cyrillic to Latin. The path to the root directory is passed to the script as an argument.
5) The script converts the names of all the files in the directory to their md5 sum. The path to the root directory is passed to the script as an argument.
