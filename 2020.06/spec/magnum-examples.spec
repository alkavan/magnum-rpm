%define commit 6b55f43dcc9f078f12ca03a4012de7f0e28839b3

Name:       magnum-examples
Version:    2020.06
Release:    1
Summary:    Examples for the Magnum C++11/C++14 graphics engine
License:    MIT
Source:     https://github.com/mosra/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   magnum = %{version}, magnum-plugins = %{version}, magnum-integration = %{version}, magnum-extras = %{version}, Box2D
BuildRequires: cmake, git, gcc-c++, Box2D-devel
Source1: https://github.com/ocornut/imgui/archive/v1.74.zip
#Source2: https://github.com/dartsim/dart/archive/v6.9.2.zip

%description
Here are various examples for the Magnum C++11/C++14 graphics engine, demonstrating its features, usage and capabilities.

%prep
%setup -c -n %{name}-%{version}

%build
unzip %{SOURCE1} -d %{_builddir}
#unzip %{SOURCE2} -d %{_builddir}

mkdir build && cd build
# Configure CMake
cmake ../%{name}-%{version} \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DIMGUI_DIR=%{_builddir}/imgui-1.74 \
  -DWITH_ANIMATED_GIF_EXAMPLE=ON \
  -DWITH_ARCBALL_EXAMPLE=ON \
  -DWITH_AREALIGHTS_EXAMPLE=ON \
  -DWITH_AUDIO_EXAMPLE=ON \
  -DWITH_BOX2D_EXAMPLE=ON \
  -DWITH_BULLET_EXAMPLE=ON \
  -DWITH_CUBEMAP_EXAMPLE=ON \
  -DWITH_DART_EXAMPLE=OFF \
  -DWITH_FLUIDSIMULATION2D_EXAMPLE=ON \
  -DWITH_FLUIDSIMULATION3D_EXAMPLE=ON \
  -DWITH_IMGUI_EXAMPLE=ON \
  -DWITH_MOTIONBLUR_EXAMPLE=ON \
  -DWITH_MOUSEINTERACTION_EXAMPLE=ON \
  -DWITH_OCTREE_EXAMPLE=ON \
  -DWITH_PRIMITIVES_EXAMPLE=ON \
  -DWITH_PICKING_EXAMPLE=ON \
  -DWITH_RAYTRACING_EXAMPLE=ON \
  -DWITH_SHADOWS_EXAMPLE=ON \
  -DWITH_TEXT_EXAMPLE=ON \
  -DWITH_TEXTUREDTRIANGLE_EXAMPLE=ON \
  -DWITH_TRIANGLE_EXAMPLE=ON \
  -DWITH_TRIANGLE_PLAIN_GLFW_EXAMPLE=ON \
  -DWITH_TRIANGLE_SOKOL_EXAMPLE=ON \
  -DWITH_TRIANGLE_VULKAN_EXAMPLE=ON \
  -DWITH_VIEWER_EXAMPLE=ON

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=$RPM_BUILD_ROOT install
strip $RPM_BUILD_ROOT/%{_bindir}/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_builddir}/imgui-1.74

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/magnum

#%doc COPYING COPYING.LESSER

%changelog
# TODO: changelog
