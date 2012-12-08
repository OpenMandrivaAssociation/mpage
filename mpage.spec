Summary: A tool for printing multiple pages of text on each printed page
Name: mpage
Version: 2.5.6
Release: %mkrel 7
License: BSD
Group: System/Printing
Source: http://www.mesa.nl/pub/mpage/%name-%version.tgz
Patch0: mpage-2.5.4-config.patch
#Patch1: mpage-2.5.4-gcc4.patch
# Japanese patch.bz2
Patch10: mpage-2.5.3-j.patch
Patch20: mpage-mfix.patch
Patch21: mpage-psprint.patch
Patch22: mpage-2.5.3-japanese-fix.patch
Patch23: mpage-2.5.6-LDFLAGS.diff
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
%patch22 -p1
%patch23 -p0

%build
%make RPM_OPT_FLAGS="%{optflags}" LDFLAGS="%{ldflags}"

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




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5.6-5mdv2011.0
+ Revision: 666486
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5.6-4mdv2011.0
+ Revision: 606659
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5.6-3mdv2010.1
+ Revision: 523383
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.5.6-2mdv2010.0
+ Revision: 426165
- rebuild

* Mon Dec 29 2008 Oden Eriksson <oeriksson@mandriva.com> 2.5.6-1mdv2009.1
+ Revision: 321041
- 2.5.6
- rediffed one fuzzy patch
- use %%ldflags

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.5.5-5mdv2009.0
+ Revision: 223317
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 2.5.5-4mdv2008.1
+ Revision: 153245
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 2.5.5-2mdv2008.0
+ Revision: 74573
- use the new System/Printing RPM GROUP


* Mon Dec 11 2006 Emmanuel Andry <eandry@mandriva.org> 2.5.5-1mdv2007.0
+ Revision: 94573
- New version 2.5.5
  bunzip patches
  drop patch 1
- Import mpage

* Tue May 02 2006 Stefan van der Eijk <stefan@eijk.nu> 2.5.4-3mdk
- rebuild for sparc

* Mon Aug 22 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 2.5.4-2mdk
- gcc4 & makefilery fixes
- move encodings where they are expected to be: /usr/share/mpage

* Fri Jun 25 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.5.4-1mdk
- new release

