Summary:	XMMS - iris visualization plugin
Summary(pl):	XMMS - wtyczka do wizualizacji iris
Name:		xmms-visualization-iris
Version:	0.11
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://cdelfosse.free.fr/xmms-iris/iris-%{version}.tar.gz
# Source0-md5:	3f49d936f069765b7d317e188cf89404
URL:		http://cdelfosse.free.fr/xmms-iris/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xmms-devel
Requires:	OpenGL
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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/xmms/Visualization/libiris.*
