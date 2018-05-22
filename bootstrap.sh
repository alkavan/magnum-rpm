#!/bin/bash

# RUN AS ROOT USER!

dnf group install -y 'Development Tools'
dnf install -y fedora-packager rpmdevtools

dnf builddep -y spec/corrade.spec
dnf builddep -y spec/magnum.spec
dnf builddep -y spec/magnum-plugins.spec
dnf builddep -y spec/magnum-integration.spec
dnf builddep -y spec/magnum-extras.spec
dnf builddep -y spec/magnum-examples.spec

rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/corrade.spec
dnf install -y ~/rpmbuild/RPMS/x86_64/corrade-2018.04-1.x86_64.rpm
dnf install -y ~/rpmbuild/RPMS/x86_64/corrade-devel-2018.04-1.x86_64.rpm

rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum.spec
dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-2018.04-1.x86_64.rpm
dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-devel-2018.04-1.x86_64.rpm

rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-plugins.spec
dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-plugins-2018.04-1.x86_64.rpm
dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-plugins-devel-2018.04-1.x86_64.rpm

rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-integration.spec
dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-plugins-2018.04-1.x86_64.rpm
dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-plugins-devel-2018.04-1.x86_64.rpm

rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-extras.spec
dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-extras-2018.04-1.x86_64.rpm
dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-extras-devel-2018.04-1.x86_64.rpm

rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-examples.spec
dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-examples-2018.04-1.x86_64.rpm
