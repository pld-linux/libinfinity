#
# Conditional build:
%bcond_without	gtk2		# GTK+ 2.x based libraries
%bcond_without	gtk3		# GTK+ 3.x based libraries
%bcond_without	static_libs	# static libraries

Summary:	Infinote libraries to build collaborative text editors
Summary(pl.UTF-8):	Biblioteki Infinote do tworzenia edytorów tekstów do pracy grupowej
Name:		libinfinity
Version:	0.6.8
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://github.com/gobby/libinfinity/releases
Source0:	https://github.com/gobby/libinfinity/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9f3fbf802ffbca94a762f073bcd4fbaa
Patch0:		%{name}-link.patch
URL:		https://gobby.github.io/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	avahi-devel >= 0.6
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.16
BuildRequires:	gnutls-devel >= 2.12.0
BuildRequires:	gsasl-devel >= 0.2.21
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.12}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0}
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	libdaemon-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libinfinity is library to build collaborative text editors. Changes to
the text buffers are synced to all other clients over a central
server. Even though a central server is involved, the local user sees
his changes applied instantly and the merging is done on the
individual clients.

%description -l pl.UTF-8
libinfinity to biblioteka do tworzenia edytorów tekstu obsługujących
pracę grupową. Zmiany w buforach tekstu są synchronizowane z
pozostałymi klientami poprzez serwer centralny. Mimo wykorzystania
serwera centralnego, lokalny użytkownik widzi zmiany naniesione
natychmiast, a łączenie jest wykonywane po stronie poszczególnych
klientów.

%package devel
Summary:	Header files for core Infinote libraries
Summary(pl.UTF-8):	Pliki nagłówkowe podstawowych bibliotek Infinote
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.16
Requires:	gnutls-devel >= 2.12.0
Requires:	gsasl-devel >= 0.2.21
Requires:	libxml2-devel >= 2.0

%description devel
Header files for core Infinote libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe podstawowych bibliotek Infinote.

%package static
Summary:	Static core Infinote libraries
Summary(pl.UTF-8):	Statyczne biblioteki podstawowe Infinote
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static core Infinote libraries.

%description static -l pl.UTF-8
Statyczne biblioteki podstawowe Infinote.

%package apidocs
Summary:	API documentation for Infinote libraries
Summary(pl.UTF-8):	Dokumentacja API bibliotek Infinote
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Infinote libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek Infinote.

%package gtk
Summary:	Infinote GTK+ 2 UI libraries
Summary(pl.UTF-8):	Biblioteki Infinote interfejsu użytkownika GTK+ 2
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.12

%description gtk
Infinote GTK+ 2 UI libraries.

%description gtk -l pl.UTF-8
Biblioteki Infinote interfejsu użytkownika GTK+ 2.

%package gtk-devel
Summary:	Header files for Infinote GTK+ 2 libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Infinote GTK+ 2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.12

%description gtk-devel
Header files for Infinote GTK+ 2 libraries.

%description gtk-devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Infinote GTK+ 2.

%package gtk-static
Summary:	Static Infinote GTK+ 2 libraries
Summary(pl.UTF-8):	Statyczne biblioteki Infinote GTK+ 2
Group:		X11/Development/Libraries
Requires:	%{name}-gtk-devel = %{version}-%{release}

%description gtk-static
Static Infinote GTK+ 2 libraries.

%description gtk-static -l pl.UTF-8
Statyczne biblioteki Infinote GTK+ 2.

%package gtk3
Summary:	Infinote GTK+ 3 UI libraries
Summary(pl.UTF-8):	Biblioteki Infinote interfejsu użytkownika GTK+ 3
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3 >= 3.0

%description gtk3
Infinote GTK+ 3 UI libraries.

%description gtk3 -l pl.UTF-8
Biblioteki Infinote interfejsu użytkownika GTK+ 3.

%package gtk3-devel
Summary:	Header files for Infinote GTK+ 3 libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Infinote GTK+ 3
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk3 = %{version}-%{release}
Requires:	gtk+3-devel >= 3.0

%description gtk3-devel
Header files for Infinote GTK+ 3 libraries.

%description gtk3-devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Infinote GTK+ 3.

%package gtk3-static
Summary:	Static Infinote GTK+ 3 libraries
Summary(pl.UTF-8):	Statyczne biblioteki Infinote GTK+ 3
Group:		X11/Development/Libraries
Requires:	%{name}-gtk3-devel = %{version}-%{release}

%description gtk3-static
Static Infinote GTK+ 3 libraries.

