Design a Python program that reads a text file line by line and logs all
file-related operations using Python’s logging mechanism.


The program should attempt to open and read a text file provided by the user.

Each major operation (file access, file read start, and completion) must be logged.

While reading the file:

Count the total number of lines.

Detect and count empty lines.

Log a warning whenever an empty line is encountered.

Log the content of non-empty lines with line numbers.

After processing the file:

Log the total number of lines read.

Log the total number of empty lines found.

If the file does not exist:

Log an error indicating the file was not found.

If any unexpected error occurs during execution:

Log a critical message along with exception details.