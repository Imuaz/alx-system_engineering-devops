# 0x0A. Configuration management:wrench:

## Resources:books:
***Read or watch:***
- [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management0)
- [Puppet resource type: file](https://www.puppet.com/docs/puppet/5.5/types/file.html) (check “Resource types” for all manifest types in the left menu)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](https://www.puppet.com/blog)
- [Puppet lint](http://puppet-lint.com/)
- [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)

## Requirements:round_pushpin:
**General**
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A mandatory [README.md](./README.md) file at the root of the folder of the project
- The Puppet manifests must `pass puppet-lint` version 2.1.1 without any errors
- The Puppet manifests must run without error
- The Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- The Puppet manifests files must end with the extension `.pp`

## Tasks:page_with_curl:
**0. Create a file**
- [0-create_a_file.pp](./0-create_a_file.pp): Puppet manifest that creates a file in `/tmp`.
  - `/tmp/school` is the file path
  - `0744` is the file permission
  - `www-data` the file owner
  - `www-data` the file group
  - the file contains `I love Puppet`

**1. Install a package**
- [1-install_a_package.pp](./1-install_a_package.pp): Puppet manifest that installs `flask` version `2.1.0` from `pip3`.

**2. Execute a command**
- [2-execute_a_command.pp](./2-execute_a_command.pp): Puppet manifest that kills a process named `killmenow`.
  - it uses `exec` Puppet resource
  - it uses `pkill`
  
  :+1:
