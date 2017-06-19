# efind-py-path

## Introduction

This extension for [efind](https://github.com/20centaurifux/efind) provides
functions to filter search results by file extension and mime-type.

## Available functions

### ext\_equals(string: extension)

Tests if the extension of the found file equals *extension*.

	$ efind . 'ext_equals(".txt") or ext_equals(".TXT")'

### ext\_equals(string: extension)

Tests if the extension of the found file equals *extension*. The
string comparison is case in-sensitive.

	$ efind . 'ext_equals_icase(".TxT")'

### ext\_in(string: extensions)

Tests if the comma-separated list *extensions* contains the file extension
of the found file.

	$ efind . 'ext_in(".c, .h")'

### ext\_in_icase(string: extensions)

Tests if the comma-separated list *extensions* contains the file extension
of the found file. The string comparison is case-insensitive.

	$ efind . 'ext_in(".cpp, .Hpp")'

### mime_equals(string: mime-type)

Tests if the mime-type of the found file is equal to *mime-type*.

	$ efind . 'mime_equals("text/html") or mime_equals("text/plain")'

## Installation

Copy the Python script to *~/.efind/extensions*.
