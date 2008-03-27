%define api_version 1
%define lib_major 22
%define startup_notification_version 0.4
%define libname %mklibname wnck- %{api_version} %{lib_major}
%define libnamedev %mklibname -d wnck- %{api_version}

Summary: Libwnck is Window Navigator Construction Kit
Name: libwnck
Version: 2.22.0
Release: %mkrel 2
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 2.22.0-2mdv various fixes from SVN
Patch0:	libwnck-2.22.0-svnfixes.patch
License: LGPL
URL: http://www.gnome.org/
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: gtk+2-devel >= 2.1
BuildRequires: startup-notification-devel >= %{startup_notification_version}
BuildRequires: gtk-doc
BuildRequires: perl-XML-Parser

#ugly stuff to update old libwnck
Obsoletes: %{name}-1_1
Provides: %{name}-1_1

%description
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}

Provides:	%{name}-%{api_version} = %{version}-%{release}
Requires:	%{name} >= %{version}
Requires:   libstartup-notification-1 >= %{startup_notification_version}

%description -n %{libname}
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package -n %{libnamedev}
Summary:	Static libraries, include files for libwnck
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}-%{api_version}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	gtk+2-devel >= 2.1
Requires:	startup-notification-devel >= %{startup_notification_version}
Conflicts:	%mklibname -d wnck-1_ 4
Conflicts:	%mklibname -d wnck-1_ 16
Conflicts:	%mklibname -d wnck-1_ 18
Obsoletes:	%mklibname -d wnck-1_ 22

%description -n %{libnamedev}
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%prep
%setup -q
%patch0 -p1 -b .svnfixes

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std
rm -rf %buildroot%_datadir/locale/{io,be@latin,bn_IN,si,uz@cyrillic}
%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig -n %{libname}
%postun -p /sbin/ldconfig -n %{libname}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS
%_bindir/wnckprop

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libwnck-%{api_version}.so.%{lib_major}*

%files -n %{libnamedev}
%defattr(-,root,root)
%doc ChangeLog
%doc %_datadir/gtk-doc/html/libwnck
%{_includedir}/*
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*


