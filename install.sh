#!/bin/sh

echo "Copying extension to ~/.efind/extensions"

mkdir -p ~/.efind/extensions && \
cp ./py-path.py ~/.efind/extensions/
