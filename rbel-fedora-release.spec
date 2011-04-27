Summary: RBEL Fedora repo release files
Name: rbel-fedora-release
Version: 1.0
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
Source1: rbel-fedora.repo
Source2: RPM-GPG-KEY-RBEL
BuildRoot: %{_tmppath}/rbel-fedora-release
BuildArch: noarch

%description
RBEL Fedora repo release files

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d/
mkdir -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg/
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/yum.repos.d/
cp %{SOURCE2} $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/etc/yum.repos.d/*
/etc/pki/rpm-gpg/*

%changelog
* Tue Apr 26 2011 Sergio Rubio <rubiojr@frameos.org> - 1.0-1
- Initial Release

