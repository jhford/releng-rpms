%define realname python26
%define pyver 2.6
%define pyrel 7
%define _prefix /tools/%{realname}-%{version}

Name:       mozilla-%{realname}
Version:	%{pyver}.%{pyrel}
Release:	1%{?dist}
Summary:	This is a packaging of %{realname} %{version}-%{release} for Mozilla Release Engineering infrastructure

Group:		mozilla
License:	tbd
URL:		http://python.org
Source0:	http://python.org/ftp/python/%{pyver}.%{pyrel}/Python-%{pyver}.%{pyrel}.tar.bz2
Patch0:     python-2.6-fix-cgi.patch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
%{realname} %{version}-%{release} for Mozilla Release Engineering infrastructure

%prep
%setup -q -n Python-%{pyver}.%{pyrel}
%patch0


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make altinstall DESTDIR=$RPM_BUILD_ROOT
# This file doesn't seem to respect the _prefix
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/man/
# This file needs to writable for stripping
chmod +w $RPM_BUILD_ROOT/%{_libdir}/libpython%{pyver}.a


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%_prefix/*
%attr(555, -, -) %{_libdir}/libpython%{pyver}.a



%changelog
