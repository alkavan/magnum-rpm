Name:       meshoptimizer
Version:    0.14
Release:    1
Summary:    Provides algorithms to help optimize meshes for various stages of the GPU pipeline
License:    MIT
Source:     https://github.com/zeux/%{name}/archive/v%{version}.tar.gz
#Requires:
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cmake, git, gcc-c++

%description
When a GPU renders triangle meshes, various stages of the GPU pipeline have to process vertex and index data.
The efficiency of these stages depends on the data you feed to them; this library provides algorithms
to help optimize meshes for these stages, as well as algorithms to reduce the mesh complexity and storage overhead.

%package devel
Summary: meshoptimizer development files
Requires: %{name} = %{version}

%description devel
Headers and and source files of meshoptimizer.

%prep
%setup -c -n %{name}-%{version}

%build
mkdir build && cd build
# Configure CMake
cmake ../%{name}-%{version} \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DBUILD_SHARED_LIBS=true

# Compile
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

%files
%defattr(-,root,root,-)
%{_libdir}/*.so*
%{_libdir}/cmake/*
%{_includedir}/meshoptimizer.h

#%doc COPYING COPYING.LESSER

%changelog
#TODO: changelog
