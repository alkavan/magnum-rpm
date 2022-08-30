Name:       magnum-plugins
Version:    master
Release:    1
Summary:    Plugins for the Magnum C++11/C++14 graphics engine
License:    MIT
Source:     https://github.com/mosra/%{name}/archive/%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   magnum = %{version}, DevIL, libpng, libjpeg-turbo, freetype, assimp, faad2-libs, glslang, spirv-tools-libs
BuildRequires: cmake, git, gcc-c++, DevIL-devel, libpng-devel, libjpeg-turbo-devel, freetype-devel, assimp-devel, faad2-devel, harfbuzz-devel, glslang-devel, spirv-tools-devel
Source1: https://github.com/BinomialLLC/basis_universal/archive/refs/tags/1.15_final.zip
Source2: https://github.com/zeux/meshoptimizer/archive/refs/tags/v0.18.zip

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
unzip %{SOURCE1} -d %{_builddir}/
unzip %{SOURCE2} -d %{_builddir}/

mv %{_builddir}/meshoptimizer-0.18 %{name}-%{version}/src/external/meshoptimizer

mkdir build && cd build
# Configure CMake
cmake ../%{name}-%{version} \
  -DCMAKE_BUILD_TYPE=Debug \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DBASIS_UNIVERSAL_DIR=%{_builddir}/basis_universal-1.15_final/ \
  -DBUILD_TESTS=ON \
  -DBUILD_GL_TESTS=ON \
  -DMAGNUM_WITH_ASSIMPIMPORTER=ON \
  -DMAGNUM_WITH_BASISIMAGECONVERTER=ON \
  -DMAGNUM_WITH_BASISIMPORTER=ON \
  -DMAGNUM_WITH_DDSIMPORTER=ON \
  -DMAGNUM_WITH_DEVILIMAGEIMPORTER=ON \
  -DMAGNUM_WITH_DRFLACAUDIOIMPORTER=ON \
  -DMAGNUM_WITH_DRMP3AUDIOIMPORTER=ON \
  -DMAGNUM_WITH_DRWAVAUDIOIMPORTER=ON \
  -DMAGNUM_WITH_FAAD2AUDIOIMPORTER=ON \
  -DMAGNUM_WITH_FREETYPEFONT=ON \
  -DMAGNUM_WITH_GLSLANGSHADERCONVERTER=ON \
  -DMAGNUM_WITH_HARFBUZZFONT=ON \
  -DMAGNUM_WITH_ICOIMPORTER=ON \
  -DMAGNUM_WITH_JPEGIMAGECONVERTER=ON \
  -DMAGNUM_WITH_JPEGIMPORTER=ON \
  -DMAGNUM_WITH_MESHOPTIMIZERSCENECONVERTER=ON \
  -DMAGNUM_WITH_MINIEXRIMAGECONVERTER=ON \
  -DMAGNUM_WITH_OPENGEXIMPORTER=ON \
  -DMAGNUM_WITH_PNGIMAGECONVERTER=ON \
  -DMAGNUM_WITH_PNGIMPORTER=ON \
  -DMAGNUM_WITH_PRIMITIVEIMPORTER=ON \
  -DMAGNUM_WITH_SPIRVTOOLSSHADERCONVERTER=ON \
  -DMAGNUM_WITH_STANFORDIMPORTER=ON \
  -DMAGNUM_WITH_STANFORDSCENECONVERTER=ON \
  -DMAGNUM_WITH_STBIMAGECONVERTER=ON \
  -DMAGNUM_WITH_STBIMAGEIMPORTER=ON \
  -DMAGNUM_WITH_STBTRUETYPEFONT=ON \
  -DMAGNUM_WITH_STBVORBISAUDIOIMPORTER=ON \
  -DMAGNUM_WITH_STLIMPORTER=ON \
  -DMAGNUM_WITH_TINYGLTFIMPORTER=ON

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=$RPM_BUILD_ROOT install
strip $RPM_BUILD_ROOT/%{_libdir}/*.so*
strip $RPM_BUILD_ROOT/%{_libdir}/magnum-d/*/*.so*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_builddir}/basis_universal-1.15_final

%files
%defattr(-,root,root,-)
%{_libdir}/*.so*
%{_libdir}/magnum-d/*/*

#%doc COPYING

%files devel
%defattr(-,root,root,-)
%{_includedir}/Magnum
%{_includedir}/MagnumPlugins
%{_includedir}/MagnumExternal
%{_datadir}/cmake/MagnumPlugins

%changelog
# TODO: changelog
