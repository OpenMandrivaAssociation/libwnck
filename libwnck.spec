%define api_version 3
%define lib_major 0.2.0
%define startup_notification_version 0.4
%define libname %mklibname wnck- %{api_version} %{lib_major}
%define libnamedev %mklibname -d wnck- %{api_version}

Summary: Libwnck is Window Navigator Construction Kit
Name: libwnck
Version: 3.4.0
Release: %mkrel 1
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
Patch0: libwnck-2.27.4-linking.patch
License: LGPLv2+
URL: http://www.gnome.org/
Group: System/Libraries
BuildRequires: gtk+2-devel >= 2.19.7
BuildRequires: startup-notification-devel >= %{startup_notification_version}
BuildRequires: gobject-introspection-devel
BuildRequires: gtk-doc
BuildRequires: intltool
BuildRequires: gnome-common

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
Conflicts: gir-repository < 0.6.5-9

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
Conflicts: gir-repository < 0.6.5-9

%description -n %{libnamedev}
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%prep
%setup -q

%build
%configure2_5x
%make 

%install
%makeinstall_std
rm -rf %buildroot%_datadir/locale/{io,be@latin,bn_IN,si,uz@cyrillic}
%find_lang %{name} --all-name

rm -f %buildroot%{_libdir}/*.la

%files -f %{name}.lang
%doc README AUTHORS
%_bindir/wnckprop
%_bindir/wnck-urgency-monitor

%files -n %{libname}
%{_libdir}/libwnck-%{api_version}.so.%{lib_major}*
%_libdir/girepository-1.0/Wnck-3.0.typelib
%{_libdir}/libwnck-%{api_version}.so.0

%files -n %{libnamedev}
%doc ChangeLog
%doc %_datadir/gtk-doc/html/libwnck-3.0
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%_datadir/gir-1.0/Wnck-3.0.gir
