# 0x0B. SSH:shell:
**INTRODUCTION**

This project covered several key topics related to servers and SSH. It began with an explanation of what a server is and where servers are typically located. It then delved into SSH (Secure Shell) and provided instructions on how to create an SSH RSA key pair. Additionally, it covered the process of connecting to a remote host using an SSH RSA key pair. Lastly, the project discussed the advantages of using `#!/usr/bin/env bash` instead of `/bin/bash` in scripts. Overall, the project provided a comprehensive understanding of servers, SSH, and the usage of SSH RSA key pairs for secure remote connections.

## Resources:books:
***Read or watch:***
- [What is a (physical) server - text](https://en.m.wikipedia.org/wiki/Server_(computing)#Hardware_requirement)
- [What is a (physical) server - video](https://youtu.be/B1ANfsDyjeA)
- [SSH essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
- [SSH Config File](https://www.ssh.com/academy/ssh/config)
- [Public Key Authentication for SSH](https://www.ssh.com/academy/ssh/public-key-authentication)
- [How Secure Shell Works](https://youtu.be/ORcvSkgdA58)
- [SSH Crash Course](https://youtu.be/hQWRp-FdTpc)(Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)

***For reference:***
- [Understanding the SSH Encryption and Connection Process](https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process)
- [Secure Shell Wiki](https://en.m.wikipedia.org/wiki/Secure_Shell)
- [IETF RFC 4251 (Description of the SSH Protocol)](https://www.ietf.org/rfc/rfc4251.txt)
- [Internet Engineering Task Force](https://en.m.wikipedia.org/wiki/Internet_Engineering_Task_Force)
- [Request for Comments](https://en.m.wikipedia.org/wiki/Request_for_Comments)

***man or help:***
- `ssh`
- `ssh-keygen`
- `env`

## Requirements:round_pushpin:
**General**
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A mandatory [README.md](./README.md) file, at the root of the folder of the project.
- All Bash script files must be executable
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what is the script doing

## Tasks:page_with_curl:

**0. Use a private key**
- [0-use_a_private_key](./0-use_a_private_key): Bash script that `ssh` to connect to my server using the private key `~/.ssh/school` with the user `ubuntu`.
  - It only uses `ssh` single-character flags
  - does not use `-l`
  - no need to handle the case of a private key protected by a passphrase

**1. Create an SSH key pair**
- [1-create_ssh_key_pair](./1-create_ssh_key_pair): Bash script that creates an RSA key pair.
  - `school` is the name of the created private key
  - 4096 is the number of bits in the created key to be created
  - The created key will be protected by the passphrase `betty`

**2. Client configuration file**
- [2-ssh_config](./2-ssh_config): The SSH configuration file sets to use the private key `~/.ssh/school` for authentication without requiring a password.

**3. Let me in!**
- An SSH public key added to the server to grant access permissions.

**4. Client configuration file (w/ Puppet)**
- [100-puppet_ssh_config.pp](./100-puppet_ssh_config.pp): The SSH configuration file sets to use the private key `~/.ssh/school` for authentication without requiring a password using Puppet.

    :+1:
