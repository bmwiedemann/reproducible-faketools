#!/usr/bin/perl -w
use strict;
use Getopt::Long;
Getopt::Long::Configure ("bundling");
my @mappedargv=qw(7z -tzip -mtc=off);
my @lateargv=();
my %options=qw();
my @options=qw"recurse-paths|r filesync delete|d update|u test|T move|m exclude|x=s no-extra|X no-dir-entries|D junk-paths|j quiet|q names-stdin|@ 0 1 2 3 4 5 6 7 8 9";
GetOptions(\%options, @options);
#print (%options);

for(0..9) {
    if($options{$_}) {push(@mappedargv, "-mx=$_")}
}
push(@mappedargv, "-bd") if $options{quiet};
push(@mappedargv, "-x".$options{exclude}) if $options{exclude};
if($options{"junk-paths"}) { die "junk-paths option is not supported in $0" }
if($options{"names-stdin"}) {push(@lateargv, '@/dev/stdin')}

my $action='a';
my %actionmap=qw(
    add a
    update u
    delete d
);
if($actionmap{$ARGV[0]}) {
    $action=$actionmap{shift(@ARGV)};
}
if($options{move}) {$action="a"}
if($options{update}) {$action="u"}
if($options{delete}) {$action="d"}
if($options{test}) {$action="t"}
push(@mappedargv, $action, @ARGV, @lateargv);
print STDERR "@mappedargv\n";
exec(@mappedargv);
