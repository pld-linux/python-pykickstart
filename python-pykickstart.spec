#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define		module	pykickstart
Summary:	A Python 2 library for manipulating kickstart files
Summary(pl.UTF-8):	Biblioteka Pythona 2 do operowania na plikach kickstart
Name:		python-%{module}
Version:	3.32
Release:	6
License:	GPL v2
Group:		Libraries/Python
Source0:	https://github.com/pykickstart/pykickstart/archive/r%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	3dc66875645787f3b390d2cb55977c8c
URL:		https://fedoraproject.org/wiki/pykickstart
BuildRequires:	gettext-tools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_duplicate_files_terminate_build	0

%description
Pykickstart is a Python 2 and Python 3 library consisting of a data
representation of kickstart files, a parser to read files into that
representation, and a writer to generate kickstart files.

%description -l pl.UTF-8
Pykickstart to biblioteka Pythona 2 i Pythona 3, składająca się z
reprezentacji danych plików kickstart, parsera do odczytu plików do
tej reprezentacji oraz generatora plików kickstart.

%package -n python3-%{module}
Summary:	A Python 3 library for manipulating kickstart files
Summary(pl.UTF-8):	Biblioteka Pythona 3 do operowania na plikach kickstart
Group:		Libraries/Python

%description -n python3-%{module}
Pykickstart is a Python 2 and Python 3 library consisting of a data
representation of kickstart files, a parser to read files into that
representation, and a writer to generate kickstart files.

%description -n python3-%{module} -l pl.UTF-8
Pykickstart to biblioteka Pythona 2 i Pythona 3, składająca się z
reprezentacji danych plików kickstart, parsera do odczytu plików do
tej reprezentacji oraz generatora plików kickstart.

%prep
%setup -q -n %{module}-r%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%{__make} -C po

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%{__make} -C po install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_NLS_DIR=$RPM_BUILD_ROOT%{_localedir}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst docs/{kickstart-docs.rst,programmers-guide}
%if 0
# TODO: package as *-2 or in -tools package?
%attr(755,root,root) %{_bindir}/ksflatten
%attr(755,root,root) %{_bindir}/ksshell
%attr(755,root,root) %{_bindir}/ksvalidator
%attr(755,root,root) %{_bindir}/ksverdiff
%{_mandir}/man1/ksflatten.1*
%{_mandir}/man1/ksshell.1*
%{_mandir}/man1/ksvalidator.1*
%{_mandir}/man1/ksverdiff.1*
%endif
%{py_sitescriptdir}/pykickstart
%{py_sitescriptdir}/pykickstart-%{version}-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst docs/{kickstart-docs.rst,programmers-guide}
%attr(755,root,root) %{_bindir}/ksflatten
%attr(755,root,root) %{_bindir}/ksshell
%attr(755,root,root) %{_bindir}/ksvalidator
%attr(755,root,root) %{_bindir}/ksverdiff
%{_mandir}/man1/ksflatten.1*
%{_mandir}/man1/ksshell.1*
%{_mandir}/man1/ksvalidator.1*
%{_mandir}/man1/ksverdiff.1*
%{py3_sitescriptdir}/pykickstart
%{py3_sitescriptdir}/pykickstart-%{version}-*.egg-info
%endif
