Summary:	Simple Image Loading LibrarY
Summary(pl.UTF-8):	Simple Image Loading LibrarY - prosta biblioteka do wczytywania obrazów
Name:		SILLY
Version:	0.1.0
Release:	9
License:	MIT-like
Group:		Libraries
Source0:	http://downloads.sourceforge.net/crayzedsgui/%{name}-%{version}.tar.gz
# Source0-md5:	c3721547fced7792a36ffc9ce6ec23fd
Source1:	http://downloads.sourceforge.net/crayzedsgui/%{name}-DOCS-%{version}.tar.gz
# Source1-md5:	e52e9043b21a9d35a6da66ce9e84d3e1
Patch0:		%{name}-link.patch
Patch1:		%{name}-libpng15.patch
Patch2:		build.patch
URL:		http://www.cegui.org.uk/wiki/index.php/SILLY
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 2:1.2.10
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libpng >= 2:1.2.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SILLY means Simple Image Loading LibrarY. The aim of this library is
to provide a simple library for loading image in the context of CEGUI.
The library supports only the most common image format. The project
was initialy launch in order to provide an MIT based replacement of
DevIL with less image format supported and focused on loading image
only.

%description -l pl.UTF-8
SILLY oznacza Simple Image Loading LibrarY (prostą bibliotekę do
wczytywania obrazów). Celem projektu jest udostępnienie prostej
biblioteki do wczytywania obrazów w kontekście CEGUI. Obsługuje tylko
najpopularniejsze formaty obrazów. Projekt został zapoczątkowany w
celu zapewnienia zamiennika MIT biblioteki DevIL z mniejszą liczbą
obsługiwanych formatów i skupiającego się tylko na wczytywaniu obrazów.

%package devel
Summary:	Header files for SILLY library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SILLY
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	libpng-devel >= 2:1.2.10
Requires:	libstdc++-devel

%description devel
Header files for SILLY library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SILLY.

%package static
Summary:	Static SILLY library
Summary(pl.UTF-8):	Statyczna biblioteka SILLY
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SILLY library.

%description static -l pl.UTF-8
Statyczna biblioteka SILLY.

%prep
%setup -q -b 1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-zlib-libdir="%{_lib}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libSILLY.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSILLY.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_libdir}/libSILLY.so
%{_libdir}/libSILLY.la
%{_includedir}/SILLY
%{_pkgconfigdir}/SILLY.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libSILLY.a
