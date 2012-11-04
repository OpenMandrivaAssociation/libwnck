%define	api 1
%define	major 22
%define	libname %mklibname wnck- %{api} %{major}
%define girname %mklibname wnck-gir %{api}
%define	develname %mklibname -d wnck- %{api}

Summary:	Libwnck is Window Navigator Construction Kit
Name:		libwnck
Version:	2.31.0
Release:	2
License:	LGPLv2+
URL:		http://www.gnome.org/
Group:		System/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pango-devel
BuildRequires:	libxt-devel
BuildRequires:	pkgconfig(xres)
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(glib-2.0) >= 2.16.0
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gobject-2.0) >= 2.13.0
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
Requires:	startup-notification

%description
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}
Provides:	%{name}-%{api} = %{version}-%{release}
Requires:	%{name} >= %{version}
Conflicts:	gir-repository < 0.6.5-9

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}wnck1_22 < 2.31.0-1

%description -n %{girname}
GObject Introspection interface description for %{name}.

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

%build
%configure2_5x \
	--disable-static \
	--enable-startup-notification \
	--enable-introspection=yes

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

%files -n %{girname}
%{_libdir}/girepository-1.0/Wnck-1.0.typelib

%files -n %{develname}
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/libwnck
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/Wnck-1.0.gir
