%define api_version 1
%define lib_major 22
%define startup_notification_version 0.4
%define lib_name %mklibname wnck- %{api_version} %{lib_major}

Summary: Libwnck is Window Navigator Construction Kit
Name: libwnck
Version: 2.19.5
Release: %mkrel 1
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
License: LGPL
URL: http://www.gnome.org/
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: gtk+2-devel >= 2.1
BuildRequires: startup-notification-devel >= %{startup_notification_version}
BuildRequires: perl-XML-Parser

#ugly stuff to update old libwnck
Obsoletes: %{name}-1_1
Provides: %{name}-1_1

%description
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package -n %{lib_name}
Summary:	%{summary}
Group:		%{group}

Provides:	%{name}-%{api_version} = %{version}-%{release}
Requires:	%{name} >= %{version}
Requires:   libstartup-notification-1 >= %{startup_notification_version}

%description -n %{lib_name}
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package -n %{lib_name}-devel
Summary:	Static libraries, include files for libwnck
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}-%{api_version}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}
Requires:	gtk+2-devel >= 2.1
Requires:	startup-notification-devel >= %{startup_notification_version}
Conflicts:	%mklibname -d wnck-1_ 4
Conflicts:	%mklibname -d wnck-1_ 16
Conflicts:	%mklibname -d wnck-1_ 18

%description -n %{lib_name}-devel
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%prep
%setup -q

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig -n %{lib_name}
%postun -p /sbin/ldconfig -n %{lib_name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%_bindir/wnckprop

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/libwnck-%{api_version}.so.%{lib_major}*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/libwnck
%{_includedir}/*
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*


