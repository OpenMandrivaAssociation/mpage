Summary:	A tool for printing multiple pages of text on each printed page
Name:		mpage
Version:	2.5.6
Release:	16
License:	BSD
Group:		System/Printing
Url:		http://www.mesa.nl/pub/mpage
Source0:	http://www.mesa.nl/pub/mpage/%{name}-%{version}.tgz
Patch0:		mpage-2.5.4-config.patch
# Japanese patch.bz2
Patch10:	mpage-2.5.3-j.patch
Patch20:	mpage-mfix.patch
Patch21:	mpage-psprint.patch
Patch22:	mpage-2.5.3-japanese-fix.patch
Patch23:	mpage-2.5.6-LDFLAGS.diff

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
%apply_patches

%build
%make RPM_OPT_FLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
%makeinstall_std

%files
%doc CHANGES Copyright README NEWS TODO
%{_bindir}/mpage
%{_mandir}/man1/mpage.1*
%dir %{_datadir}/mpage
%{_datadir}/mpage/*

