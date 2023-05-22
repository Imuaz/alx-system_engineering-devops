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
