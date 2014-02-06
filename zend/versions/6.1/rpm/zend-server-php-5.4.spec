%global zend_base_dir /usr/local/zend-server-6-php-5.4/

Summary:        Zend web application server package
Name:           zend-server-php-5.4
Version:        6.1
Release:        4%{?dist}
Group:          Zend/Server
License:        Zend
URL:            http://www.zend.com
Source0:        zs6-binaries.tar.gz

%description
Zend Server is a complete, enterprise-ready Web Application Server for running
and managing PHP applications that require a high level of reliability,
performance and security.

%prep

%build

%install
cd %{buildroot}
tar xfz %{SOURCE0}

%files
%{zend_base_dir}

%changelog
* Thu Oct 10 2013 Troy Dawson <dawson@fnal.gov> 6.1-4
- New code with bugfixes

* Tue Oct 01 2013 Troy Dawson <dawson@fnal.gov> 6.1-3
- make sure var.orig are in this version

* Tue Oct 01 2013 Troy Dawson <dawson@fnal.gov> 6.1-2
- updated to latest version

* Mon Sep 23 2013 Troy Dawson <dawson@fnal.gov> 6.1-1
- Initial package

