%define api 1
%define major 22
%define libname %mklibname wnck- %{api} %{major}
%define develname %mklibname -d wnck- %{api}

Summary:	Libwnck is Window Navigator Construction Kit
Name:		libwnck
Version:	2.31.0
Epoch:		1
Release:	1
License:	LGPLv2+
URL:		http://www.gnome.org/
Group:		System/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/2.31/%{name}-%{version}.tar.xz
Patch:		libwnck-2.27.4-linking.patch

BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)

%description
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}
Provides:	%{name}-%{api} = %{version}-%{release}
Requires:	%{name} >= %{version}
Conflicts:	gir-repository < 0.6.5-9

%description -n %{libname}
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package -n %{develname}
Summary:	Development libraries, include files for libwnck
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}-%{api}-devel = %{version}-%{release}
Requires:	%{name}-1 = %{version}
Conflicts:	gir-repository < 0.6.5-9

%description -n %{develname}
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%prep
%setup -q
#%patch -p1
#autoconf

%build
%configure2_5x \
	--disable-static

%make 

%install
%makeinstall_std
rm -rf %{buildroot}%{_datadir}/locale/{io,be@latin,bn_IN,si,uz@cyrillic}
%find_lang %{name}

rm -f %{buildroot}%{_libdir}/*.la

%files -f %{name}.lang
%doc README AUTHORS
%{_bindir}/wnckprop
%{_bindir}/wnck-urgency-monitor

%files -n %{libname}
%{_libdir}/libwnck-%{api}.so.%{major}*
%{_libdir}/girepository-1.0/Wnck-1.0.typelib

%files -n %{develname}
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/libwnck
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/Wnck-1.0.gir



%changelog
* Sat Apr 28 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.30.7-5
+ Revision: 794326
- rebuild
- major spec clean
- revert changes to maintain libwnck 1
- libwnck3 is the new package already established

* Sat Apr 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.4.0-1
+ Revision: 794216
- gtk3+-devel add
- version update 3.4.0

* Thu Dec 15 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.7-4
+ Revision: 741486
- remove libtool archives here as well

* Mon Oct 24 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.7-3
+ Revision: 705822
- rebuild for new xcb

* Thu Sep 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2.30.7-2
+ Revision: 700853
- rebuild

* Wed Aug 31 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.7-1
+ Revision: 697591
- new version
- xz tarball

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.30.6-3
+ Revision: 661546
- mass rebuild

* Thu Dec 16 2010 Funda Wang <fwang@mandriva.org> 2.30.6-2mdv2011.0
+ Revision: 622235
- rebuild

* Wed Nov 17 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.6-1mdv2011.0
+ Revision: 598369
- update to new version 2.30.6

* Mon Sep 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.5-1mdv2011.0
+ Revision: 581280
- update to new version 2.30.5

* Tue Sep 14 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.4-1mdv2011.0
+ Revision: 578283
- update to new version 2.30.4

* Sun Sep 12 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.3-2mdv2011.0
+ Revision: 577676
- rebuild for new g-i

* Wed Aug 04 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.3-1mdv2011.0
+ Revision: 565808
- update to new version 2.30.3

* Sat Jul 31 2010 Funda Wang <fwang@mandriva.org> 2.30.2-2mdv2011.0
+ Revision: 563906
- rebuild for new gobject-introspection

* Sun Jul 11 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.2-1mdv2011.0
+ Revision: 550679
- update to new version 2.30.2

* Tue Mar 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528961
- update to new version 2.30.0

* Tue Mar 09 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.92-1mdv2010.1
+ Revision: 517235
- new version
- bump gtk dep
- add introspection support

* Mon Feb 22 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 509658
- update to new version 2.29.91

* Wed Jan 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.6-1mdv2010.1
+ Revision: 497244
- update to new version 2.29.6

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446795
- update to new version 2.28.0

* Thu Sep 10 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 437222
- update to new version 2.27.92

* Wed Jul 29 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.5-1mdv2010.0
+ Revision: 402908
- new version
- update file list

* Wed Jul 15 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 396380
- new version
- update the patch

* Wed Jul 01 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.2-1mdv2010.0
+ Revision: 391253
- update to new version 2.26.2

* Tue Jun 30 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.1-1mdv2010.0
+ Revision: 390824
- new version
- fix build

* Tue Apr 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 366939
- update to new version 2.26.1

* Mon Mar 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 356299
- new version
- fix build

* Tue Feb 17 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.91-2mdv2009.1
+ Revision: 341372
- bump for bs bs
- new version
- rediff patch
- fix autoreconf call

* Mon Jan 19 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.5-1mdv2009.1
+ Revision: 331439
- update to new version 2.25.5

* Thu Dec 18 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.3-1mdv2009.1
+ Revision: 315912
- update to new version 2.25.3

* Tue Nov 25 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.2-1mdv2009.1
+ Revision: 306595
- update to new version 2.24.2

* Fri Nov 07 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.1-2mdv2009.1
+ Revision: 300876
- rebuild for new libxcb

* Wed Oct 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 296440
- update to new version 2.24.1

* Tue Sep 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287268
- new version

* Mon Sep 08 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.92-1mdv2009.0
+ Revision: 282796
- new version

* Tue Sep 02 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 278805
- new version

* Mon Aug 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.6-1mdv2009.0
+ Revision: 263625
- new version

* Thu Jul 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.4-1mdv2009.0
+ Revision: 230987
- new version

* Mon Jun 30 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.3-1mdv2009.0
+ Revision: 230188
- new version
- fix license
- fix buildrequires
- patch to make it link

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.1-1mdv2009.0
+ Revision: 192481
- new version
- drop patch

* Thu Mar 27 2008 Frederic Crozat <fcrozat@mandriva.com> 2.22.0-2mdv2008.1
+ Revision: 190736
- Patch0: various fixes from SVN

* Mon Mar 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183850
- new version

* Tue Feb 26 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 175482
- new version

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.21.91-2mdv2008.1
+ Revision: 170962
- rebuild

* Mon Feb 11 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.91-1mdv2008.1
+ Revision: 165445
- fix rpmlint error
- new version

* Mon Jan 28 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.90-1mdv2008.1
+ Revision: 159050
- new version

* Tue Jan 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.5-1mdv2008.1
+ Revision: 152131
- new version
- update buildrequires

  + Thierry Vignaud <tv@mandriva.org>
    - do not package big ChangeLog
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Nov 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.2.1-1mdv2008.1
+ Revision: 108690
- new version

* Tue Oct 16 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 98873
- new version

* Mon Sep 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 89343
- new version

* Tue Sep 04 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.92-1mdv2008.0
+ Revision: 79454
- rename the package

* Tue Aug 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.90-1mdv2008.0
+ Revision: 63277
- new version
- new devel name

* Mon Jul 30 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.6-1mdv2008.0
+ Revision: 56701
- new version

* Sun Jul 08 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.5-1mdv2008.0
+ Revision: 50067
- new version
- update file list

* Mon Jun 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.4-1mdv2008.0
+ Revision: 41128
- new version
- update devel conflicts
- new version
- drop patch 0
- new major

* Mon May 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.2-1mdv2008.0
+ Revision: 32083
- new version
- drop patch

* Fri Apr 27 2007 Pascal Terjan <pterjan@mandriva.org> 2.18.0-2mdv2008.0
+ Revision: 18812
- Don't crash when dragging a small window


* Mon Mar 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 142068
- new version

* Mon Feb 26 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.92-1mdv2007.1
+ Revision: 126124
- new version

* Mon Feb 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.91-1mdv2007.1
+ Revision: 120219
- new version

* Tue Jan 30 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.3-1mdv2007.1
+ Revision: 115378
- new version

* Wed Nov 22 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.2-1mdv2007.1
+ Revision: 86190
- new version

* Fri Oct 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1-3mdv2007.1
+ Revision: 63835
- rebuild
- rebuild
- Import libwnck

* Fri Oct 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1-1mdv2007.0
- New version 2.16.1

* Wed Sep 13 2006 Frederic Crozat <fcrozat@mandriva.com> 2.16.0-2mdv2007.0
- Patch0 (CVS): various bug fixes from CVS

* Tue Sep 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New release 2.16.0

* Wed Aug 23 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.92-1mdv2007.0
- New release 2.15.92

* Wed Aug 09 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.91-1mdv2007.0
- New release 2.15.91

* Wed Jul 26 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.90-1
- New release 2.15.90

* Wed Jul 12 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.4-1mdv2007.0
- New release 2.15.4

* Wed Jun 14 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.3-1
- New release 2.15.3

* Fri Jun 02 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.2-1mdv2007.0
- Release 2.15.2

* Wed May 31 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-1mdv2007.0
- New release 2.14.2

* Thu Apr 13 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.1-1mdk
- Release 2.14.1
- Remove patch0 (merged upstream)

* Wed Apr 05 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.3-3mdk
- Update patch0 (fix regression from GNOME bug #335316)

* Wed Mar 01 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.3-2mdk
- Patch0 (vuntz): fix window activatin across workspace (GNOME bug #331661)

* Tue Feb 07 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.3-1mdk
- New release 2.12.3
- use mkrel

* Tue Nov 29 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.2-1mdk
- New release 2.12.2

* Mon Oct 10 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.12.1-3mdk
- add BuildRequires: perl-XML-Parser

* Thu Oct 06 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-2mdk
- Add conflicts to ease upgrade

* Thu Oct 06 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-1mdk
- Release 2.12.1
- Remove patches 0, 1, 2, 3, 4, 5 (merged upstream)

* Mon Aug 29 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.3-3mdk 
- Patch1 (CVS): fix icon used for window selector
- Patch2 (CVS): fix memleak
- Patch3 (CVS): improve attention demand notification
- Patch4 (CVS): fix EWHM implemention
- Patch5 (CVS): fix transient window activation

* Mon Aug 29 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.3-2mdk 
- Patch0 (CVS): fix flicker when moving window across workspaces

* Tue Jul 26 2005 Götz Waschk <waschk@mandriva.org> 2.10.3-1mdk
- New release 2.10.3

* Wed Jun 29 2005 Götz Waschk <waschk@mandriva.org> 2.10.2-1mdk
- New release 2.10.2

* Fri Apr 22 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.0-2mdk 
- Add conflicts to easy upgrade

* Thu Apr 21 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.0-1mdk 
- Release 2.10.0 (from Götz Waschk package)

* Sun Mar 20 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.1-2mdk 
- Patch0 (CVS): various bug fixes

* Wed Oct 20 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.1-1mdk
- New release 2.8.1
- Remove patches 0, 1, 2 (merged upstream)

* Wed Sep 08 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.2.1-2mdk
- Patch0 (CVS): fix move to workspace X when window is on all workspaces
- Patch1 (CVS): fix focus when unminimizing from menu
- Patch2 (CVS): fix extents size for accessible API

* Wed Jul 07 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.6.2.1-1mdk
- New release 2.6.2.1

* Wed Jun 16 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.2-1mdk
- reenable libtoolize
- New release 2.6.2

* Wed Apr 21 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.1-1mdk
- drop the patch (merged)
- New release 2.6.1

* Tue Apr 06 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0.1-1mdk
- Release 2.6.0.1 (with Götz help)

