#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module [all functionality present in 3.5+]

Summary:	Backport of recent additions to the 'collections.abc' module
Summary(pl.UTF-8):	Backport ostatnich rozszerzeń modułu 'collections.abc'
Name:		python-backports_abc
Version:	0.4
Release:	1
License:	PSF
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/pypi/backports_abc
Source0:	https://pypi.python.org/packages/source/b/backports_abc/backports_abc-%{version}.tar.gz
# Source0-md5:	0b65a216ce9dc9c1a7e20a729dd7c05b
URL:		https://github.com/cython/backports_abc
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-modules < 1:3.5
%endif
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Backport of recent additions to the 'collections.abc' module.

%description -l pl.UTF-8
Backport ostatnich rozszerzeń modułu 'collections.abc'.

%package -n python3-backports_abc
Summary:	Backport of recent additions to the 'collections.abc' module
Summary(pl.UTF-8):	Backport ostatnich rozszerzeń modułu 'collections.abc'
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2
Requires:	python3-modules < 1:3.5

%description -n python3-backports_abc
Backport of recent additions to the 'collections.abc' module.

%description -n python3-backports_abc -l pl.UTF-8
Backport ostatnich rozszerzeń modułu 'collections.abc'.

%prep
%setup -q -n backports_abc-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%{py_sitescriptdir}/backports_abc.py[co]
%{py_sitescriptdir}/backports_abc-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-backports_abc
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%{py3_sitescriptdir}/backports_abc.py
%{py3_sitescriptdir}/__pycache__/backports_abc.cpython-*.py[co]
%{py3_sitescriptdir}/backports_abc-%{version}-py*.egg-info
%endif
