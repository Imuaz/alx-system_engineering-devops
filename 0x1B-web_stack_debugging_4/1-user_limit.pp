# Enable the user holberton to login and open files without error
file { '/etc/security/limits.conf':
  ensure  =>  present,
  content =>  template('module/limits.conf.erb'),
}

exec { 'increase-file-limits-for-holberton-user':
  command     =>  'sed -i "s/holberton hard nofile 5/holberton hard nofile\
  50000/g; s/holberton soft nofile 4/holberton \
  soft nofile 50000/g" /etc/security/limits.conf',
  path        =>  ['/usr/local/bin', '/bin'],
  refreshonly =>  true,
}
service { 'sshd':
  ensure  =>  running,
  require =>  Exec['increase-file-limits-for-holberton-user'],
}
