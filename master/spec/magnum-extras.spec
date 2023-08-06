Name:       magnum-extras
Version:    master
Release:    1
Summary:    Extras for the Magnum C++11/C++14 graphics engine
License:    MIT
Source:     https://github.com/mosra/%{name}/archive/refs/heads/%{version}.zip#/%{name}-%{version}.zip
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
  -DMAGNUM_WITH_PLAYER=ON \
  -DMAGNUM_WITH_UI=ON \
  -DMAGNUM_WITH_UI_GALLERY=ON \
  -DMAGNUM_BUILD_TESTS=OFF \
  -DMAGNUM_BUILD_GL_TESTS=OFF

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
