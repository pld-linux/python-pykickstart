%define 	module	pykickstart
Summary:	A python library for manipulating kickstart files
Name:		python-%{module}
Version:	1.99.30
Release:	1
License:	GPL v2
Group:		Libraries/Python
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/pykickstart/%{module}-%{version}.tar.gz/b9c78c95c6233b69f696ce4b8ea9407e/%{module}-%{version}.tar.gz
# Source0-md5:	b9c78c95c6233b69f696ce4b8ea9407e
URL:		http://fedoraproject.org/wiki/pykickstart
BuildRequires:	gettext-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
#BuildRequires:	transifex-client
Requires:	python-urlgrabber
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pykickstart package is a Python library for manipulating kickstart
files.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build
%{__make} -C po

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%{__make} -C po install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean
%find_lang %{module}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{module}.lang
%defattr(644,root,root,755)
%doc README ChangeLog docs/programmers-guide docs/kickstart-docs.txt
%attr(755,root,root) %{_bindir}/ksvalidator
%attr(755,root,root) %{_bindir}/ksflatten
%attr(755,root,root) %{_bindir}/ksverdiff
%dir %{py_sitescriptdir}/pykickstart
%dir %{py_sitescriptdir}/pykickstart/commands
%dir %{py_sitescriptdir}/pykickstart/handlers
%{py_sitescriptdir}/pykickstart/*.py[co]
%{py_sitescriptdir}/pykickstart/commands/*.py[co]
%{py_sitescriptdir}/pykickstart/handlers/__init__.py[co]
%{py_sitescriptdir}/pykickstart/handlers/control.py[co]
%{py_sitescriptdir}/pykickstart/handlers/f1[0-9].py[co]
%{py_sitescriptdir}/pykickstart/handlers/f[7-9].py[co]
%{py_sitescriptdir}/pykickstart/handlers/fc[3-6].py[co]
%{py_sitescriptdir}/pykickstart/handlers/rhel[3-7].py[co]
%{py_sitescriptdir}/pykickstart-%{version}-*.egg-info
