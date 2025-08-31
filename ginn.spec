Summary:	Gesture Injector: No-GEIS, No-Toolkits
Summary(pl.UTF-8):	Wstrzykiwanie gestów - bez GEIS, bez toolkitów
Name:		ginn
Version:	0.2.6
Release:	4
License:	GPL v3+
Group:		X11/Applications
Source0:	https://launchpad.net/ginn/0.x/%{version}/+download/%{name}-%{version}.tar.bz2
# Source0-md5:	b486aaf747331766a1f2610a1b9c1b7a
Patch0:		%{name}-build.patch
URL:		https://launchpad.net/ginn
BuildRequires:	bamf-devel >= 0.2.53
BuildRequires:	geis-devel >= 1.0.10
BuildRequires:	libxml2-devel >= 1:2.7.7
BuildRequires:	xorg-lib-libX11-devel >= 1.3.3
BuildRequires:	xorg-lib-libXtst-devel >= 1.1.0
Requires:	bamf >= 0.2.53
Requires:	geis >= 1.0.10
Requires:	libxml2 >= 1:2.7.7
Requires:	xorg-lib-libX11 >= 1.3.3
Requires:	xorg-lib-libXtst >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A deamon with jinn-like wish-granting capabilities: it gives
applications the ability to support a subset of multi-touch gestures
without having to explicitly program to GEIS or multi-touch GTK/Qt
libs.

%description -l pl.UTF-8
Demon o mocy spełniania życzeń w stylu dżina: umożliwa aplikacjom
obsługę podzbioru gestów wielodotykowych bez potrzeby jawnego
programowania GEIS lib wielodotykowych bibliotek GTK/Qt.

%prep
%setup -q
%patch -P0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/wishes.xml
%attr(755,root,root) %{_bindir}/ginn
%{_pkgconfigdir}/ginn.pc
%{_datadir}/ginn
%{_mandir}/man1/ginn.1*
