Name:       magnum-integration
Version:    2018.04
Release:    1
Summary:    Integration libraries for the Magnum C++11/C++14 graphics engine
License:    MIT
Source:     https://github.com/mosra/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   magnum = 2018.04, bullet, bullet-extras
BuildRequires: cmake, git, gcc-c++, bullet-devel, bullet-devel

%if %{defined suse_version}
Group:      System/Libraries
%else
Group:      System Environment/Libraries
%endif

%description
Here are integration libraries for Magnum C++11/C++14 graphics engine,
providing integration of various math and physics libraries into the engine itself.

%package devel
%if %{defined suse_version}
Group: Development/Libraries/C and C++
%else
Group: Development/Libraries
%endif
Summary: MagnumIntegration development files
Requires: %{name} = %{version}

%description devel
Headers and tools needed for integrating Magnum with various math and physics libraries.

%prep
%setup -c -n %{name}-%{version}

%build
mkdir build && cd build
# Configure CMake
cmake ../%{name}-%{version} \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DWITH_BULLET=ON \
    -DWITH_DART=OFF

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=$RPM_BUILD_ROOT install
strip $RPM_BUILD_ROOT/%{_prefix}/lib*/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/lib*/*.so*
#%doc COPYING COPYING.LESSER

%files devel
%defattr(-,root,root,-)
%{_prefix}/lib*/*.so*
%{_prefix}/include/Magnum
%{_prefix}/share/cmake/MagnumIntegration
#%doc COPYING COPYING.LESSER

%changelog
# TODO: changelog
