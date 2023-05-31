# Use Puppet to automate the task of creating a custom HTTP header response

exec { 'update':
  command => '/usr/bin/apt-get update',
  logoutput => true,
}

package { 'nginx':
  ensure => 'installed',
  provider => 'apt',
  require => Exec['update'],
}

file { '/var/www/html/index.html':
  ensure => 'file',
  content => 'Hello World!',
}

exec { 'allow_nginx':
  command => '/usr/sbin/ufw allow "Nginx HTTP"',
  unless => '/usr/sbin/ufw status | grep "Nginx HTTP"',
}

file_line { 'redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  notify => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
