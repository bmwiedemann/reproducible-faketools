wrapper+=(strace -q -s 400 -f \
    -e file,open,openat,rename,renameat,renameat2,link,linkat,symlink,symlinkat\
,chdir,fchdir,execve\
,clone,clone3,fork,vfork,uname)
