# 0x0D. Web stack debugging #0:briefcase:

**Background Context**

This is the first project in a series of web stack debugging projects. In these projects, a broken/bugged web stack is provided in isolated containers, and you are tasked with fixing the web stack to a working state. For each task, a script has been written to automate the commands necessary to fix the web stack.

**Concepts**
- [Network basics](../0x09-web_infrastructure_design/concepts/network_b.md)
- [Docker](./docker.md)
- [Web stack debugging](../0x0F-load_balancer/concepts/web_stack_debug.md)

## Resources:books:
***man or help***
- `curl`

## Requirements:round_pushpin:
**General**
- Allowed editors: `vi`, `vim`, `emacs`,
- All files will be interpreted on Ubuntu 14.04 LTS
- All files should end with a new line
- A mandatory [README.md](./README.md) file, at the root of the folder of the project.
- All Bash script files must be executable
- The Bash scripts must pass `Shellcheck` without any error
- The Bash scripts must run without error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what is the script doing

## Tasks:page_with_curl:
**0. Give me a page!**
- [0-give_me_a_page](./0-give_me_a_page): Bash script that runs [Apache](https://en.m.wikipedia.org/wiki/Apache_HTTP_Server) on a web server and gets to return a page containing `Hello Holberton` when querying the root of it (when curling port 80 returns a page containing `Hello Holberton`.

:+1:
