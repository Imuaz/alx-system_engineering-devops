# 0x14. MySQL:file_cabinet:

**INTRODUCTION**

The project covered several key aspects of databases, including their main role and the importance of database replicas. It explained the concept of a database replica and its purpose in ensuring data availability and fault tolerance. Additionally, the project emphasized the need to store database backups in different physical locations to mitigate risks such as hardware failures, natural disasters, or data corruption. It also highlighted the significance of regularly performing a verification operation to ensure the effectiveness of the database backup strategy. Overall, this project provided a comprehensive understanding of database management, replication, backup strategies, and risk mitigation.

**CONCEPTS**
- [Database administration](./concept/db_admin.md)
- [Web stack debugging](../0x0F-load_balancer/concepts/web_stack_debug.md)
- [{How to} Install mysql 5.7](./concept/mysql5_inst.md)

## Resources:books:
***Read or watch:***
- [What is a primary-replica cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)
- [MySQL primary replica setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)
- [Build a robust database backup strategy](https://www.databasejournal.com/ms-sql/developing-a-sql-server-backup-strategy/)

***man or help:***
- `mysqldump`

## Requirements:round_pushpin:
**General**
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A mandatory [README.md](./README.md) file, at the root of the folder of the project.
- All Bash script files must be executable
- The Bash script must pass `Shellcheck` (version `0.3.7-5~ubuntu16.04.1` via `apt-get`) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what is the script doing

## Tasks:page_with_curl:
**4. Setup a Primary-Replica infrastructure using MySQL**
- [4-mysql_configuration_primary](./4-mysql_configuration_primary): file contains the configuration for MySQL primary database.
- [4-mysql_configuration_replica](./4-mysql_configuration_replica): file contains the configuratio    n for MySQL replica database.

**5. MySQL backup**
- [5-mysql_backup](./5-mysql_backup):Bash script that generates a MySQL dump and creates a compressed archive out of it.
  - `backup.sql` is the name of MySQL dump
  - MySQL dump has been compressed to a `tar.gz` archive
  - the archive has the following name format: `day-month-year.tar.gz`
  - user to connect to the MySQL database should be `root`
- The Bash script accepts one argument that is the password used to connect to the MySQL database

:-1:
