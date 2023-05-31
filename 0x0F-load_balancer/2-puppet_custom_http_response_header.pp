# Use Puppet to automate the task of creating a custom HTTP header response

exec { 'update':
  command => '/usr/bin/apt-get update',
  logoutput => true,
}

package { 'nginx':
  ensure => present,
  require => Exec['update'],
}

file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => 'add_header X-Served-By "%{::hostname}";',
  match => '^http {',
  notify => Exec['run'],
}

exec { 'run':
  command => '/usr/sbin/service nginx restart',
  refreshonly => true,
}
