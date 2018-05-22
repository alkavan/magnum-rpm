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
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-plugins.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-integration.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-extras.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-examples.spec
