#!/bin/bash/
# home directory
echo ~
# Brace expansion
# {01..10} or c{a,o,u}t
# nested brace expansion
# {}{}
# parameter expansion
# ${} or $
LIST="this is my list"
echo "one two" {$LIST} "three"
# bash man pages
man bash
# search
/
# command substitution, runs this command in a subshell and returns it to the shell
$()
# arithmetic expansion
$(())
