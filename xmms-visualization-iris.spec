Summary:	XMMS - iris visualization plugin
Summary(pl):	XMMS - wtyczka do wizualizacji iris
Name:		xmms-visualization-iris
Version:	0.9
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://cdelfosse.free.fr/xmms-iris/iris-%{version}.tar.gz
URL:		http://cdelfosse.free.fr/xmms-iris/
BuildRequires:	XFree86-OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
Iris visualization plugin for XMMS.

%description -l pl
Wytczka do wizualizacji iris dla XMMS.

%prep
%setup -q -n iris-%{version}

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/xmms/Visualization/libiris.*
