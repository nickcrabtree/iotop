Name:           iotop-c
Version:        1.20
Release:        1%{?dist}
Summary:        Simple top-like I/O monitor (implemented in C)

License:        GPLv2+
URL:            https://github.com/Tomas-M/iotop/
Source0:        https://github.com/Tomas-M/iotop/releases/download/v%{version}/iotop-%{version}.tar.xz
Source1:        https://github.com/Tomas-M/iotop/releases/download/v%{version}/iotop-%{version}.tar.xz.asc
Source2:        https://raw.githubusercontent.com/Tomas-M/iotop/v%{version}/debian/upstream/signing-key.asc

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  ncurses-devel
BuildRequires:  make
BuildRequires:  pkgconfig(ncursesw)

%description
iotop-c does for I/O usage what top(1) does for CPU usage. It watches I/O
usage information output by the Linux kernel and displays a table of
current I/O usage by processes on the system. It is handy for answering
the question "Why is the disk churning so much?".

iotop-c requires a Linux kernel built with the CONFIG_TASKSTATS,
CONFIG_TASK_DELAY_ACCT, CONFIG_TASK_IO_ACCOUNTING and
CONFIG_VM_EVENT_COUNTERS config options on.

iotop-c is an alternative re-implementation of iotop in C, optimized for
performance. Normally a monitoring tool intended to be used on a system
under heavy stress should use the least additional resources as
possible.

%global _hardened_build 1

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n iotop-%{version}

%build
%set_build_flags
NO_FLTO=1 %make_build

%install
V=1 STRIP=: %make_install
mv %{buildroot}%{_sbindir}/iotop %{buildroot}%{_sbindir}/iotop-c
mv %{buildroot}%{_mandir}/man8/iotop.8 %{buildroot}%{_mandir}/man8/iotop-c.8

%files
%license COPYING
%license LICENSE
%{_sbindir}/iotop-c
%{_mandir}/man8/iotop-c.8*

%changelog
* Mon Sep 04 2021 Boian Bonev <bbonev@ipacct.com> - 1.20-1
- Update to latest ver 1.20

* Tue Sep 21 2021 Boian Bonev <bbonev@ipacct.com> - 1.19-1
- Update to latest ver 1.19

* Tue Aug 24 2021 Boian Bonev <bbonev@ipacct.com> - 1.18-1
- Update to latest ver 1.18

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 6 2021 Boian Bonev <bbonev@ipacct.com> - 1.17-1
- Update to latest ver 1.17

* Thu Jan 28 2021 Boian Bonev <bbonev@ipacct.com> - 1.16-1
- Update to latest ver 1.16

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 26 2020 Boian Bonev <bbonev@ipacct.com> - 1.15-1
- Initial packaging for Fedora
