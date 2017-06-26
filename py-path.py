"""
	project............: efind-py-path
	description........: efind extension to filter files by extension and
                             mime-type.
	date...............: 06/2017
	copyright..........: Sebastian Fedrau

	Permission is hereby granted, free of charge, to any person obtaining
	a copy of this software and associated documentation files (the
	"Software"), to deal in the Software without restriction, including
	without limitation the rights to use, copy, modify, merge, publish,
	distribute, sublicense, and/or sell copies of the Software, and to
	permit persons to whom the Software is furnished to do so, subject to
	the following conditions:

	The above copyright notice and this permission notice shall be
	included in all copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
	EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
	MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
	IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
	OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
	ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
	OTHER DEALINGS IN THE SOFTWARE.
"""
import os
from mimetypes import MimeTypes

EXTENSION_NAME="py-path"
EXTENSION_VERSION="0.1.0"
EXTENSION_DESCRIPTION="Filter files by extension and mime-type."

MIME_TYPES=MimeTypes()

def get_ext(filename):
    _, ext = os.path.splitext(filename)

    return ext

def extension_equals(filename, extension):
    ext = get_ext(filename)

    if len(ext) > 0:
        return ext == extension

    return 0

extension_equals.__signature__=[str]

def extension_equals_icase(filename, extension):
    ext = get_ext(filename)

    if len(ext) > 0:
        return ext.lower() == extension.lower()

    return 0

extension_equals_icase.__signature__=[str]

def extension_in(filename, extensions):
    ext = get_ext(filename)
    l = extensions.split(',')

    return ext in map(str.strip, l)

extension_in.__signature__=[str]

def extension_in_icase(filename, extensions):
    ext = get_ext(filename)
    l = extensions.split(',')

    return ext.lower() in map(lambda s: s.strip().lower(), l)

extension_in_icase.__signature__=[str]

def mime_equals(filename, mime):
    global MIME_TYPES

    mime_type = MIME_TYPES.guess_type(filename)

    if not mime_type[0] is None:
        return mime == mime_type[0]

    return 0

mime_equals.__signature__=[str]

EXTENSION_EXPORT=[extension_equals, extension_equals_icase, extension_in, extension_in_icase, mime_equals]
