export RUSTC_WRAPPER=/usr/local/lib/reproducible-faketools/rustcwrap
# under rpmbuild's topdir so that the buildroot diff picks it up
: ${RUSTCWRAP_LOG:=/home/abuild/rpmbuild/rustcwrap}
export RUSTCWRAP_LOG
