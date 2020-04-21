%define commit d2f9067f7865f469c71e1f7881089d7a2dee9dd4

Name:       magnum-integration
Version:    2020.04a
Release:    1
Summary:    Integration libraries for the Magnum C++11/C++14 graphics engine
License:    MIT
Source:     https://github.com/mosra/magnum-integration/archive/d2f9067f7865f469c71e1f7881089d7a2dee9dd4.zip
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   magnum = %{version}, bullet, bullet-extras, eigen3
BuildRequires: cmake, git, gcc-c++, bullet-devel, eigen3-devel glm-devel
Source1: https://github.com/ocornut/imgui/archive/v1.74.zip

%description
Here are integration libraries for Magnum C++11/C++14 graphics engine,
providing integration of various math and physics libraries into the engine itself.

%package devel
Summary: MagnumIntegration development files
Requires: %{name} = %{version}

%description devel
Headers and tools needed for integrating Magnum with various math and physics libraries.

%prep
%setup -c -n %{name}-%{version}

%build
unzip %{SOURCE1} -d %{_builddir}

mkdir build && cd build
# Configure CMake
cmake ../%{name}-%{commit} \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DIMGUI_DIR=%{_builddir}/imgui-1.74 \
  -DBUILD_TESTS=ON \
  -DBUILD_GL_TESTS=ON \
  -DWITH_BULLET=ON \
  -DWITH_DART=OFF \
  -DWITH_EIGEN=ON \
  -DWITH_GLM=ON \
  -DWITH_IMGUI=ON \
  -DOpenGL_GL_PREFERENCE=GLVND

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=$RPM_BUILD_ROOT install
strip $RPM_BUILD_ROOT/%{_libdir}/*.so*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_builddir}/imgui-1.74

%files
%defattr(-,root,root,-)
%{_libdir}/*.so*

#%doc COPYING COPYING.LESSER

%files devel
%defattr(-,root,root,-)
%{_includedir}/Magnum
%{_datadir}/cmake/MagnumIntegration

#%doc COPYING COPYING.LESSER

%changelog
# TODO: changelog
