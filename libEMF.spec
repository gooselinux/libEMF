Summary:	A library for generating Enhanced Metafiles
Summary(pl):	Biblioteka do generowania plików w formacie Enhanced Metafile
Name:		libEMF
Version:	1.0.4
Release:	1%{?dist}
License:	LGPLv2+ and GPLv2+
Group:		System Environment/Libraries
Source0:	http://downloads.sourceforge.net/pstoedit/%{name}-%{version}.tar.gz
# Source0-md5:	a4e91fd8077ce5f540f569e20e8ef7ff
Patch0:		%{name}-amd64.patch
Patch1:		%{name}-axp.patch
Patch3:		%{name}-s390.patch
URL:		http://libemf.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)

%description
libEMF is a library for generating Enhanced Metafiles on systems which
don't natively support the ECMA-234 Graphics Device Interface
(GDI). The library is intended to be used as a driver for other
graphics programs such as Grace or gnuplot. Therefore, it implements a
very limited subset of the GDI.

%description -l pl
libEMF to biblioteka do generowania plików w formacie Enhanced
Metafile na systemach nie obsługujących natywnie systemu graficznego
ECMA-234 GDI. Biblioteka ma służyć jako sterownik dla innych programów
graficznych, takich jak Grace czy gnuplot. Z tego powodu ma
zaimplementowany bardzo ograniczony podzbiór GDI.

%package devel
Summary:	libEMF header files
Summary(pl):	Pliki nagłówkowe libEMF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
libEMF header files.

%description devel -l pl
Pliki nagłówkowe libEMF.

%prep
%setup -q
%patch0 -p1 -b .amd64
%patch1 -p1 -b .axp
%patch3 -p1 -b .s390
chmod 0644 libemf/libemf.h

%build
# supplied libtool is broken (no C++ libraries support)
%{__libtoolize} --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--enable-editing

%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

export CPPROG="cp -p"
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/libEMF.la

%check
%{__make} check

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING COPYING.LIB NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%doc doc/html
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/libEMF

%changelog
* Tue Aug 25 2009 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.0.4-1
- updated to 1.0.4
- updated source URL
- dropped obsolete patch

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun  3 2009 Dan Horak <dan[at]danny.cz> - 1.0.3-9
- add support for s390/s390x

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.3-7
- Autorebuild for GCC 4.3

* Sun Jan 06 2008 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.0.3-6
- fixed compilation with gcc-4.3

* Mon Dec 03 2007 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.0.3-5
- fixed compilation on Alpha platform (patch by Oliver Falk)

* Sat Aug 25 2007 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.0.3-4
- rebuild for BuildID
- update license tag

* Sun Nov 19 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.0.3-3
- remove executable bit from libemf.h

* Sun Nov 19 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.0.3-2
- added license texts
- preserved timestamps during install
- added %%check section

* Sun Nov 19 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.0.3-1
- adapted PLD spec
- enhanced amd64 patch
