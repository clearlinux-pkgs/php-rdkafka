#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-rdkafka
Version  : 6.0.3
Release  : 19
URL      : https://pecl.php.net/get/rdkafka-6.0.3.tgz
Source0  : https://pecl.php.net/get/rdkafka-6.0.3.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: php-rdkafka-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : pcre2-dev
BuildRequires : pkgconfig(rdkafka)

%description
# PHP Kafka client - php-rdkafka
[![Join the chat at https://gitter.im/arnaud-lb/php-rdkafka](https://badges.gitter.im/arnaud-lb/php-rdkafka.svg)](https://gitter.im/arnaud-lb/php-rdkafka?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

%package lib
Summary: lib components for the php-rdkafka package.
Group: Libraries

%description lib
lib components for the php-rdkafka package.


%prep
%setup -q -n rdkafka-6.0.3
cd %{_builddir}/rdkafka-6.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/rdkafka.so
