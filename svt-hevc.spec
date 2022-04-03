Summary:	Scalable Video Technology for HEVC Encoder
Summary(pl.UTF-8):	Koder Scalable Video Technology dla HEVC
Name:		svt-hevc
Version:	1.5.1
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/OpenVisualCloud/SVT-HEVC/releases
Source0:	https://github.com/OpenVisualCloud/SVT-HEVC/archive/v%{version}/SVT-HEVC-%{version}.tar.gz
# Source0-md5:	cc41d3975610781f70527faa567c6a30
URL:		https://github.com/OpenVisualCloud/SVT-HEVC
BuildRequires:	cmake >= 3.5
BuildRequires:	libstdc++-devel >= 6:5.4
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	yasm >= 1.2.0
Requires:	cpuinfo(sse2)
ExclusiveArch:	%{x8664} x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Scalable Video Technology for HEVC Encoder (SVT-HEVC Encoder) is
an HEVC-compliant encoder library core that achieves excellent
density-quality tradeoffs, and is highly optimized for Intel(R)
Xeon(TM) Scalable Processor and Xeon(TM) D processors.

%description -l pl.UTF-8
Koder Scalable Video Technology dla HEVC (koder SVT-HEVC) to
podstawowa biblioteka kodera zgodnego z HEVC, osiągająca świetny
współczynnik gęstości do jakości, znacząco zoptymalizowana pod kątem
procesorów Intel(R) Xeon(TM) Scalable Processor oraz Xeon(TM) D.

%package devel
Summary:	Header files for SVT-HEVC library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SVT-HEVC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for SVT-HEVC library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SVT-HEVC.

%prep
%setup -q -n SVT-HEVC-%{version}

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.md NOTICES.md README.md 
%attr(755,root,root) %{_bindir}/SvtHevcEncApp
%attr(755,root,root) %{_libdir}/libSvtHevcEnc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSvtHevcEnc.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSvtHevcEnc.so
%{_includedir}/svt-hevc
%{_pkgconfigdir}/SvtHevcEnc.pc
