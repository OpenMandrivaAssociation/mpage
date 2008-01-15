Summary: A tool for printing multiple pages of text on each printed page
Name: mpage
Version: 2.5.5
Release: %mkrel 4
License: BSD
Group: System/Printing
Source: http://www.mesa.nl/pub/mpage/%name-%version.tar.bz2
Patch0: mpage-2.5.4-config.patch
#Patch1: mpage-2.5.4-gcc4.patch
# Japanese patch.bz2
Patch10: mpage-2.5.3-j.patch
Patch20: mpage-mfix.patch
Patch21: mpage-psprint.patch
Patch22: mpage-2.5.3-japanese-fix.patch

URL: http://www.mesa.nl/pub/mpage
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
The mpage utility takes plain text files or PostScript(TM) documents
as input, reduces the size of the text, and prints the files on a
PostScript printer with several pages on each sheet of paper.  Mpage
is very useful for viewing large printouts without using up tons of
paper.  Mpage supports many different layout options for the printed
pages.

Mpage should be installed if you need a useful utility for viewing
long text documents without wasting paper.

%prep
%setup -q
%patch0 -p1 -b .config
#%patch1 -p1 -b .gcc4
%patch10 -p1 -b .jp
%patch20 -p1 -b .fix
%patch21 -p1
%patch22 -p0

%build
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES Copyright README NEWS TODO
%_bindir/mpage
%_mandir/man1/mpage.1*
%dir %_datadir/mpage
%_datadir/mpage/*


