Name:       magnum
Version:    2019.10
Release:    1
Summary:    C++11/C++14 graphics middleware for games and data visualization
License:    MIT
Source:     https://github.com/mosra/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   corrade = %{version}, openal-soft, mesa-libGL, mesa-libEGL, SDL2
BuildRequires: openal-soft-devel, mesa-libGL-devel, mesa-libEGL-devel, SDL2-devel

%if %{defined suse_version}
Group:      System/Libraries
%else
Group:      System Environment/Libraries
%endif

%description
Looking for an open-source library that gives you graphics abstraction
and platform independence on major desktop, mobile and web platforms?
Do you want it to have all the convenience utilities around yet stay small,
powerful and not give up on flexibility?
Website: http://magnum.graphics

%package devel
%if %{defined suse_version}
Group: Development/Libraries/C and C++
%else
Group: Development/Libraries
%endif
Summary: Magnum development files
Requires: %{name} = %{version}

%description devel
Headers and tools needed for developing with Magnum engine.

%prep
%setup -c -n %{name}-%{version}

%build
mkdir build && cd build

# Configure CMake
cmake ../%{name}-%{version} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DWITH_AUDIO=ON \
        -DWITH_GLFWAPPLICATION=OFF \
        -DWITH_SDL2APPLICATION=ON \
        -DWITH_GLXAPPLICATION=ON \
        -DWITH_WINDOWLESSGLXAPPLICATION=ON \
        -DWITH_GLXCONTEXT=ON \
        -DWITH_OPENGLTESTER=ON \
        -DWITH_ANYAUDIOIMPORTER=ON \
        -DWITH_ANYIMAGECONVERTER=ON \
        -DWITH_ANYIMAGEIMPORTER=ON \
        -DWITH_ANYSCENEIMPORTER=ON \
        -DWITH_MAGNUMFONT=ON \
        -DWITH_MAGNUMFONTCONVERTER=ON \
        -DWITH_OBJIMPORTER=ON \
        -DWITH_TGAIMAGECONVERTER=ON \
        -DWITH_TGAIMPORTER=ON \
        -DWITH_WAVAUDIOIMPORTER=ON \
        -DWITH_DISTANCEFIELDCONVERTER=ON \
        -DWITH_FONTCONVERTER=ON \
        -DWITH_IMAGECONVERTER=ON \
        -DWITH_GL_INFO=ON \
        -DWITH_AL_INFO=ON

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=$RPM_BUILD_ROOT install
strip $RPM_BUILD_ROOT/%{_prefix}/lib*/magnum/audioimporters/*.so
strip $RPM_BUILD_ROOT/%{_prefix}/lib*/magnum/fontconverters/*.so
strip $RPM_BUILD_ROOT/%{_prefix}/lib*/magnum/fonts/*.so
strip $RPM_BUILD_ROOT/%{_prefix}/lib*/magnum/imageconverters/*.so
strip $RPM_BUILD_ROOT/%{_prefix}/lib*/magnum/importers/*.so
strip $RPM_BUILD_ROOT/%{_prefix}/bin/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/lib*/*.a
%{_prefix}/lib*/*.so*
%{_prefix}/lib*/magnum/*/*.so*
%{_prefix}/lib*/magnum/*/*.conf
#%doc COPYING COPYING.LESSER

%files devel
%defattr(-,root,root,-)
%{_prefix}/lib*/*.a
%{_prefix}/lib*/*.so*
%{_prefix}/lib*/magnum/*/*.so*
%{_prefix}/lib*/magnum/*/*.conf
%{_prefix}/bin/magnum-al-info
%{_prefix}/bin/magnum-distancefieldconverter
%{_prefix}/bin/magnum-fontconverter
%{_prefix}/bin/magnum-gl-info
%{_prefix}/bin/magnum-imageconverter
%{_prefix}/include/Magnum
%{_prefix}/include/MagnumExternal
%{_prefix}/include/MagnumPlugins
%{_prefix}/share/cmake/Magnum
#%doc COPYING COPYING.LESSER

%changelog
# TODO: changelog
