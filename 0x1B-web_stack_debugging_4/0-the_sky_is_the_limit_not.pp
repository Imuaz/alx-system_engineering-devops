# Increases the amount of traffic an Nginx server can handle.
# Increase the ULIMIT of the default file
exec { 'fix-for-nginx':
command => 'sed -i "s/15/4096/" /etc/default/nginx',
path    => ['/usr/local/bin', '/bin'],
notify  => Exec['nginx-restart']
}

# Restart Nginx
exec { 'nginx-restart':
command     => '/etc/init.d/nginx restart',
path        => ['/usr/local/sbin', '/usr/local/bin', '/sbin', '/bin', '/usr/sbin', '/usr/bin'],
refreshonly =>  true
}
