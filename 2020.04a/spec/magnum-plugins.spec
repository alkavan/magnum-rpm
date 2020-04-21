%define commit 755394c225131aaeb7affd5684c4ce96703a5a24

Name:       magnum-plugins
Version:    2020.04a
Release:    1
Summary:    Plugins for the Magnum C++11/C++14 graphics engine
License:    MIT
Source:     https://github.com/mosra/magnum-plugins/archive/%{commit}.zip
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   magnum = %{version}, DevIL, libpng, libjpeg-turbo, freetype, assimp, faad2-libs
BuildRequires: cmake, git, gcc-c++, DevIL-devel, libpng-devel, libjpeg-turbo-devel, freetype-devel, assimp-devel, faad2-devel
Source1: https://github.com/BinomialLLC/basis_universal/archive/master.zip

%description
Here are various plugins for the Magnum C++11/C++14 graphics engine -
asset import and conversion, text rendering and more.

%package devel
Summary: MagnumPlugins development files
Requires: %{name} = %{version}

%description devel
Headers and tools needed for the Magnum plugins collection.

%prep
%setup -c -n %{name}-%{version}

%build
unzip %{SOURCE1} -d %{_builddir}

mkdir build && cd build
# Configure CMake
cmake ../%{name}-%{commit} \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DBASIS_UNIVERSAL_DIR=%{_builddir}/basis_universal-master \
  -DBUILD_TESTS=ON \
  -DBUILD_GL_TESTS=ON \
  -DWITH_ASSIMPIMPORTER=ON \
  -DWITH_BASISIMPORTER=ON \
  -DWITH_BASISIMAGECONVERTER=ON \
  -DWITH_DDSIMPORTER=ON \
  -DWITH_DEVILIMAGEIMPORTER=ON \
  -DWITH_DRFLACAUDIOIMPORTER=ON \
  -DWITH_DRMP3AUDIOIMPORTER=ON \
  -DWITH_DRWAVAUDIOIMPORTER=ON \
  -DWITH_FAAD2AUDIOIMPORTER=ON \
  -DWITH_FREETYPEFONT=ON \
  -DWITH_HARFBUZZFONT=ON \
  -DWITH_JPEGIMAGECONVERTER=ON \
  -DWITH_JPEGIMPORTER=ON \
  -DWITH_MINIEXRIMAGECONVERTER=ON \
  -DWITH_OPENGEXIMPORTER=ON \
  -DWITH_PNGIMAGECONVERTER=ON \
  -DWITH_PNGIMPORTER=ON \
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
strip $RPM_BUILD_ROOT/%{_libdir}/*/*/*.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_builddir}/basis_universal-master

%files
%defattr(-,root,root,-)
%{_libdir}/*.so*
%{_libdir}/magnum/*/*

#%doc COPYING COPYING.LESSER

%files devel
%defattr(-,root,root,-)
%{_includedir}/MagnumPlugins
%{_includedir}/Magnum/OpenDdl
%{_includedir}/MagnumExternal
%{_datadir}/cmake/MagnumPlugins

#%doc COPYING COPYING.LESSER

%changelog
# TODO: changelog
