# 0x0E. Web stack debugging #1:briefcase:
**Background Context**

This is the second project in a series of web stack debugging projects. In these projects, a broken/bugged web stack is provided in isolated containers, and you are tasked with fixing the web stack to a working state. For each task, a script has been written to automate the commands necessary to fix the web stack.

**Concepts**
- [Network basics](../0x09-web_infrastructure_design/concepts/network_b.md)
- [Web stack debugging](../0x0F-load_balancer/concepts/web_stack_debug.md)

## Requirements:round_pushpin:
- [General](../0x0D-web_stack_debugging_0/README.md#Requirements)

## Tasks:page_with_curl:
**0. Nginx likes port 80**
- [0-nginx_likes_port_80](./0-nginx_likes_port_80): Bash script that configures an Nginx web server to run and listen on port 80 for all active IPv4 IPs of the server.

**1. Make it sweet and short**
- [1-debugging_made_short](./1-debugging_made_short): A a concise Bash script based on `0-nginx_likes_port_80`, limited to 5 lines or fewer, which adheres to standard Bash script requirements while avoiding certain commands (`;`, `&&`, `wget`). It ensures that there is a newline at the end of the file.

:-1:
