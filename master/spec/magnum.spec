Name:       magnum
Version:    master
Release:    1
Summary:    C++11/C++14 graphics middleware for games and data visualization
License:    MIT
Source:     https://github.com/mosra/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   corrade = %{version}, openal-soft, mesa-libGL, mesa-libEGL, SDL2, glfw, vulkan-loader
BuildRequires: cmake, git, gcc-c++, openal-soft-devel, mesa-libGL-devel, mesa-libEGL-devel, SDL2-devel, glfw-devel, vulkan-loader-devel

# Fedora 35 also seems to neee the mesa-vulkan-devel package

%description
Looking for an open-source library that gives you graphics abstraction
and platform independence on major desktop, mobile and web platforms?
Do you want it to have all the convenience utilities around yet stay small,
powerful and not give up on flexibility?
Website: http://magnum.graphics

%package devel
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
  -DCMAKE_BUILD_TYPE=Debug \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DMAGNUM_WITH_AUDIO=ON \
  -DMAGNUM_WITH_VK=ON \
  -DMAGNUM_WITH_GLFWAPPLICATION=ON \
  -DMAGNUM_WITH_GLXAPPLICATION=ON \
  -DMAGNUM_WITH_SDL2APPLICATION=ON \
  -DMAGNUM_WITH_XEGLAPPLICATION=ON \
  -DMAGNUM_WITH_WINDOWLESSGLXAPPLICATION=ON \
  -DMAGNUM_WITH_WINDOWLESSEGLAPPLICATION=ON \
  -DMAGNUM_WITH_EGLCONTEXT=ON \
  -DMAGNUM_WITH_GLXCONTEXT=ON \
  -DMAGNUM_WITH_OPENGLTESTER=ON \
  -DMAGNUM_WITH_ANYAUDIOIMPORTER=ON \
  -DMAGNUM_WITH_ANYIMAGECONVERTER=ON \
  -DMAGNUM_WITH_ANYIMAGEIMPORTER=ON \
  -DMAGNUM_WITH_ANYSCENECONVERTER=ON \
  -DMAGNUM_WITH_ANYSCENEIMPORTER=ON \
  -DMAGNUM_WITH_ANYSHADERCONVERTER=ON \
  -DMAGNUM_WITH_MAGNUMFONT=ON \
  -DMAGNUM_WITH_MAGNUMFONTCONVERTER=ON \
  -DMAGNUM_WITH_OBJIMPORTER=ON \
  -DMAGNUM_WITH_TGAIMAGECONVERTER=ON \
  -DMAGNUM_WITH_TGAIMPORTER=ON \
  -DMAGNUM_WITH_WAVAUDIOIMPORTER=ON \
  -DMAGNUM_WITH_DISTANCEFIELDCONVERTER=ON \
  -DMAGNUM_WITH_FONTCONVERTER=ON \
  -DMAGNUM_WITH_IMAGECONVERTER=ON \
  -DMAGNUM_WITH_SCENECONVERTER=ON \
  -DMAGNUM_WITH_SHADERCONVERTER=ON \
  -DMAGNUM_WITH_GL_INFO=ON \
  -DMAGNUM_WITH_VK_INFO=ON \
  -DMAGNUM_WITH_AL_INFO=ON \
  -DMAGNUM_BUILD_TESTS=ON \
  -DMAGNUM_BUILD_GL_TESTS=ON \
  -DMAGNUM_BUILD_AL_TESTS=ON \
  -DMAGNUM_BUILD_VK_TESTS=ON

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=$RPM_BUILD_ROOT install
strip $RPM_BUILD_ROOT/%{_libdir}/*.so*
strip $RPM_BUILD_ROOT/%{_libdir}/magnum-d/*/*.so*
strip $RPM_BUILD_ROOT/%{_bindir}/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/*.a
%{_libdir}/*.so*
%{_libdir}/magnum-d/*/*.so*
%{_libdir}/magnum-d/*/*.conf

#%doc COPYING

%files devel
%defattr(-,root,root,-)

%{_bindir}/*
%{_includedir}/Magnum
%{_includedir}/MagnumExternal
%{_includedir}/MagnumPlugins
%{_datadir}/cmake/Magnum
%{_datadir}/magnum

%changelog
# TODO: changelog
