Name:       magnum-examples
Version:    master
Release:    1
Summary:    Examples for the Magnum C++11/C++14 graphics engine
License:    MIT
Source:     https://github.com/mosra/%{name}/archive/refs/heads/%{version}.zip#/%{name}-%{version}.zip
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   magnum = %{version}, magnum-plugins = %{version}, magnum-integration = %{version}, magnum-extras = %{version}, Box2D
BuildRequires: cmake, git, gcc-c++, Box2D-devel
Source1: https://github.com/ocornut/imgui/archive/v1.88.zip

%description
Here are various examples for the Magnum C++11/C++14 graphics engine, demonstrating its features, usage and capabilities.

%prep
%setup -c -n %{name}-%{version}

%build
unzip %{SOURCE1} -d %{_builddir}

mkdir build && cd build
# Configure CMake
cmake ../%{name}-%{version} \
  -DCMAKE_BUILD_TYPE=Debug \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DIMGUI_DIR=%{_builddir}/imgui-1.88 \
  -DMAGNUM_WITH_ANIMATED_GIF_EXAMPLE=ON \
  -DMAGNUM_WITH_ARCBALL_EXAMPLE=ON \
  -DMAGNUM_WITH_AREALIGHTS_EXAMPLE=ON \
  -DMAGNUM_WITH_AUDIO_EXAMPLE=ON \
  -DMAGNUM_WITH_BOX2D_EXAMPLE=ON \
  -DMAGNUM_WITH_BULLET_EXAMPLE=ON \
  -DMAGNUM_WITH_CUBEMAP_EXAMPLE=ON \
  -DMAGNUM_WITH_DART_EXAMPLE=OFF \
  -DMAGNUM_WITH_FLUIDSIMULATION2D_EXAMPLE=ON \
  -DMAGNUM_WITH_FLUIDSIMULATION3D_EXAMPLE=ON \
  -DMAGNUM_WITH_IMGUI_EXAMPLE=ON \
  -DMAGNUM_WITH_LEAPMOTION_EXAMPLE=OFF \
  -DMAGNUM_WITH_MOTIONBLUR_EXAMPLE=ON \
  -DMAGNUM_WITH_MOUSEINTERACTION_EXAMPLE=ON \
  -DMAGNUM_WITH_OCTREE_EXAMPLE=ON \
  -DMAGNUM_WITH_OVR_EXAMPLE=OFF \
  -DMAGNUM_WITH_PICKING_EXAMPLE=ON \
  -DMAGNUM_WITH_PRIMITIVES_EXAMPLE=ON \
  -DMAGNUM_WITH_RAYTRACING_EXAMPLE=ON \
  -DMAGNUM_WITH_SHADOWS_EXAMPLE=ON \
  -DMAGNUM_WITH_TEXT_EXAMPLE=ON \
  -DMAGNUM_WITH_TEXTUREDQUAD_EXAMPLE=ON \
  -DMAGNUM_WITH_TRIANGLE_EXAMPLE=ON \
  -DMAGNUM_WITH_TRIANGLE_PLAIN_GLFW_EXAMPLE=ON \
  -DMAGNUM_WITH_TRIANGLE_SOKOL_EXAMPLE=OFF \
  -DMAGNUM_WITH_TRIANGLE_VULKAN_EXAMPLE=ON \
  -DMAGNUM_WITH_VIEWER_EXAMPLE=ON \
  -DMAGNUM_WITH_WEBXR_EXAMPLE=OFF

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
rm -rf %{_builddir}/imgui-1.79

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/magnum

#%doc COPYING

%changelog
# TODO: changelog
