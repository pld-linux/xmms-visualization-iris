Summary:	XMMS - iris visualization plugin.
Summary(pl):	XMMS - wtyczka do wizualizacji iris.
Name:		xmms-visualization-iris
Version:	0.9
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	xmms-devel
BuildRequires:	XFree86-OpenGL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
Iris visualization plugin for XMMS.

%description -l pl
Wytczka do wizualizacji iris dla XMMS.

%prep
%setup -q -n %{name}

%build
%configure2_13
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
