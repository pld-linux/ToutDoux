Summary:	Project manager
Summary(pl):	Zarz±dca projektów
Name:		ToutDoux
Version:	1.2.7
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://www.gnu.org/software/toutdoux/source/%{name}-%{version}.tar.gz
# Source0-md5:	13eb83311422e447b88114e72155364d
Patch0:		%{name}-configure.patch
Patch1:		%{name}-am16.patch
URL:		http://www.gnu.org/software/toutdoux/en/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	docbook-utils >= 0.6.10
BuildRequires:	gdk-pixbuf-devel >= 0.9.0
BuildRequires:	gettext-devel >= 0.10.35
# ??? not in PLD
BuildRequires:	getxml >= 1.0.3
BuildRequires:	gtk+-devel >= 1.2.1
BuildRequires:	gnome-libs-devel >= 1.0.8
BuildRequires:	html-dtd401-sgml
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.3.5
BuildRequires:	openjade >= 1.2.1
BuildRequires:	postgresql-devel >= 7.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	toutdoux

%description
ToutDoux is a project manager which permits management with different
views (based on plugins). For example, you can design a plan of
actions using a tree structure.

%description -l pl
ToutDoux jest programem do zarz±dzania projektami pozwalaj±cym na
uwzglêdnianie ró¿nych punktów widzenia (bazuj±c na pluginach). Mo¿na
za jego pomoc± np. projektowaæ plan zadañ u¿ywaj±c struktury
drzewiastej.

%package devel
Summary:	ToutDoux - includes, etc
Summary(pl):	ToutDoux - pliki nag³ówkowe itp.
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	toutdoux-devel

%description devel
Header files for ToutDoux.

%description devel -l pl
Pliki nag³ówkowe itp. do ToutDoux.

%package static
Summary:	ToutDoux static libraries
Summary(pl):	Biblioteki statyczne ToutDoux
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
ToutDoux static libraries.

%description static -l pl
Biblioteki statyczne z funkcjami ToutDoux.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

echo 'Categories=Development;' >> toutdoux.desktop

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure  \
	--with-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gmenudir=%{_desktopdir}

rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/en/toutdoux/*
%attr(755,root,root) %{_bindir}/toutdoux
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/toutdoux
%dir %{_libdir}/toutdoux/plugins
%attr(755,root,root) %{_libdir}/toutdoux/plugins/lib*.so*
%dir %{_pixmapsdir}/toutdoux
%{_pixmapsdir}/toutdoux/*
%{_pixmapsdir}/*.*
%{_datadir}/toutdoux
%{_desktopdir}/*.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/toutdoux

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
