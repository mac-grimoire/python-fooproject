%{!?_version: %define _version 0.0.1 }
%global srcname carcano_foolist

Name:           python-%{srcname}
Version:        %{_version} 
Release:        1%{?dist}
Summary:        Full Features Python3 Sample Project
License:        LGPLv3+
Source0:        %{pypi_source}

BuildArch:       noarch
BuildRequires:   python3-devel python3-setuptools
Requires:        python3

%description
Full Featured Python3 Sample Project

%package -n python3-%{srcname}-common
Summary:        %{summary}
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{srcname}-common}

%description -n python3-%{srcname}-common
Python3 packages of the sample project

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
Requires:       python3-%{srcname}-common
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Python3 scripts and resources of the sample project

%prep
%autosetup -n %{srcname}-%{_version}

%build
unset RPM_BUILD_ROOT
%{__python3} setup.py bdist_wheel

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir %{buildroot}
mkdir %{buildroot}/usr
cd "%{_builddir}/%{srcname}-%{_version}/dist"
%{__python3} -m pip install --target %{buildroot}%{python3_sitelib} %{srcname}-%{_version}-py3-none-any.whl 
mkdir %{buildroot}/%{_sysconfdir}
mkdir %{buildroot}/%{_sysconfdir}/fooapp
mkdir %{buildroot}/%{_sysconfdir}/rsyslog.d
mkdir %{buildroot}/usr/bin
cp %{_builddir}/%{srcname}-%{_version}/bin/logging.conf %{buildroot}/%{_sysconfdir}/fooapp/logging.conf
cp %{_builddir}/%{srcname}-%{_version}/share/doc/fooapp/rsyslog/fooapp.conf %{buildroot}/%{_sysconfdir}/rsyslog.d/fooapp.conf
cp %{_builddir}/%{srcname}-%{_version}/bin/fooapp.py %{buildroot}/usr/bin/fooapp.py

%check
cd "%{_builddir}/%{srcname}-%{_version}"
unset RPM_BUILD_ROOT
%{__python3} setup.py nosetests >/dev/null

%files -n python3-%{srcname}-common
%{python3_sitelib}/carcano/foolist/__init__.py
%{python3_sitelib}/carcano/foolist/__pycache__/__init__.cpython-36.opt-1.pyc
%{python3_sitelib}/carcano/foolist/__pycache__/__init__.cpython-36.pyc
%{python3_sitelib}/carcano/foolist/__pycache__/foolist.cpython-36.opt-1.pyc
%{python3_sitelib}/carcano/foolist/__pycache__/foolist.cpython-36.pyc
%{python3_sitelib}/carcano/foolist/__pycache__/foolistitem.cpython-36.opt-1.pyc
%{python3_sitelib}/carcano/foolist/__pycache__/foolistitem.cpython-36.pyc
%{python3_sitelib}/carcano/foolist/foolist.py
%{python3_sitelib}/carcano/foolist/foolistitem.py
%{python3_sitelib}/carcano_foolist-%{_version}.dist-info/INSTALLER
%{python3_sitelib}/carcano_foolist-%{_version}.dist-info/METADATA
%{python3_sitelib}/carcano_foolist-%{_version}.dist-info/RECORD
%{python3_sitelib}/carcano_foolist-%{_version}.dist-info/WHEEL
%{python3_sitelib}/carcano_foolist-%{_version}.dist-info/top_level.txt

%files -n python3-%{srcname}
%config  %{_sysconfdir}/fooapp/logging.conf
%config  %{_sysconfdir}/rsyslog.d/fooapp.conf
/usr/bin/fooapp.py

%post -n python3-%{srcname}
systemctl restart rsyslog

%postun -n python3-%{srcname}
systemctl restart rsyslog

%changelog
* Mon Jun 14 2021 Marco Antonio Carcano <me@mydomain.tld>
First release
