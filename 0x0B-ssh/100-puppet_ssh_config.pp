# set up client SSH configuration file
file { 'etc/ssh/ssh_config'
  ensure  => 'present',
  content => "
	      #SSH Client Configuartion
	      host *
	      IdentityFile ~/.ssh/school
	      PasswordAuthentication no
	      "
}
