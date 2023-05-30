#sets up nginx web server with puppet manifest

package { 'nginx':
  ensure   => installed,
  provider => 'apt',
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!\n',
}

exec { 'allow nginx':
  command => '/usr/sbin/ufw allow "Nginx HTTP"',
  unless  => '/usr/sbin/ufw status | grep "Nginx HTTP"',
}

file_line { 'redirect':
  path    => '/etc/nginx/sites-available/default',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  after   => 'root /var/www/html;',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}

