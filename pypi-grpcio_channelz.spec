#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-grpcio_channelz
Version  : 1.56.2
Release  : 45
URL      : https://files.pythonhosted.org/packages/e6/2f/e97349e123a3802a8a2cb387781718e76b44307c79f139547f1b1c09a847/grpcio-channelz-1.56.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/e6/2f/e97349e123a3802a8a2cb387781718e76b44307c79f139547f1b1c09a847/grpcio-channelz-1.56.2.tar.gz
Summary  : Channel Level Live Debug Information Service for gRPC
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-grpcio_channelz-license = %{version}-%{release}
Requires: pypi-grpcio_channelz-python = %{version}-%{release}
Requires: pypi-grpcio_channelz-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(grpcio)
BuildRequires : pypi(protobuf)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
gRPC Python Channelz package
==============================
Channelz is a live debug tool in gRPC Python.

%package license
Summary: license components for the pypi-grpcio_channelz package.
Group: Default

%description license
license components for the pypi-grpcio_channelz package.


%package python
Summary: python components for the pypi-grpcio_channelz package.
Group: Default
Requires: pypi-grpcio_channelz-python3 = %{version}-%{release}

%description python
python components for the pypi-grpcio_channelz package.


%package python3
Summary: python3 components for the pypi-grpcio_channelz package.
Group: Default
Requires: python3-core
Provides: pypi(grpcio_channelz)
Requires: pypi(grpcio)
Requires: pypi(protobuf)

%description python3
python3 components for the pypi-grpcio_channelz package.


%prep
%setup -q -n grpcio-channelz-1.56.2
cd %{_builddir}/grpcio-channelz-1.56.2
pushd ..
cp -a grpcio-channelz-1.56.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689801145
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-grpcio_channelz
cp %{_builddir}/grpcio-channelz-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-grpcio_channelz/242ec6abfdd8c114f2e803b84934469c299348fc || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-grpcio_channelz/242ec6abfdd8c114f2e803b84934469c299348fc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
