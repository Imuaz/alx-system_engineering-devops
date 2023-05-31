# 0x0F. Load balancer:traffic_light:

## Concepts
- **Load balancer**
Ever wonder how Facebook, Linkedin, Twitter and other web giants are handling such huge amounts of traffic? They don’t have just one server, but tens of thousands of them. In order to achieve this, web traffic needs to be distributed to these servers, and that is the role of a load-balancer.

![image]()

***Readme:***
  - [Load-balancing](https://www.thegeekstuff.com/2016/01/load-balancer-intro/)
  - [Load-balancing algorithms](https://community.f5.com/t5/technical-articles/intro-to-load-balancing-for-developers-the-algorithms/ta-p/273759)
  -[redundancy](https://en.m.wikipedia.org/wiki/Redundancy_(engineering))

- [Web stack debugging](./concepts/web_stack_debug.md)

## Resources:books:
***Read or watch:***
- [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HTTP header](https://www.techopedia.com/definition/27178/http-header)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)

## Requirements:round_pushpin:
**General**
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A mandatory [README.md](./README.md) file, at the root of the folder of the project.
- All Bash script files must be executable
- Bash script must pass `Shellcheck` (version `0.3.7`) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what is the script doing

## Tasks:page_with_curl:

**0. Double the number of webservers**
- [0-custom_http_response_header](./0-custom_http_response_header): Bash script that installs and configures Nginx on a server with a custom HTTP response header.
  - Contains a custom HTTP header named `X-Served-By`
  - the value of the HTTP header is the hostname of the server Nginx is running on
  
**1. Install your load balancer**
- [1-install_load_balancer](./1-install_load_balancer): Bash script that installs and configures HAproxy on a server.
  - Distributes requests using a roundrobin algorithm
  - It allows the HAproxy management via an init script
- [this tutorial](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-hostname.html) can be followed in other to configure the servers with a right hostnames.

**2. Add a custom HTTP header with Puppet**
- [2-puppet_custom_http_response_header.pp](./2-puppet_custom_http_response_header.pp): Puppet manifest that configures a brand new Ubuntu machine.
  - Creates a custom HTTP header response
  - The name of the custom HTTP header will be `X-Served-By`
  - The value of the custom HTTP header will be the hostname of the server Nginx is running on

:+1:
