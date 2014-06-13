%define url_ver %(echo %{version}|cut -d. -f1,2)

%define girapi	1.0
%define api	1
%define major	22
%define libname %mklibname wnck %{api} %{major}
%define girname %mklibname wnck-gir %{girapi}
%define devname %mklibname -d wnck %{api}

Summary:	Libwnck is Window Navigator Construction Kit
Name:		libwnck
Epoch:		1
Version:	2.31.0
Release:	8
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libwnck/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gnome-common
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)

%description
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}
Suggests:	%{name} >= %{EVRD}
Obsoletes:	%{_lib}wnck-1_22 < 1:2.31.0-3

%description -n %{libname}
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}wnck-1_22 < 1:2.31.0-3

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Development libraries, include files for libwnck
Group:		Development/GNOME and GTK+
Provides:	%{name}%{api}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}
Obsoletes:	%{_lib}wnck-1-devel < 1:2.31.0-3

%description -n %{devname}
This package includes the development files for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make 

%install
%makeinstall_std
rm -rf %{buildroot}%{_datadir}/locale/{io,be@latin,bn_IN,si,uz@cyrillic}
%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS
%{_bindir}/wnckprop
%{_bindir}/wnck-urgency-monitor

%files -n %{libname}
%{_libdir}/libwnck-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Wnck-%{girapi}.typelib

%files -n %{devname}
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/libwnck
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/Wnck-%{girapi}.gir

