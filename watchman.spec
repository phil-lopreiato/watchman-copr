%define name        watchman
%define release     1
%define version     2020.07.27.00

Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Watches files and records, or triggers actions, when they change.

Group:          Development/Tools
License:        Apache 2.0
URL:            https://facebook.github.io/watchman
Source:         https://github.com/facebook/watchman/archive/v%{version}.tar.gz

BuildRequires:  autoconf, automake, libtool, python-devel, python-setuptools, gcc-c++, openssl-devel

%description
Watches files and records, or triggers actions, when they change.

%prep
%setup -q


%build
./autogen.sh
%configure
%make_build


%install
%make_install


%files
%defattr(-,root,root)
%{_bindir}/watchman
%{_bindir}/watchman-make
%{_bindir}/watchman-wait
%{_libdir}/python2.7/site-packages/pywatchman*

%doc %attr(0444,root,root)
%{_docdir}/watchman-${version}/README.markdown

%license %attr(0444,root,root) LICENSE

%exclude /usr/var/run/watchman/.not-empty
