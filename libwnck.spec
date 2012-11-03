%define api 1
%define major 22
%define libname %mklibname wnck- %{api} %{major}
%define develname %mklibname -d wnck- %{api}

Summary: Libwnck is Window Navigator Construction Kit
Name: libwnck
Version: 2.31.0
Release: 1
License: LGPLv2+
URL: http://www.gnome.org/
Group: System/Libraries
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
Patch: libwnck-2.27.4-linking.patch

BuildRequires: intltool
BuildRequires: gnome-common
BuildRequires: gtk-doc
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)

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
Requires:	%{libname} = %{version}
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

