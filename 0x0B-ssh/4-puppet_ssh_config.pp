# Puppet to make changes to our configuration file

file_line { 'add new config':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'update config':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    replace => 'PasswordAuthentication no'
}