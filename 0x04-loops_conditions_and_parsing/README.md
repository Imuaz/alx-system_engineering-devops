# 0x04. Loops, conditions and parsing:loop:

**INTRODUCTION**

The project covered several important topics related to shell scripting and command line usage. It included instructions on how to create SSH keys, highlighting their significance in secure communication. Additionally, it explained the advantages of using `#!/usr/bin/env bash` over `#!/bin/bash` as a shebang in shell scripts. The project also provided guidance on utilizing loop constructs such as `while`, `until`, and `for` loops for iterative operations. Furthermore, it covered conditional statements like `if`, `else`, `elif`, and `case`, enabling decision-making and branching in scripts. Moreover, the project included instructions on utilizing the `cut` command for extracting specific sections of text from files or outputs. Lastly, it explored various file-related operations and comparison operators, offering practical examples and guidance on their usage. Overall, the project aimed to provide a comprehensive understanding of shell scripting concepts and command line utilities.

## Resources:books:
***Read or watch:***
- [Loops sample](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html)
- [Variable assignment and arithmetic](https://tldp.org/LDP/abs/html/ops.html)
- [Comparison operators](https://tldp.org/LDP/abs/html/comparison-ops.html)
- [File test operators](https://tldp.org/LDP/abs/html/fto.html)
- [Make your scripts portable](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html)
- [data centers](https://youtu.be/iuqXFC_qIvA)

## Requirements:round_pushpin:
**General**
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A mandatory [README.md](./README.md) file, at the root of the folder of the project.
- All Bash script files must be executable
- is it not allowed to use `awk`
- the Bash script must pass `Shellcheck` (version `0.7.0`) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what is the script doing

## More Info:information_source:

**Shellcheck**
[Shellcheck](https://github.com/koalaman/shellcheck) is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. `Shellcheck` is your friend! **All your Bash scripts must pass Shellcheck without any error or you will not get any points on the task**.

`Shellcheck` is available on the school’s computers. If you want to use it on your own computer, here is how to [install it](https://github.com/koalaman/shellcheck#installing).

## Tasks:page_with_curl:

**0. Create a SSH RSA key pair**
- [0-RSA_public_key.pub](./0-RSA_public_key.pub). contains RSA public key
  - it can be achieved:
    - [Linux and Mac OS users](https://askubuntu.com/questions/61557/how-do-i-set-up-ssh-authentication-keys)
    - [Windows users](https://docs.rackspace.com/support/how-to/generating-rsa-keys-with-ssh-puttygen/)
    - ``man ssh-keygen``

**1. For Best School loop**
- [1-for_best_school](./1-for_best_school): Bash script that displays `Best School` 10 times.
  - it uses the `for` loop as required(`while` and `until` are forbidden)

**2. While Best School loop**
- [2-while_best_school](.2-while_best_school): Bash script that displays `Best School` 10 times.
  - it uses `while` loop as required(`for` and `until` are forbidden)

**3. Until Best School loop**
- [3-until_best_school](./3-until_best_school): Bash script that displays `Best School` 10 times.
  - it uses `until` loop (`for` and `while` are forbidden)

**4. If 9, say Hi!**
- [4-if_9_say_hi](./4-if_9_say_hi): Bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` and then `Hi` on a new line.
  - it uses `while` loop (`for` and `until are` forbidden)
  - uses the `if` statement

**5. 4 bad luck, 8 is your chance**
- [5-4_bad_luck_8_is_your_chance](./5-4_bad_luck_8_is_your_chance): Bash script that loops from 1 to 10 and:
  - it displays `bad luck` for the 4th loop iteration, `good luck` for the 8th loop iteration and `Best School` for the other iterations
  - it uses `while loop` (`for` and `until` are forbidden), uses the `if`, `elif` and `else` statements

**6. Superstitious numbers**
- [6-superstitious_numbers](./6-superstitious_numbers): Bash script that displays numbers from 1 to 20 and:
  - it displays `4` _and then_ `bad luck from China` for the 4th loop iteration, `9` _and then_ `bad luck from Japan` for the 9th loop iteration, and `17` _and then_ `bad luck from Italy` for the 17th loop iteration
  - it uses `while` loop (`for` and `until` are forbidden), and uses the `case` statement

**7. Clock**
- [7-clock](./7-clock): Bash script that displays the time for 12 hours and 59 minutes:
  - it display hours from 0 to 12 and minutes from 1 to 59
  - it uses `while` loop (`for` and `until` are forbidden)

**8. For ls**
- [8-for_ls](./8-for_ls): Bash script that displays:
  - The content of the current directory
  - In a list format
  - Where only the part of the name after the first dash is displayed
  - it uses `for` loop (`while` and `until` are forbidden)
  - Does not display hidden files

**9. To file, or not to file**
- [9-to_file_or_not_to_file](./9-to_file_or_not_to_file): Bash script that gives you information about the `school` file.
  - it uses `if` and, `else` (`case` is forbidden)
  - the script checks if the file exists and prints:
    - if the file exists: `school file exists`
    - if the file does not exist: `school file does not exist`
  - If the file exists,it prints:
    - if the file is empty: `school file is empty`
    - if the file is not empty: `school file is not empty`
    - if the file is a regular file: `school is a regular file`
    - if the file is not a regular file: (nothing)

**10. FizzBuzz**
- [10-fizzbuzz](./10-fizzbuzz): Bash script that displays numbers from 1 to 100.
  - It displays `FizzBuzz` when the number is a multiple of 3 and 5, `Fizz` when the number is multiple of 3 and displays `Buzz` when the number is a multiple of 5
  - Otherwise,it  displays the number 
  - In a list format

**11. Read and cut**
- [100-read_and_cut](./100-read_and_cut): Bash script that that displays the content of the file `/etc/passwd`.
  - it only displays:
    - username
    - user id
    - Home directory path for the user
  - it uses `while` loop (`for` and `until` are forbidden)

**12. Tell the story of passwd**
- For this taks read:
  - [IFS (internal field separator)](https://tldp.org/LDP/abs/html/internalvariables.html)
  - [Understanding /etc/passwd](https://www.cyberciti.biz/faq/understanding-etcpasswd-file-format/)
  - [previous project](../0x02-shell_redirections)
- [101-tell_the_story_of_passwd](./101-tell_the_story_of_passwd): Bash script that displays the content of the file `/etc/passwd`, using the `while` loop + IFS.
  - Format: `The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO`
  - it uses `while` loop (`for` and `until` are forbidden)

**13. Let's parse Apache logs**
- for this tasks, the following might be useful:
  - [Apache](https://en.m.wikipedia.org/wiki/Apache_HTTP_Server)
- [102-lets_parse_apache_logs](./102-lets_parse_apache_logs): Bash script that displays the visitor IP along with the [HTTP status code](https://en.m.wikipedia.org/wiki/List_of_HTTP_status_codes) from the Apache log file.
  - Format: IP HTTP_CODE
    - in a list format
    - it must use `awk`
  - it is not allowed to use `while`, `for`, `until` and `cut`
  - see example output:
  ```./102-lets_parse_apache_logs | tail -n 10
  185.130.5.207 301
  185.130.5.207 301
  91.224.140.223 200
  62.210.142.23 304
  92.222.20.166 304
  180.76.15.19 200
  2.1.201.36 304
  198.58.99.82 304
  50.116.30.23 304
  209.133.111.211 200
  ```

**14. Dig the data**
- [103-dig_the-data](./103-dig_the-data): Bash script that groups visitors by IP and HTTP status code, and displays this data using the previous task (`102-lets_parse_apache_logs`).
  - The exact format must be:
    - OCCURENCE_NUMBER IP <br> HTTP_CODE
    - In list format
  - Ordered from the greatest to the lowest number of occurrences
  - it uses `awk`
  - it is not allowed to use `while`, `for`, `until` and cut
  - see the example output:
  ```./103-dig_the-data | head -n 10
    141 130.0.236.153 200
    140 62.210.250.66 200
    117 103.243.26.232 404
    67 195.154.172.143 200
    60 78.154.190.29 200
    45 195.154.172.59 200
    41 62.210.248.185 200
    41 167.114.156.198 200
    36 2.1.201.36 304
    36 195.154.172.53 200
    ```

    :+1:
