#  Puppet, install flask from pip3

package {'flask':
  ensure   => '2.1.0',
  provider => pip3,
  before   => Package['werkzeug']
}

package {'werkzeug':
  ensure   => '2.1.1',
  provider => pip3,
  require  => Package['flask']
}
