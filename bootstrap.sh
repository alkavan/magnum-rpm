#!/bin/bash

MAGNUM_VERSION="2019.10"

# corrade
sudo dnf builddep -y spec/corrade.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/corrade.spec
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/corrade-${MAGNUM_VERSION}-1.x86_64.rpm
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/corrade-devel-${MAGNUM_VERSION}-1.x86_64.rpm
rpmbuild --clean spec/corrade.spec

# magnum
sudo dnf builddep -y spec/magnum.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum.spec
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-${MAGNUM_VERSION}-1.x86_64.rpm
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-devel-${MAGNUM_VERSION}-1.x86_64.rpm
rpmbuild --clean spec/magnum.spec

# magnum-plugins
sudo dnf builddep -y spec/magnum-plugins.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-plugins.spec
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-plugins-${MAGNUM_VERSION}-1.x86_64.rpm
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-plugins-devel-${MAGNUM_VERSION}-1.x86_64.rpm
rpmbuild --clean spec/magnum-plugins.spec

# magnum-integration
sudo dnf builddep -y spec/magnum-integration.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-integration.spec
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-integration-${MAGNUM_VERSION}-1.x86_64.rpm
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-integration-devel-${MAGNUM_VERSION}-1.x86_64.rpm
rpmbuild --clean spec/magnum-integration.spec

# magnum-extras
sudo dnf builddep -y spec/magnum-extras.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-extras.spec
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-extras-${MAGNUM_VERSION}-1.x86_64.rpm
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-extras-devel-${MAGNUM_VERSION}-1.x86_64.rpm
rpmbuild --clean spec/magnum-extras.spec

# magnum-examples
sudo dnf builddep -y spec/magnum-examples.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-examples.spec
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/magnum-examples-${MAGNUM_VERSION}-1.x86_64.rpm
rpmbuild --clean spec/magnum-examples.spec
