#!/bin/bash

MAGNUM_VERSION="2019.10"

# corrade
sudo dnf builddep -y spec/corrade.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/corrade.spec --clean
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/corrade-${MAGNUM_VERSION}-1.x86_64.rpm
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/corrade-devel-${MAGNUM_VERSION}-1.x86_64.rpm

# magnum
sudo dnf builddep -y spec/magnum.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum.spec --clean
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-${MAGNUM_VERSION}-1.x86_64.rpm
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-devel-${MAGNUM_VERSION}-1.x86_64.rpm

# magnum-plugins
sudo dnf builddep -y spec/magnum-plugins.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-plugins.spec --clean
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-plugins-${MAGNUM_VERSION}-1.x86_64.rpm
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-plugins-devel-${MAGNUM_VERSION}-1.x86_64.rpm

# magnum-integration
sudo dnf builddep -y spec/magnum-integration.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-integration.spec --clean
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-integration-${MAGNUM_VERSION}-1.x86_64.rpm
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-integration-devel-${MAGNUM_VERSION}-1.x86_64.rpm

# magnum-extras
sudo dnf builddep -y spec/magnum-extras.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-extras.spec --clean
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-extras-${MAGNUM_VERSION}-1.x86_64.rpm
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-extras-devel-${MAGNUM_VERSION}-1.x86_64.rpm

# magnum-examples
sudo dnf builddep -y spec/magnum-examples.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-examples.spec --clean
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-examples-${MAGNUM_VERSION}-1.x86_64.rpm
