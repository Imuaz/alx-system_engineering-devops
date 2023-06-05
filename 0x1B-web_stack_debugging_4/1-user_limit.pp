# Enable the user holberton to login and open files without error
exec {'Updating limits to Holberton User':
  command  => "sed -i 's/holberton soft nofile.*/holberton soft nofile 9000/' /etc/security/limits.conf",
  provider => shell
}
exec {'Updating limit to Holberton User':
  command  => "sed -i 's/holberton hard nofile.*/holberton hard nofile 9000/' /etc/security/limits.conf",
  provider => shell
}
