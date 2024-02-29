# Using Puppet, install flask from pip3

package { 'flask':
  ensure   => latest,
  provider => 'pip3',
}
