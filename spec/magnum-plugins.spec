Name:       magnum-plugins
Version:    2018.04
Release:    1
Summary:    Plugins for the Magnum C++11/C++14 graphics engine
License:    MIT
Source:     https://github.com/mosra/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   magnum = 2018.04, DevIL, libpng, libjpeg-turbo, freetype, assimp
BuildRequires: cmake, git, gcc-c++, DevIL-devel, libpng-devel, libjpeg-turbo-devel, freetype-devel, assimp-devel

%if %{defined suse_version}
Group:      System/Libraries
%else
Group:      System Environment/Libraries
%endif

%description
Here are various plugins for the Magnum C++11/C++14 graphics engine -
asset import and conversion, text rendering and more.

%package devel
%if %{defined suse_version}
Group: Development/Libraries/C and C++
%else
Group: Development/Libraries
%endif
Summary: MagnumPlugins development files
Requires: %{name} = %{version}

%description devel
Headers and tools needed for the Magnum plugins collection.

%prep
%setup -c -n %{name}-%{version}

%build
mkdir build && cd build
# Configure CMake
cmake ../%{name}-%{version} \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DWITH_ASSIMPIMPORTER=ON \
    -DWITH_DDSIMPORTER=ON \
    -DWITH_DEVILIMAGEIMPORTER=ON \
    -DWITH_DRFLACAUDIOIMPORTER=ON \
    -DWITH_DRWAVAUDIOIMPORTER=ON \
    -DWITH_FREETYPEFONT=ON \
    -DWITH_JPEGIMPORTER=ON \
    -DWITH_MINIEXRIMAGECONVERTER=ON \
    -DWITH_PNGIMAGECONVERTER=ON \
    -DWITH_PNGIMPORTER=ON \
    -DWITH_OPENGEXIMPORTER=ON \
    -DWITH_STANFORDIMPORTER=ON \
    -DWITH_STBIMAGECONVERTER=ON \
    -DWITH_STBIMAGEIMPORTER=ON \
    -DWITH_STBTRUETYPEFONT=ON \
    -DWITH_STBVORBISAUDIOIMPORTER=ON \
    -DWITH_TINYGLTFIMPORTER=ON

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=$RPM_BUILD_ROOT install
strip $RPM_BUILD_ROOT/%{_prefix}/lib*/*/*/*.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/lib*/*.so*
%{_prefix}/lib*/magnum/*/*
#%doc COPYING COPYING.LESSER

%files devel
%defattr(-,root,root,-)
%{_prefix}/lib*/*.so*
%{_prefix}/lib*/magnum/*/*
%{_prefix}/include/MagnumPlugins
%{_prefix}/include/Magnum/OpenDdl
%{_prefix}/share/cmake/MagnumPlugins
#%doc COPYING COPYING.LESSER

%changelog
# TODO: changelog