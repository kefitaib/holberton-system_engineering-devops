# Puppet to make changes to our configuration file

file_line { 'add new config':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/holberton',
}