Summary:	Gesture Injector: No-GEIS, No-Toolkits
Name:		ginn
Version:	0.2.6
Release:	1
License:	LGPL v3
Group:		Applications
Source0:	https://launchpad.net/ginn/0.x/0.2.6/+download/%{name}-%{version}.tar.bz2
# Source0-md5:	b486aaf747331766a1f2610a1b9c1b7a
URL:		https://launchpad.net/ginn
BuildRequires:	bamf-devel >= 0.2.53
BuildRequires:	geis-devel >= 1.0.10
BuildRequires:	libxml2-devel >= 2.7.7
BuildRequires:	xorg-lib-libX11-devel >= 1.3.3
BuildRequires:	xorg-lib-libXtst-devel >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A deamon with jinn-like wish-granting capabilities: it gives
applications the ability to support a subset of multi-touch gestures
without having to explicitly program to GEIS or multi-touch GTK/Qt
libs.

%prep
%setup -q

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
%dir %{_datadir}/%{name}
%{_datadir}/%{maname}/wishes.xml
%{_mandir}/man1/ginn.1*
