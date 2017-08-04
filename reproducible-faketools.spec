#
# spec file for package reproducible-faketools
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           reproducible-faketools
Version:        0.3.9
Release:        0
Summary:        Fake system tools for reproducible builds
License:        MIT
Group:          Development/Tools/Other
Url:            https://github.com/bmwiedemann/reproducible-faketools
Source0:        %{name}-%{version}.tar.xz
Requires:       hostname
Requires:       coreutils
BuildArch:      noarch

%description
These tools are meant to help with reproducible builds.
This works by masking standard UNIX tools in build environments
with versions that give more predictable output when $SOURCE_DATE_EPOCH
is set but just redirect to the normal version otherwise.

%prep
%setup

%build

%install
%makeinstall

%package hostname
Summary:  replacement hostname
Requires: reproducible-faketools
%description hostname
a script to enhance the reproducibility of the output of hostname
%files hostname
%defattr(-, root, root, 0755)
/usr/local/bin/hostname
/usr/local/bin/uname


%package date
Summary:  replacement date
Requires: reproducible-faketools
%description date
a script to enhance the reproducibility of the output of date
%files date
%defattr(-, root, root, 0755)
/usr/local/bin/date


%package ar
Summary:  replacement ar
Requires: reproducible-faketools
%description ar
a script to enhance the reproducibility of the output of ar
%files ar
%defattr(-, root, root, 0755)
/usr/local/bin/ar
/usr/local/bin/strip

%package tar
Summary:  replacement tar
Requires: reproducible-faketools
Requires: tar >= 1.28
%description tar
a script to enhance the reproducibility of the output of tar
by adding --sort and --mtime options
%files tar
%defattr(-, root, root, 0755)
/usr/local/bin/gzip
/usr/local/bin/tar

%package ant
Summary:  replacement ant
Requires: reproducible-faketools
Requires: strip-nondeterminism
%description ant
a script to enhance the reproducibility of the output of ant
%files ant
%defattr(-, root, root, 0755)
/usr/local/bin/ant

%package filesys
Summary:  sorted filesystem
Requires: disorderfs
%description filesys
a script to make sure readdir on filesystems is always sorted during build
WARNING: do not use outside OBS or osc build --vm-type=kvm
%files filesys
%defattr(-, root, root, 0755)
/etc/profile.d/disorderfs.sh
%post filesys
chmod 4755 /usr/bin/fusermount || :
mknod /dev/fuse c 10 229 || :

%package zip
Summary:  replacement zip
Requires: p7zip
Requires: perl
Requires: reproducible-faketools
%description zip
a script to enhance the reproducibility of the output of zip
by replacing it with a wrapper to 7z
%files zip
%defattr(-, root, root, 0755)
/usr/local/bin/zip
/usr/local/bin/reproducible-zip.pl

%package faketime
Summary:  fake time via LD_PRELOAD
RemovePathPostfixes: -faketime
Requires: libfaketime
Requires: reproducible-faketools
%description faketime
a script to enhance the reproducibility of the output
by replacing time(2) and fstat(2) library calls to return our notion of time
%files faketime
%defattr(-, root, root, 0755)
/usr/local/bin/rpmbuild-faketime

%package strace
Summary:  run build with strace
RemovePathPostfixes: -strace
Requires: strace
Conflicts: reproducible-faketools-faketime
%description strace
a script to facilitate the debugging of reproducibility issues
by running rpmbuild with strace to find how files are created
%files strace
%defattr(-, root, root, 0755)
/usr/local/bin/rpmbuild-strace

%files
%defattr(-, root, root, 0755)
%license LICENSE.md
%doc README.md
/usr/local/lib/%{name}*

%changelog
