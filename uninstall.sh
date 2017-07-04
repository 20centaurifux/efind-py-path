#!/bin/sh

echo "Removing extension from ~/.efind/extensions"

for f in py-path.py py-path.pyc; do
	rm -f ~/.efind/extensions/$f
done