%description gtk3-static -l pl.UTF-8
Statyczne biblioteki Infinote GTK+ 3.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
for d in %{?with_gtk2:gtk2} %{?with_gtk3:gtk3} ; do
install -d build-${d}
cd build-${d}
../%configure \
	--enable-gtk-doc \
	%{!?with_static_libs:--disable-static} \
	`[ "$d" != "gtk3" ] || echo --with-gtk3` \
	--with-html-dir=%{_gtkdocdir}
%{__make}
cd ..
done

%install
rm -rf $RPM_BUILD_ROOT

for d in %{?with_gtk2:gtk2} %{?with_gtk3:gtk3} ; do
%{__make} -C build-${d} install \
	DESTDIR=$RPM_BUILD_ROOT
done

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/infinoted-0.6/plugins/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/infinoted-0.6/plugins/*.a
%endif

%find_lang libinfinity-0.6

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   gtk -p /sbin/ldconfig
%postun gtk -p /sbin/ldconfig

%post   gtk3 -p /sbin/ldconfig
%postun gtk3 -p /sbin/ldconfig

%files -f libinfinity-0.6.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
%attr(755,root,root) %{_bindir}/infinoted-0.6
%attr(755,root,root) %{_libdir}/libinfinity-0.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinfinity-0.6.so.0
%attr(755,root,root) %{_libdir}/libinfinoted-plugin-manager-0.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinfinoted-plugin-manager-0.6.so.0
%attr(755,root,root) %{_libdir}/libinftext-0.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinftext-0.6.so.0
%dir %{_libdir}/infinoted-0.6
%dir %{_libdir}/infinoted-0.6/plugins
%attr(755,root,root) %{_libdir}/infinoted-0.6/plugins/libinfinoted-plugin-*.so
%{_iconsdir}/hicolor/*x*/apps/infinote.png
%{_iconsdir}/hicolor/scalable/apps/infinote.svg
%{_mandir}/man1/infinoted-0.6.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libinfinity-0.6.so
%attr(755,root,root) %{_libdir}/libinfinoted-plugin-manager-0.6.so
%attr(755,root,root) %{_libdir}/libinftext-0.6.so
%{_includedir}/libinfinity-0.6
%{_includedir}/libinfinoted-plugin-manager-0.6
%{_includedir}/libinftext-0.6
%{_pkgconfigdir}/libinfinity-0.6.pc
%{_pkgconfigdir}/libinfinoted-plugin-manager-0.6.pc
%{_pkgconfigdir}/libinftext-0.6.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libinfinity-0.6.a
%{_libdir}/libinfinoted-plugin-manager-0.6.a
%{_libdir}/libinftext-0.6.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libinfgtk-0.6
%{_gtkdocdir}/libinfinity-0.6
%{_gtkdocdir}/libinfinoted-plugin-manager-0.6
%{_gtkdocdir}/libinftext-0.6
%{_gtkdocdir}/libinftextgtk-0.6

%if %{with gtk2}
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libinfgtk-0.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinfgtk-0.6.so.0
%attr(755,root,root) %{_libdir}/libinftextgtk-0.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinftextgtk-0.6.so.0

%files gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libinfgtk-0.6.so
%attr(755,root,root) %{_libdir}/libinftextgtk-0.6.so
%{_includedir}/libinfgtk-0.6
%{_includedir}/libinftextgtk-0.6
%{_pkgconfigdir}/libinfgtk-0.6.pc
%{_pkgconfigdir}/libinftextgtk-0.6.pc

%if %{with static_libs}
%files gtk-static
%defattr(644,root,root,755)
%{_libdir}/libinfgtk-0.6.a
%{_libdir}/libinftextgtk-0.6.a
%endif
%endif

%if %{with gtk3}
%files gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libinfgtk3-0.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinfgtk3-0.6.so.0
%attr(755,root,root) %{_libdir}/libinftextgtk3-0.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinftextgtk3-0.6.so.0

%files gtk3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libinfgtk3-0.6.so
%attr(755,root,root) %{_libdir}/libinftextgtk3-0.6.so
%{_includedir}/libinfgtk3-0.6
%{_includedir}/libinftextgtk3-0.6
%{_pkgconfigdir}/libinfgtk3-0.6.pc
%{_pkgconfigdir}/libinftextgtk3-0.6.pc

%if %{with static_libs}
%files gtk3-static
%defattr(644,root,root,755)
%{_libdir}/libinfgtk3-0.6.a
%{_libdir}/libinftextgtk3-0.6.a
%endif
%endif
