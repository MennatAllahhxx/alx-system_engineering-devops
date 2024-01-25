# login with the holberton user and open a file without any error message
exec { 'fix-hard-file':
    provider => shell,
    command  => 'sudo sed -i "s/5/50000/g" /etc/security/limits.conf'
}
exec { 'fix-soft-file':
    provider => shell,
    command  => 'sudo sed -i "s/4/50000/g" /etc/security/limits.conf'
}