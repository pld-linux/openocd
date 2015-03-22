# https://sourceforge.net/apps/trac/openocd/ticket/51
#
# Conditional build:
%bcond_without	libftdi	# use libftdi instead of libftd2xx
%bcond_without	system_jimtcl

Summary:	Free and Open On-Chip Debugging, In-System Programming and Boundary-Scan Testing
Name:		openocd
Version:	0.6.1
Release:	3
License:	GPL
Group:		Applications
Source0:	http://downloads.sourceforge.net/openocd/%{name}-%{version}.tar.bz2
# Source0-md5:	946421efc2414ff89bdaf3f588b230f8
URL:		http://openocd.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
%if %{with system_jimtcl}
BuildRequires:	jimtcl-devel
%endif
%if %{with libftdi}
BuildRequires:	libftdi-devel
%else
BuildRequires:	libftd2xx-devel
%endif
BuildRequires:	libtool
BuildRequires:	libusb-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautostrip	^/.*\.elf$

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
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--disable-werror \
	%{?with_system_jimtcl:--disable-internal-jimtcl} \
	--enable-ftdi \
%if %{with libftdi}
	--enable-ft2232_libftdi \
	--enable-usb_blaster_libftdi \
	--enable-presto_libftdi \
%else
	CPPFLAGS="-I/usr/include/ftd2xx %{rpmcppflags}" \
	--enable-ft2232_ftd2xx \
	--enable-usb_blaster_ftd2xx \
	--enable-presto_ftd2xx \
%endif
	--enable-amtjtagaccel \
	--enable-arm-jtag-ew \
	--enable-at91rm9200 \
	--enable-buspirate \
	--enable-dummy \
	--enable-ep93xx \
	--enable-gw16012 \
	--enable-ioutil \
	--enable-jlink \
	--enable-oocd_trace \
	--enable-parport \
	--enable-rlink \
	--enable-usbprog \
	--enable-stlink \
	--enable-vsllink

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_infodir}/%{name}.info*
%{_mandir}/man1/%{name}.1*
