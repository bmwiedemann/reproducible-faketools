#!/bin/sh
(
exec >/dev/null
exec 2>&1
if [ -e /home/abuild/rpmbuild/BUILD ] && ! [ -e /home/abuild/rpmbuild/BUILD.unsorted ] ; then
	mv /home/abuild/rpmbuild/BUILD /home/abuild/rpmbuild/BUILD.unsorted
	mkdir /home/abuild/rpmbuild/BUILD
	# needs chmod 4755 /usr/bin/fusermount
	# and mknod /dev/fuse c 10 229
	disorderfs --sort-dirents=yes --reverse-dirents=no /home/abuild/rpmbuild/BUILD.unsorted /home/abuild/rpmbuild/BUILD
fi
)
