#  create a manifest that kills a process named killmenow

exec {'kill_a_process':
  command => 'pkill killmenow',
  path    => '/usr/bin/:/bin'
}
