# reproducible-faketools
These tools are meant to help with [reproducible builds](https://reproducible-builds.org/).
This works by masking standard UNIX tools in build environments
with versions that give more predictable output when [$SOURCE_DATE_EPOCH](https://reproducible-builds.org/specs/source-date-epoch/) is set
but just redirect to the normal version otherwise.

This is similar to [reproducible-utils](https://anonscm.debian.org/git/reproducible/reproducible-utils.git/tree/) and might be merged later.

## Usage

in [OBS](https://build.opensuse.org/), pull in extra packages by adding to [prjconf](https://build.opensuse.org/projects/home:bmwiedemann:reproducible:rebuild/prjconf):

    VMinstall: reproducible-faketools-j1

in osc:

    osc build --vm-type=kvm -x reproducible-faketools-j1

in [rbk](https://github.com/bmwiedemann/reproducibleopensuse/blob/devel/rbk):

    oscbuildparams="-x reproducible-faketools-j1" rbk

## How to Contribute

Send bugreports and pull-requests via [GitHub](https://github.com/bmwiedemann/reproducible-faketools/issues).
