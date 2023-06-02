# 0x10. HTTPS SSL:lock:
**Concepts**
- [DNS](../0x09-web_infrastructure_design/concepts/dns.md)
- [Web stack debugging](../0x0F-load_balancer/concepts/web_stack_debug.md)

**INTRODUCTION**
The project explored various aspects of HTTPS SSL, focusing on its roles and the purpose of encrypting traffic. It also delved into the concept of SSL termination and its significance. In summary, the project provided a comprehensive understanding of HTTPS SSL, its main roles, the importance of traffic encryption, and the meaning of SSL termination in secure communication.

## Resources:books:
***Read or watch:***
- [What are the 2 main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)
- [HAProxy SSL termination on Ubuntu16.04](https://docs.ionos.com/cloud/)
- [SSL termination](https://en.m.wikipedia.org/wiki/TLS_termination_proxy)
- [Bash function](https://tldp.org/LDP/abs/html/complexfunct.html)

***man or help:***
- `awk`
- `dig`

## Requirements:round_pushpin:
**General**
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A mandatory [README.md](./README.md) file, at the root of the folder of the project.
- All Bash script files must be executable
- The Bash script must pass `Shellcheck` (version `0.3.7`) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what is the script doing

## Tasks:page_with_curl:

**0. World wide web**
- [0-world_wide_web](./0-world_wide_web): Bash script that will display information about subdomains.
  - It accepts 2 arguments:
    - `domain`:
      1. type: string
      2. what: domain name to audit
      3. mandatory: yes
    - `subdomain`:
      1. type: string
      2. what: specific subdomain to audit
      3. mandatory: no
  - Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`
  - When only the parameter `domain` is provided, it displays information for its subdomains `www`, `lb-01`, `web-01` and `web-02` - in this specific order.
  - When passing `domain` and `subdomain` parameters, it displays information for the specified subdomain
  - It uses `awk` and atleast one Bash function.
  - it does not handle edge cases such as:
    - Empty parameters
    - Nonexistent domain names
    - Nonexistent subdomains

**1. HAproxy SSL termination**
- [1-haproxy_ssl_termination](./1-haproxy_ssl_termination): The HAproxy configuration file (`/etc/haproxy/haproxy.cfg`) version `1.5` or higher that sets up HAproxy for handling HTTPS traffic on port 443. It enables SSL/TLS encryption and specifies various settings such as the SSL certificate file, default timeouts, error pages, and other configuration options. Requests received on port 443 are directed to the appropriate backend based on specified ACLs and default_backend. It serves encrypted traffic and is specifically configured to return the root `/` of a web server. When accessing the root of the domain, the displayed page will include the name `Holberton School`.

**2. No loophole in your website traffic**
- [100-redirect_http_to_https](./100-redirect_http_to_https) HAproxy configuration file (`/etc/haproxy/haproxy.cfg`), set to provide a seamless and secure browsing experience for the user by transparently redirecting HTTP requests to HTTPS using a `301` status code. This configuration ensures that all traffic is encrypted and follows the appropriate redirection, enhancing the security and privacy of the user's browsing experience.

:+1:
