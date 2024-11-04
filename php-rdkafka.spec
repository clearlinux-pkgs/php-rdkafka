#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v20
# autospec commit: f35655a
#
Name     : php-rdkafka
Version  : 6.0.5
Release  : 78
URL      : https://pecl.php.net/get/rdkafka-6.0.5.tgz
Source0  : https://pecl.php.net/get/rdkafka-6.0.5.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: php-rdkafka-lib = %{version}-%{release}
Requires: php-rdkafka-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : file
BuildRequires : pkgconfig(rdkafka)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# PHP Kafka client - php-rdkafka
[![Join the chat at https://gitter.im/arnaud-lb/php-rdkafka](https://badges.gitter.im/arnaud-lb/php-rdkafka.svg)](https://gitter.im/arnaud-lb/php-rdkafka?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

%package lib
Summary: lib components for the php-rdkafka package.
Group: Libraries
Requires: php-rdkafka-license = %{version}-%{release}

%description lib
lib components for the php-rdkafka package.


%package license
Summary: license components for the php-rdkafka package.
Group: Default

%description license
license components for the php-rdkafka package.


%prep
%setup -q -n rdkafka-6.0.5
cd %{_builddir}/rdkafka-6.0.5
pushd ..
cp -a rdkafka-6.0.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-rdkafka
cp %{_builddir}/rdkafka-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-rdkafka/78f5e4ea46cab953e344029e218c9b5fd9e9cc73 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/rdkafka.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-rdkafka/78f5e4ea46cab953e344029e218c9b5fd9e9cc73
