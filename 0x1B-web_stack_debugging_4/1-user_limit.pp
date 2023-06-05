# Enable the user holberton to login and open files without error
file { '/etc/security/limits.conf':
  ensure  =>  present,
  content =>  template('module/limits.conf.erb'),
}

exec { 'update-limits-for-holberton-user':
  command     =>  "sed -i -e 's/holberton soft nofile.*/holberton soft nofile \
  9000/' -e 's/holberton hard nofile.*/holberton hard nofile 9000/' \
  /etc/security/limits.conf",
  path        =>  '/usr/local/bin:/usr/bin:/bin',
  refreshonly =>  true,
  subscribe   =>  File['/etc/security/limits.conf'],
}
