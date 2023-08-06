Name:       magnum-integration
Version:    master
Release:    1
Summary:    Integration libraries for the Magnum C++11/C++14 graphics engine
License:    MIT
Source:     https://github.com/mosra/%{name}/archive/refs/heads/%{version}.zip#/%{name}-%{version}.zip
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   magnum = %{version}, bullet, bullet-extras, eigen3
BuildRequires: cmake, git, gcc-c++, bullet-devel, eigen3-devel glm-devel
Source1: https://github.com/ocornut/imgui/archive/v1.79.zip

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
cmake ../%{name}-%{version} \
  -DCMAKE_BUILD_TYPE=Debug \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DIMGUI_DIR=%{_builddir}/imgui-1.79 \
  -DMAGNUM_WITH_BULLET=ON \
  -DMAGNUM_WITH_DART=OFF \
  -DMAGNUM_WITH_EIGEN=ON \
  -DMAGNUM_WITH_GLM=ON \
  -DMAGNUM_WITH_IMGUI=ON \
  -DMAGNUM_WITH_OVR=OFF \
  -DMAGNUM_BUILD_TESTS=OFF \
  -DMAGNUM_BUILD_GL_TESTS=OFF \
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
rm -rf %{_builddir}/imgui-1.79

%files
%defattr(-,root,root,-)
%{_libdir}/*.so*

#%doc COPYING

%files devel
%defattr(-,root,root,-)
%{_includedir}/Magnum
%{_datadir}/cmake/MagnumIntegration

%changelog
# TODO: changelog
