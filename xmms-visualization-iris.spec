Summary:	XMMS - iris visualization plugin
Summary(pl):	XMMS - wtyczka do wizualizacji iris
Name:		xmms-visualization-iris
Version:	0.12
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://cdelfosse.free.fr/xmms-iris/iris-%{version}.tar.gz
# Source0-md5:	f867afc759744bb3d98949af9cfd03e6
URL:		http://cdelfosse.free.fr/xmms-iris/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	OpenGL
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Iris visualization plugin for XMMS.

%description -l pl
Wtyczka do wizualizacji iris dla XMMS.

%prep
%setup -q -n iris-%{version}

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
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
%doc README
%attr(755,root,root) %{xmms_visualization_plugindir}/libiris.*
