Name:       magnum-extras
Version:    master
Release:    1
Summary:    Extras for the Magnum C++11/C++14 graphics engine
License:    MIT
Source:     https://github.com/mosra/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   magnum = %{version}
BuildRequires: cmake, git, gcc-c++

%description
Here you find extra functionality for the Magnum C++11/C++14 graphics engine -
playground for testing new APIs, specialized stuff that doesn't necessarily need to be a part
of main Magnum repository or mutually exclusive functionality.

%package devel
Summary: MagnumIntegration development files
Requires: %{name} = %{version}

%description devel
Headers and tools needed for extra functionality for the Magnum C++11/C++14 graphics engine.

%prep
%setup -c -n %{name}-%{version}

%build
mkdir build && cd build
# Configure CMake
cmake ../%{name}-%{version} \
  -DCMAKE_BUILD_TYPE=Debug \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DBUILD_TESTS=ON \
  -DBUILD_GL_TESTS=ON \
  -DWITH_PLAYER=ON \
  -DWITH_UI=ON \
  -DWITH_UI_GALLERY=ON

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=$RPM_BUILD_ROOT install
strip $RPM_BUILD_ROOT/%{_libdir}/*.so*
strip $RPM_BUILD_ROOT/%{_bindir}/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/*.so*

#%doc COPYING

%files devel
%defattr(-,root,root,-)
%{_bindir}/*
%{_includedir}/Magnum
%{_datadir}/cmake/MagnumExtras
%{_datadir}/applications/magnum-player.desktop

%changelog
# TODO: changelog
