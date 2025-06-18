#!/usr/bin/zsh
# This program is to download the valid html page 
# The valid html page is stored in a file called as output_dir

filename="exsist_url.txt"
output_dir="output_dir"
i=1

mkdir -p "$output_dir"

while read line
do
    curl -s "$line" > "$output_dir/output$i.html"
    (($i = $i + 1))
    sleep(2)
done < "$filename"