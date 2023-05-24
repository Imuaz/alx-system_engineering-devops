# 0x08. Networking basics #1:globe_with_meridians:

**INTRODUCTION**

The project covered various topics related to networking and system configuration. It included explanations of concepts such as localhost/127.0.0.1, 0.0.0.0, and /etc/hosts. The project also covered how to display the active network interfaces on a machine. Overall, it provided a comprehensive understanding of these networking and system configuration concepts.

## Resources:books:
***Read or watch:***
- [What is localhost](https://en.m.wikipedia.org/wiki/Localhost)
- [What is 0.0.0.0](https://en.m.wikipedia.org/wiki/0.0.0.0)
- [What is the hosts file](https://www.makeuseof.com/tag/modify-manage-hosts-file-linux/)
- [Netcat examples](https://www.thegeekstuff.com/2012/04/nc-command-examples/)

***man or help:***
- `ifconfig`
- `telnet`
- `nc`
- `cut`

## Requirements:round_pushpin:

**General**
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A mandatory [README.md](./README.md) file, at the root of the folder of the project.
- All Bash script files must be executable
- The Bash script must pass `Shellcheck` (version `0.7.0` via `apt-get`) without any errors
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what is the script doing

## Tasks:page_with_curl:

**0. Change your home IP**
- [0-change_your_home_IP](./0-change_your_home_IP): Bash script that configures an Ubuntu server with the below requirements.
  - `localhost` resolves to `127.0.0.2`
  - `facebook.com` resolves to `8.8.8.8.`
  - The checker is running on Docker, so make sure to read [this](http://blog.jonathanargentiero.com/docker-sed-cannot-rename-etcsedl8ysxl-device-or-resource-busy/)

**1. Show attached IPs**
- [1-show_attached_IPs](./1-show_attached_IPs): Bash script that displays all active IPv4 IPs on the machine it’s executed on.

**2. Port listening on localhost**
- [100-port_listening_on_localhost](./100-port_listening_on_localhost): Bash script that listens on port `98` on `localhost`.

    :+1:
