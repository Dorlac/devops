# should use lowercase variable names
 # test 0 for success 1 for failure
[]
# run commands conditionally
[[ ${statement} ]]; ${command}
# same for 
${command_one}; ${command_two}
# or
${command_one} && ${command_two}
# booleans
true and false
# regular expression matching
[[ "${string}" =~ ${regularexpression} ]]
# testing is better
