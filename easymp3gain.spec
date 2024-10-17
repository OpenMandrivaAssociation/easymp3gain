%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Graphical user interface for MP3Gain, AACGain and VorbisGain (GTK2)
Name:		easymp3gain
Version:	0.5.0
Release:	4
License:	GPLv2+
Group:		Sound
Url:		https://easymp3gain.sourceforge.net
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
Source0:	%{name}-%{version}.src.tar.gz
Patch0:		easymp3gain-cpu.patch
Patch1:		easymp3gain-0.5.0-desktop.patch
Patch2:		fix_missing_LazarusDir.diff
Patch3:		fix_missing_overload_on_AddTask.diff
BuildRequires:	fpc
BuildRequires:	lazarus
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
Requires:	mp3gain
Requires:	vorbisgain

%description
easyMP3Gain is a graphical user interface for MP3Gain, AACGain and VorbisGain.
The Interface looks similar to the one available for Windows.
It's a native GTK/GTK+ application, so it runs on Linux and FreeBSD/OpenBSD.

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q
%ifarch %{ix86}
%patch0 -p1
%endif
%patch1 -p0
%patch2 -p1
%patch3 -p1

%build
make all

%install
./install.sh DESTDIR=%{buildroot}


