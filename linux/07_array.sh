# indexed arrays
("" "" "")
# retrieving a variable in an array
${array[#]}
# return the whole array
${array[@]}

# assosiative arrays
# requires version 3 or 4
declare -A ${name}
${array}["${key]"}="value"
# no nested arrays :(