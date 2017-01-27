# reproducible-faketools
These tools are meant to help with [reproducible builds](https://reproducible-builds.org/).
This works by masking standard UNIX tools in build environments
with versions that give more predictable output when [$SOURCE_DATE_EPOCH](https://reproducible-builds.org/specs/source-date-epoch/) is set
but just redirect to the normal version otherwise.

This is similar to [reproducible-utils](https://anonscm.debian.org/git/reproducible/reproducible-utils.git/tree/) and might be merged later.
