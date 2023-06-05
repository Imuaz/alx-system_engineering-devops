# Enable the user holberton to login and open files without error
package { 'augeas-tools':
  ensure =>  installed,
}

augeas { 'increase-file-limits-for-holberton-user':
  incl    =>  '/etc/security/limits.conf',
  lens    =>  'Limits.lns',
  changes =>  [
    "set *[self::user = 'holberton']/hard '50000'",
    "set *[self::user = 'holberton']/soft '50000'",
  ],
  notify  =>  Exec['reload-systemd'],
}

exec { 'reload-systemd':
  command     =>  'systemctl daemon-reload',
  refreshonly =>  true,
}
