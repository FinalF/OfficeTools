
#!/bin/bash

#use this script for downloading websites using 'wget' utility
# replace URL field with the URL to be downloaded

URL="$1"


wget  --no-directories   --accept=iso,jpg,jpeg --no-parent -Nrpl 0 $URL 
# wget flags and their functions
# -r = recursive: follows the links
# -k = changes links adresses to their local file adress
# -p = downloads images
# -l = recursion level. 0 for infinite.

exit
