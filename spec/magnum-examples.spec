Name:       magnum-examples
Version:    2018.04
Release:    1
Summary:    Examples for the Magnum C++11/C++14 graphics engine
License:    MIT
Source:     https://github.com/mosra/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   magnum = 2018.04, magnum-plugins = 2018.04, magnum-integration = 2018.04, magnum-extras = 2018.04, bullet, bullet-extras, openal-soft
BuildRequires: cmake, git, gcc-c++

%if %{defined suse_version}
Group:      System/Libraries
%else
Group:      System Environment/Libraries
%endif

%description
Here are various examples for the Magnum C++11/C++14 graphics engine, demonstrating its features, usage and capabilities.

%prep
%setup -c -n %{name}-%{version}

%build
mkdir build && cd build
# Configure CMake
cmake ../%{name}-%{version} \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DWITH_AREALIGHTS_EXAMPLE=ON \
    -DWITH_AUDIO_EXAMPLE=ON \
    -DWITH_BULLET_EXAMPLE=ON \
    -DWITH_CUBEMAP_EXAMPLE=ON \
    -DWITH_MOTIONBLUR_EXAMPLE=ON \
    -DWITH_PRIMITIVES_EXAMPLE=ON \
    -DWITH_PICKING_EXAMPLE=ON \
    -DWITH_SHADOWS_EXAMPLE=ON \
    -DWITH_TEXT_EXAMPLE=ON \
    -DWITH_TEXTUREDTRIANGLE_EXAMPLE=ON \
    -DWITH_TRIANGLE_EXAMPLE=ON \
    -DWITH_TRIANGLE_PLAIN_GLFW_EXAMPLE=OFF \
    -DWITH_VIEWER_EXAMPLE=ON

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=$RPM_BUILD_ROOT install
strip $RPM_BUILD_ROOT/%{_prefix}/bin/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/bin/*
%{_prefix}/share/magnum
#%doc COPYING COPYING.LESSER

%changelog
# TODO: changelog
