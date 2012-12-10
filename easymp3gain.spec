%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Name:		easymp3gain
Version:	0.5.0
Release:	%mkrel 2
License:	GPLv2
Summary:	Graphical user interface for MP3Gain, AACGain and VorbisGain (GTK2)
Group:		Sound
URL:		http://easymp3gain.sourceforge.net
BuildRequires:	fpc
BuildRequires:	lazarus
BuildRequires:	glib2-devel
BuildRequires:	gtk2-devel
BuildRequires:	gdk-pixbuf-devel
Source0:	%{name}-%{version}.src.tar.gz
Patch0:		easymp3gain-cpu.patch
Requires:	mp3gain
Requires:	vorbisgain

%description
easyMP3Gain is a graphical user interface for MP3Gain, AACGain and VorbisGain. 
The Interface looks similar to the one available for Windows. 
It's a native GTK/GTK+ application, so it runs on Linux and FreeBSD/OpenBSD.

%prep
%setup -q
%ifarch %{ix86}
%patch0 -p1
%endif

%build
%__make all

%install
%__rm -rf %{buildroot}
./install.sh DESTDIR=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png



%changelog
* Wed Feb 22 2012 Andrey Bondrov <abondrov@mandriva.org> 0.5.0-2mdv2011.0
+ Revision: 779252
- Disable debug package
- Update file list
- imported package easymp3gain


* Fri Dec 31 2010 Andrey Bondrov <bondrov@math.dvgu.ru> 0.5.0-69.1mib2010.2
- New version

* Sun May 31 2009 Andrey Bondrov <bondrov@math.dvgu.ru> 0.4.2-69.1mib2009.1
- First build for MIB users