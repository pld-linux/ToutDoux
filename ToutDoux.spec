Summary:	Project manager
Summary(pl):	Zarz�dca projekt�w
Name:		ToutDoux
Version:	1.2.6
Release:	7
License:	GPL
Group:		Applications/Databases
Source0:	http://toutdoux.sourceforge.net/pub/toutdoux/%{name}-%{version}.tar.gz
Patch0:		%{name}-xml.patch
Patch1:		%{name}-configure.patch
URL:		http://toutdoux.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	bison
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	libxml-devel
BuildRequires:	gdk-pixbuf-devel >= 0.9.0
BuildRequires:	postgresql-devel >= 7.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
ToutDoux is a project manager which permits management with different
views (based on plugins). For example, you can design a plan of
actions using a tree structure.

%description -l pl
ToutDoux jest programem do zarz�dzania projektami pozwalaj�cym na
uwzgl�dnianie r�nych punkt�w widzenia (bazuj�c na pluginach). Mo�esz
np. projektowa� plan zada� u�ywaj�c struktury drzewiastej.

%package devel
Summary:	%{name} libraries, includes, etc
Summary(pl):	%{name} - pliki nag��wkowe, etc
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for %{name}.

%description -l pl devel
Pliki nag��wkowe etc do %{name}.

%package static
Summary:	%{name} static libraries
Summary(pl):	Biblioteki statyczne hOpla
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
%{name} static libraries.

%description -l pl static
Biblioteki statyczne z funkcjami %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I %{_aclocaldir}/gnome -I macros
%{__autoconf}
%{__automake}
%configure  \
	--with-gnome 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gmenudir=%{_applnkdir}/Utilities

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz doc/en/toutdoux/*
%attr(755,root,root) %{_bindir}/toutdoux
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/toutdoux
%dir %{_libdir}/toutdoux/plugins
%attr(755,root,root) %{_libdir}/toutdoux/plugins/lib*.so*
%dir %{_pixmapsdir}/toutdoux
%{_pixmapsdir}/toutdoux/*
%{_pixmapsdir}/*.*
%{_datadir}/toutdoux
%{_applnkdir}/*/*
%{_datadir}/mime-info/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/toutdoux

%files static
%defattr(644,root,root,755)
%{_libdir}/toutdoux/plugins/lib*.a
%{_libdir}/lib*.a
