Summary:	ToutDoux is a small project manager (for GNOME)
Name:		ToutDoux
Version:	1.1.8
Release:	1
License:	GPL
Group:		Networking
Group(pl):	Sieciowe
Source0:	http://altern.org/toutdoux/dl/%{name}-%{version}.tar.gz
Patch0:		ToutDoux-DESTDIR.patch
URL:		http://altern.org/toutdoux/en/
BuildRequires:	libxml-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	gettext-devel
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
ToutDoux is a small project manager (for GNOME).

%description -l pl
ToutDoux jest ma�ym mened�erem projekt�w dla GNOME.

%prep
%setup -q
%patch -p1

%build
automake
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
#%{_applnkdir}/
%{_datadir}/pixmaps/*
