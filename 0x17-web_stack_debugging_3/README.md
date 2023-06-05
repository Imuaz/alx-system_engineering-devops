# 0x17. Web stack debugging #3:briefcase:
**Concepts**
- [Web Server](../0x09-web_infrastructure_design/concepts/web_server.md)
- [Web stack debugging](../0x0F-load_balancer/concepts/web_stack_debug.md)

When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites… It [actually powers 26% of the web](https://managewp.com/blog/statistics-about-wordpress-usage), so there is a fair chance that you will end up working with it at some point in your career.

Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

The web stack we debug today is a Wordpress website running on a LAMP stack.

## Requirements:round_pushpin:
**General**
- All files will be interpreted on Ubuntu 14.04 LTS
- All files should end with a new line
- A mandatory [README.md](./README.md) file at the root of the folder of the project.
- The Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors
- The Puppet manifests must run without error
- The Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- The Puppet manifests files must end with the extension `.pp`
- Files will be checked with Puppet v3.4

## More Info:information_source:
**Install** `puppet-lint`
```
apt-get install -y ruby
```
```
gem install puppet-lint -v 2.1.1
```
## Tasks:page_with_curl:
- [0-strace_is_your_friend.pp](./0-strace_is_your_friend.pp): Puppet manifest designed to rectify an issue where Apache is returning a 500 error while serving a WordPress application. The manifest includes the necessary instructions and configurations to troubleshoot and resolve the error, ensuring that the Apache server functions correctly and serves the WordPress application without encountering the 500 error.

:+1:
