# Magnum RPM Package Toolkit

This toolkit helps with building RPM packages for Magnum C++ engine,
specifically on Fedora Linux, but should be also compatible with other
RedHat Linux flavors.

This toolkit was tested on Fedora Linux 36.
I should note that only the last version of Magnum was tested
fully on the latest version of Fedora Linux.
This means, I did not test the 2020.06 actually works on Fedora 29,
I expect it to, but it might not.

## Before Building
```
dnf group install -y 'Development Tools'
dnf install -y fedora-packager rpmdevtools
```

## Build and Installation
Maybe you will need this, check if you already have these symbolic links.

```
sudo ln -s /usr/lib64/libvulkan.so.1 /usr/lib64/libvulkan.so
sudo ln -s /usr/lib/libvulkan.so.1 /usr/lib/libvulkan.so
```

I am providing a script `bootstrap.sh` that builds all packages and installs
them on the system in one run. You should have `sudo` access because usage of
`builddep` and `dnf` (installing packages), but you could also just inspect the
script yourself and run the commands manually.

```
cd master
./bootstrap.sh
```