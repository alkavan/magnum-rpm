#!/bin/bash

# RUN AS ROOT USER!

dnf group install -y 'Development Tools'

dnf builddep spec/corrade.spec
dnf builddep spec/magnum.spec
dnf builddep spec/magnum-plugins.spec
dnf builddep spec/magnum-integration.spec
dnf builddep spec/magnum-extras.spec
dnf builddep spec/magnum-examples.spec

rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/corrade.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-plugins.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-integration.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-extras.spec
rpmbuild --undefine=_disable_source_fetch --define "debug_package %{nil}" -ba spec/magnum-examples.spec
