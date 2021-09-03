# built-ins can be found in the bash man pages
builtin {}
# commands are not part of bash
command {}
# see if built-in or command
command -V 
# built-ins take precedence over commands
# this will disable the built-in
enable -n {built-in}
# show built-ins 
help
