# fixes an Apache webser returning 500 error by fixing typo in wordpress
exec { 'fix typo':
  command     => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'],
}
