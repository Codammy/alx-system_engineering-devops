# Configuration management

`DevOps`
`SysAdmin`
`Scripting`
`CI/CD`

**Use puppet and save your futureself! right now in the present.**

## Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

## Install puppet
```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```
You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

[Puppet 5 Docs](https://www.puppet.com/docs/puppet/5.5/puppet_index.html)

**Install** puppet-lint
`$ gem install puppet-lint`
