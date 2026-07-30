#
# spec file for package reproducible-faketools
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           reproducible-faketools
Version:        set-by-service-from-git-tag
Release:        0
Summary:        Fake system tools for reproducible builds
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/bmwiedemann/reproducible-faketools
Source0:        %{name}-%{version}.tar
Requires:       bash
Requires:       coreutils
Requires:       this-is-only-for-build-envs
BuildArch:      noarch

%description
These tools are meant to help with reproducible builds.
This works by masking standard UNIX tools in build environments
with versions that give more predictable output when $SOURCE_DATE_EPOCH
is set but just redirect to the normal version otherwise.

%prep
%autosetup -p1

%build
echo dummy file because an rpm cannot be empty > README.random

%install
%make_install

%check
make test

%package hostname
Summary:        Replacement hostname + uname
Requires:       hostname
Requires:       reproducible-faketools
%description hostname
a script to enhance the reproducibility of the output of hostname
%files hostname
/usr/local/bin/hostname
/usr/local/bin/uname

%package date
Summary:        Replacement date
Requires:       reproducible-faketools
%description date
a script to enhance the reproducibility of the output of date
%files date
/usr/local/bin/date

%package find
Summary:        Replacement find
Requires:       reproducible-faketools
%description find
a script to enhance the reproducibility of the output of find
%files find
/usr/local/bin/find

%package ar
Summary:        Replacement ar
Requires:       reproducible-faketools
%description ar
a script to enhance the reproducibility of the output of ar
%files ar
/usr/local/bin/ar
/usr/local/bin/strip

%package tar
Summary:        Replacement tar + gzip
Requires:       reproducible-faketools
Requires:       tar >= 1.28
%description tar
a script to enhance the reproducibility of the output of tar
by adding --sort and --mtime options
%files tar
/usr/local/bin/gzip
/usr/local/bin/tar

%package ant
Summary:        Replacement ant
Requires:       reproducible-faketools
Requires:       strip-nondeterminism
%description ant
a script to enhance the reproducibility of the output of ant
%files ant
/usr/local/bin/ant

%package strip-nondeterminism
Summary:        Run strip-nondeterminism after build
Requires:       reproducible-faketools
Requires:       strip-nondeterminism
%description strip-nondeterminism
enhance the reproducibility of various file formats
with strip-nondeterminism
%files strip-nondeterminism
/usr/lib/rpm/brp-suse.d/brp-95-strip-nondeterminism

%package filesys
Summary:        Sorted filesystem
Requires:       disorderfs
Requires:       reproducible-faketools
%description filesys
a script to make sure readdir on filesystems is always sorted during build
WARNING: do not use outside OBS or osc build --vm-type=kvm
%files filesys
/etc/profile.d/disorderfs.sh
%post filesys
chmod 4755 /usr/bin/fusermount || :
mknod /dev/fuse c 10 229 || :

%package pid
Summary:        Use fixed pid
Requires:       reproducible-faketools
%description pid
a script to wrap su to start a build with a fixed process id
to enhance the reproducibility of some packages
%files pid
/usr/local/bin/su

%package random
Summary:        Reduce sources of explicit randomness
Requires:       reproducible-faketools
%description random
reduce sources of explicit randomness
by replacing /dev/random and urandom
%files random
%doc README.random
%post random
rm -f /dev/{,u}random
mknod /dev/random c 1 5
mknod /dev/urandom c 1 5
%postun random
rm -f /dev/{,u}random
mknod /dev/random c 1 8
mknod /dev/urandom c 1 9

%package zip
Summary:        Replacement zip
Requires:       p7zip
Requires:       perl
Requires:       reproducible-faketools
%description zip
a script to enhance the reproducibility of the output of zip
by replacing it with a wrapper to 7z
%files zip
/usr/local/bin/zip
/usr/local/bin/reproducible-zip.pl

%package jar
Summary:        Replacement jar
Requires:       java-devel
Requires:       reproducible-faketools
%description jar
a script to enhance the reproducibility of the output of jar
by normalizing mtimes via the --date= option
%files jar
/usr/local/bin/jar

