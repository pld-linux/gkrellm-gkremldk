Summary:	GKrellmdk: GKrellM MLDonkey Plugin
Summary(pl.UTF-8):	Wtyczka MLDonkey dla GKrellM
Name:		gkrellm-gkremldk
Version:	0.9.6
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.tof2k.com/gkremldk/gkremldk-%{version}.tbz
# Source0-md5:	f9ccb855c3d876a843b50d816e53a8ff
URL:		http://www.tof2k.com/gkremldk/
BuildRequires:	autoconf
BuildRequires:	gkrellm-devel >= 2.0
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
Requires:	gkrellm >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gkremldk is a GKrellM plugin showing current mldonkey download/upload
rate, and to set the maximum of these.

%description -l pl.UTF-8
Gkremldk jest wtyczką do GKrellM pokazującą aktualną prędkość
transferu w mldonkey.

%prep
%setup -q -n gkremldk-%{version}

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D gkremldk.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins/gkremldk.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/gkremldk.so
