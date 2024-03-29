#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCFDF148828C642A7 (alan.coopersmith@oracle.com)
#
Name     : libXpresent
Version  : 1.0.1
Release  : 7
URL      : https://www.x.org/releases/individual/lib/libXpresent-1.0.1.tar.gz
Source0  : https://www.x.org/releases/individual/lib/libXpresent-1.0.1.tar.gz
Source1  : https://www.x.org/releases/individual/lib/libXpresent-1.0.1.tar.gz.sig
Summary  : X Present  Library
Group    : Development/Tools
License  : MIT
Requires: libXpresent-lib = %{version}-%{release}
Requires: libXpresent-license = %{version}-%{release}
BuildRequires : libXext-dev
BuildRequires : pkgconfig(presentproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(xrandr)

%description
Xpresent - X Present Extension library
--------------------------------------
All questions regarding this software should be directed at the
Xorg mailing list:

%package dev
Summary: dev components for the libXpresent package.
Group: Development
Requires: libXpresent-lib = %{version}-%{release}
Provides: libXpresent-devel = %{version}-%{release}
Requires: libXpresent = %{version}-%{release}

%description dev
dev components for the libXpresent package.


%package lib
Summary: lib components for the libXpresent package.
Group: Libraries
Requires: libXpresent-license = %{version}-%{release}

%description lib
lib components for the libXpresent package.


%package license
Summary: license components for the libXpresent package.
Group: Default

%description license
license components for the libXpresent package.


%prep
%setup -q -n libXpresent-1.0.1
cd %{_builddir}/libXpresent-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666048059
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1666048059
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libXpresent
cp %{_builddir}/libXpresent-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libXpresent/ce154c6a0d76d90cd20ef010636eb8e98a4f9fe5 || :
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/Xpresent.h
/usr/lib64/libXpresent.so
/usr/lib64/pkgconfig/xpresent.pc
/usr/share/man/man3/XPresentFreeInput.3
/usr/share/man/man3/XPresentNotifyMSC.3
/usr/share/man/man3/XPresentPixmap.3
/usr/share/man/man3/XPresentQueryCapabilities.3
/usr/share/man/man3/XPresentQueryExtension.3
/usr/share/man/man3/XPresentQueryVersion.3
/usr/share/man/man3/XPresentSelectInput.3
/usr/share/man/man3/XPresentVersion.3
/usr/share/man/man3/Xpresent.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXpresent.so.1
/usr/lib64/libXpresent.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libXpresent/ce154c6a0d76d90cd20ef010636eb8e98a4f9fe5
