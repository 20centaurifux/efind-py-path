# efind-py-path

## Introduction

This extension for [efind](https://github.com/20centaurifux/efind) provides
functions to filter search results by file extension and mime-type.

## Available functions

### extension\_equals(string: extension)

Tests if the extension of the found file equals *extension*.

	$ efind . 'extension_equals(".txt") or extension_equals(".TXT")'

### extension\_equals(string: extension)

Tests if the extension of the found file equals *extension*. The
string comparison is case in-sensitive.

	$ efind . 'extension_equals_icase(".TxT")'

### extension\_in(string: extensions)

Tests if the comma-separated list *extensions* contains the file extension
of the found file.

	$ efind . 'extension_in(".c, .h")'

### extension\_in\_icase(string: extensions)

Tests if the comma-separated list *extensions* contains the file extension
of the found file. The string comparison is case-insensitive.

	$ efind . 'extension_in_icase(".cpp, .Hpp")'

### mime\_equals(string: mime-type)

Tests if the mime-type of the found file is equal to *mime-type*.

	$ efind . 'mime_equals("text/html") or mime_equals("text/plain")'

## Installation

Copy the Python script to *~/.efind/extensions* or run the *install.sh* shell script.
