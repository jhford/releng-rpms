%define realname python27
%define pyver 2.7
%define pyrel 2
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
# from http://pkgs.fedoraproject.org/gitweb/?p=python.git;a=summary
Patch1:     python-2.7-lib64-sysconfig.patch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
%{realname} %{version}-%{release} for Mozilla Release Engineering infrastructure

%prep
%setup -q -n Python-%{pyver}.%{pyrel}
%patch0
%patch1 -p1


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make altinstall DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%_prefix/*



%changelog
