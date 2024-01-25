# login with the holberton user and open a file without any error message
exec { 'fix-hard-file':
    provider => shell,
    command  => 'sudo sed -i "/holberton hard/s/5/50000" /etc/security/limits.conf'
}
exec { 'fix-soft-file':
    provider => shell,
    command  => 'sudo sed -i "/holberton soft/s/4/50000" /etc/security/limits.conf'
}