#!/usr/bin/perl

require "/home/mackers/cgi-lib.pl";
&ReadParse;

$in{'p'} = 4 unless $in{'p'};

print "Content-type: text/html\n\n";
print `/home/mackers/www/scripts/passook/passook -p $in{'p'}`;
