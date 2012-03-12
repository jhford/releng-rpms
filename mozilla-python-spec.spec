# http://fedoraproject.org/wiki/Packaging:Python
# We do this to avoid stomping on distro-provided packages
%define realname @NAME@
# This is the 'real' name of the python to build with e.g. python26
%define pyrealname @PYNAME@
%define pyver @PYVER@
%define pyrel @PYREL@

# This is the top level directory of the python installation
# we'll use
%define pyhome /tools/%{pyrealname}-%{pyver}.%{pyrel}

# We redefine the standard RPM macros provided by the system
# since they are all wrong for what we want
%define __python %{pyhome}/bin/python%{pyver}
%define __python3 /bin/false
%define python_sitelib %{pyhome}/lib/python%{pyver}/site-packages
%define python_sitearch %{pyhome}/lib/python%{pyver}/site-packages
%define python3_sitelib /does/not/exist
%define python3_sitearch /does/not/exist
%define py3dir /does/not/exist

# We also want to install all custom software to alternate locations
%define _prefix /tools/%{realname}-%{version}

Name:       mozilla-%{pyrealname}-%{realname}
Version:	
Release:	1%{?dist}
Summary:	This is a packaging of %{realname} %{version}-%{release} for Mozilla Release Engineering infrastructure

Group:		mozilla
License:	
URL:		
Source0:	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  mozilla-%{pyrealname}
Requires:	    mozilla-%{pyrealname}


%description
%{realname} %{version}-%{release} for Mozilla Release Engineering infrastructure

%prep
# We have the -n because by default, rpmbuild will use %name-%version.
# Because we do %name of 'mozilla-%realname', we need a new default
%setup -q -n %{realname}-%{version}


%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --prefix=%{_prefix} --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES


%clean
rm -rf $RPM_BUILD_ROOT


%files -f INSTALLED_FILES
%defattr(-,root,root,-)

%changelog
