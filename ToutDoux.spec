Summary:	ToutDoux is a small project manager (for GNOME)
Name:		ToutDoux
Version:	1.2.6
Release:	1
License:	GPL
Group:		Networking
Group(de):	Netzwerkwesen
Group(pl):	Sieciowe
Source0:	http://altern.org/toutdoux/dl/%{name}-%{version}.tar.gz
URL:		http://altern.org/toutdoux/en/
BuildRequires:	postgresql-devel >= 7.0
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	gettext-devel
BuildRequires:	libxml-devel
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
ToutDoux is a small project manager (for GNOME).

%description -l pl
ToutDoux jest ma³ym mened¿erem projektów dla GNOME.

%package devel
Summary:	ToutDoux header files
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description devel
ToutDoux header files.

%prep
%setup -q

%build
gettextize --copy --force
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gmenudir=%{_applnkdir}/Utilities

gzip -9nf NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*so.*.*
%dir %{_libdir}/toutdoux
%dir %{_libdir}/toutdoux/plugins
%attr(755,root,root) %{_libdir}/toutdoux/plugins/lib*so*
%attr(755,root,root) %{_libdir}/toutdoux/plugins/lib*la
%{_applnkdir}/Utilities/*
%{_datadir}/mime-info/*
%{_pixmapsdir}/toutdoux*
%{_datadir}/toutdoux

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*so
