# Using Puppet, install flask from pip3

package { 'werkzeug':
  ensure   => '0.16.1',
  provider => 'pip3',
  require  => Package['flask'],
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  before   => Package['werkzeug']
}