%package rpmbuild
Summary:        Wrapper to include various other faketools
Requires:       reproducible-faketools
%description rpmbuild
This is a wrapper script that runs scripts from
/usr/local/lib/reproducible-faketools/rpmbuild.d/
%files rpmbuild
/usr/local/bin/rpmbuild
%dir /usr/local/lib/reproducible-faketools/rpmbuild.d

%package faketime
Summary:        Fake time via LD_PRELOAD
Requires:       libfaketime
Requires:       reproducible-faketools-rpmbuild
%description faketime
a script to enhance the reproducibility of the output
by replacing time(2) and fstat(2) library calls to return our notion of time
%files faketime
/usr/local/lib/reproducible-faketools/rpmbuild.d/60-faketime.sh

%package dettrace
Summary:        Use dettrace to normalize env
%if 0%{?withdettrace}
Requires:       dettrace
%else
Recommends:     dettrace
%endif
Requires:       reproducible-faketools-rpmbuild
%description dettrace
a script to enhance the reproducibility of the output
by ptraceing in a container
%files dettrace
/usr/local/lib/reproducible-faketools/rpmbuild.d/50-dettrace.sh

%package strace
Summary:        Run build with strace
Requires:       reproducible-faketools-rpmbuild
Requires:       strace
%description strace
a script to facilitate the debugging of reproducibility issues
by running rpmbuild with strace to find how files are created
%files strace
/usr/local/lib/reproducible-faketools/rpmbuild.d/55-strace.sh

%package rustc
Summary:        Fingerprint every crate rustc emits
Requires:       reproducible-faketools-rpmbuild
%description rustc
a script to facilitate the debugging of reproducibility issues in rust
by wrapping rustc to record the flags, the -C metadata value and a sha256
of every artifact each crate produces, one file per crate.
Diffing the logs of two builds names the first crate that differs, which
is what autoprovenance does for packages built from C.
The log is written to /home/abuild/rpmbuild/rustcwrap, overridable with
$RUSTCWRAP_LOG.
%files rustc
/usr/local/lib/reproducible-faketools/rustcwrap
/usr/local/lib/reproducible-faketools/rpmbuild.d/56-rustc.sh

%package j1
Summary:        Run build with single-thread
Requires:       reproducible-faketools-rpmbuild
Requires:       util-linux
%description j1
a script to facilitate the debugging of reproducibility issues
by running rpmbuild with taskset 1 to reduce parallelism

%post j1
for f in /sys/devices/system/cpu/cpu*/online ; do
   echo 0 > $f ||:
done

%files j1
/usr/local/lib/reproducible-faketools/rpmbuild.d/60-j1.sh

%package aslr
Summary:        Run build without aslr
Requires:       reproducible-faketools-rpmbuild
%description aslr
Run the build without aslr. Does not require root permissions.
%files aslr
/usr/local/lib/reproducible-faketools/rpmbuild.d/40-aslr.sh

%package verbose
Summary:        Run faketools in verbose mode
Requires:       reproducible-faketools-rpmbuild
%description verbose
prints various notice messages from faketools - useful for debugging
warning: can confuse some test frameworks
%files verbose
/usr/local/lib/reproducible-faketools/rpmbuild.d/03-verbose.sh

%package future1y
Summary:        Run build with the timestamp set to 1y in the future
Requires:       reproducible-faketools-future
%description future1y
Run the build with the timestamp set to 1y in the future
%files future1y
/usr/local/lib/reproducible-faketools/rpmbuild.d/80-future1y.sh

%package future
Summary:        Run build with the timestamp set to 16y in the future
Requires:       reproducible-faketools-rpmbuild
%description future
Run the build with the timestamp set to 16y in the future
(overridable default)
%files future
/usr/local/lib/reproducible-faketools/rpmbuild.d/81-future.sh

%package futurepost
Summary:        Run build in the future
Requires:       reproducible-faketools
%description futurepost
Uses post script to modify the build system date,
so that it works when rpmbuild runs as non-root (default).
Needs osc build --clean
Warning: Only install in scratch-VMs as it will change the system clock.
%post futurepost
now=$(date +%%s)
date --set @$((now + 34694220))
%files futurepost
%ghost /var/log/futurepost

%files
%license LICENSE.md
%doc README.md
%dir /usr/local/lib/%{name}
/usr/local/lib/%{name}/lib

%changelog
