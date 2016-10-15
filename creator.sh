#!/bin/sh
file_name=$1.py

echo '#!/usr/bin/env python3' > $file_name
echo '' >> $file_name

cat >> $file_name

chmod u+x $file_name

atom $file_name
