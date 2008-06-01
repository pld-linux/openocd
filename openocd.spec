#
%define snap 20080601
%define             no_install_post_strip 1

Summary:	Free and Open On-Chip Debugging, In-System Programming and Boundary-Scan Testing
Name:		openocd
Version:	0.%{snap}
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://ep09.pld-linux.org/~adasi/%{name}-%{snap}.tar.bz2
# Source0-md5:	34a10a23ecb366935babb44d8bc0a44a
URL:		http://openocd.berlios.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Open On-Chip Debugger (openocd) aims to provide debugging,
in-system programming and boundary-scan testing for embedded target
devices. The targets are interfaced using JTAG (IEEE 1149.1) compliant
hardware, but this may be extended to other connection types in the
future. Openocd currently supports Wiggler (clones), FTDI FT2232 based
JTAG interfaces, the Amontec JTAG Accelerator, and the Gateworks
GW1602. It allows ARM7 (ARM7TDMI and ARM720t), ARM9 (ARM920t, ARM922t,
ARM926ej-s, ARM966e-s), XScale (PXA25x, IXP42x) and Cortex-M3
(Luminary Stellaris LM3 and ST STM32) based cores to be debugged.
Flash writing is supported for external CFI compatible flashes (Intel
and AMD/Spansion command set) and several internal flashes (LPC2000,
AT91SAM7, STR7x, STR9x, LM3 and STM32x). Preliminary support for using
the LPC3180's NAND flash controller is included.

%prep
%setup -q -n %{name}-%{snap}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/openocd
%{_libdir}/openocd/*
%{_infodir}/openocd.info.gz
