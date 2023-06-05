# 0x13. Firewall
**Concepts**
- [Web stack debugging](../0x0F-load_balancer/concepts/web_stack_debug.md)

## Resources:books:
- [What is a firewall](https://en.m.wikipedia.org/wiki/Firewall_(computing)))
- [ufw redirects 8080/TCP to 80/TCP](https://www.cyberciti.biz/faq/how-to-configure-ufw-to-forward-port-80443-to-internal-server-hosted-on-lan/)

## Tasks:page_with_curl:
**0. Block all incoming traffic but**
- [0-block_all_incoming_traffic_but](./0-block_all_incoming_traffic_but): File contains `ufw` commands use to install and configure `ufw` so that it blocks all incoming traffic, except the following TCP ports:
  - `22` (SSH)
  - `443` (HTTPS SSL)
  - `80` (HTTP)

**1. Port forwarding**
- [100-port_forwarding](./100-port_forwarding): Configuration file (`/etc/ufw/ufw.conf`) of `ufw` modified to set up a web server in such a way that its firewall redirects port `8080/TCP` to port `80/TCP`.
