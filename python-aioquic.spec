# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-aioquic
Epoch: 100
Version: 1.1.0
Release: 1%{?dist}
Summary: QUIC and HTTP/3 implementation in Python
License: BSD-3-Clause
URL: https://github.com/aiortc/aioquic/tags
Source0: %{name}_%{version}.orig.tar.gz
%if 0%{?rhel} == 7
BuildRequires: openssl11
BuildRequires: openssl11-devel
%else
BuildRequires: openssl
BuildRequires: openssl-devel
%endif
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: libffi-devel
BuildRequires: pkgconfig
BuildRequires: python3-certifi
BuildRequires: python3-devel
BuildRequires: python3-pylsqpack >= 0.3.3
BuildRequires: python3-pyOpenSSL >= 22
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: python-rpm-macros

%description
aioquic is a library for the QUIC network protocol in Python. It
features a minimal TLS 1.3 implementation, a QUIC stack and an HTTP/3
stack.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
set -ex && \
%if 0%{?rhel} == 7
    export LDFLAGS="-L%{_libdir}/openssl11" && \
    export CFLAGS="-I%{_includedir}/openssl11" && \
%endif
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-aioquic
Summary: QUIC and HTTP/3 implementation in Python
Requires: python3
Requires: python3-certifi
Requires: python3-pylsqpack >= 0.3.3
Requires: python3-pyOpenSSL >= 22
Requires: python3-service-identity >= 23.1.0
Provides: python3-aioquic = %{epoch}:%{version}-%{release}
Provides: python3dist(aioquic) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-aioquic = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(aioquic) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-aioquic = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(aioquic) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-aioquic
aioquic is a library for the QUIC network protocol in Python. It
features a minimal TLS 1.3 implementation, a QUIC stack and an HTTP/3
stack.

%files -n python%{python3_version_nodots}-aioquic
%license LICENSE
%{python3_sitearch}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-aioquic
Summary: QUIC and HTTP/3 implementation in Python
Requires: python3
Requires: python3-certifi
Requires: python3-pylsqpack >= 0.3.3
Requires: python3-pyOpenSSL >= 22
Requires: python3-service-identity >= 23.1.0
Provides: python3-aioquic = %{epoch}:%{version}-%{release}
Provides: python3dist(aioquic) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-aioquic = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(aioquic) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-aioquic = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(aioquic) = %{epoch}:%{version}-%{release}

%description -n python3-aioquic
aioquic is a library for the QUIC network protocol in Python. It
features a minimal TLS 1.3 implementation, a QUIC stack and an HTTP/3
stack.

%files -n python3-aioquic
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-aioquic
Summary: QUIC and HTTP/3 implementation in Python
Requires: python3
Requires: python3-certifi
Requires: python3-pylsqpack >= 0.3.3
Requires: python3-pyOpenSSL >= 22
Requires: python3-service-identity >= 23.1.0
Provides: python3-aioquic = %{epoch}:%{version}-%{release}
Provides: python3dist(aioquic) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-aioquic = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(aioquic) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-aioquic = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(aioquic) = %{epoch}:%{version}-%{release}

%description -n python3-aioquic
aioquic is a library for the QUIC network protocol in Python. It
features a minimal TLS 1.3 implementation, a QUIC stack and an HTTP/3
stack.

%files -n python3-aioquic
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
