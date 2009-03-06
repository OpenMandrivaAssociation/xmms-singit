%define name xmms-singit
%define version 0.0.8
%define release %mkrel 8

Summary:	 Lyric Displayer and editor plugin for XMMS
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		%{name}-%{version}.tar.bz2
License:	GPL
Group:		Sound
Url:		http://stud.fbi.fh-darmstadt.de/~glogow/
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	glib2-devel
BuildRequires:	gtk+1.2-devel
BuildRequires:	xmms-devel
BuildRequires:	id3lib-devel

%description
The SingIt Lyric Displayer is an XMMS plugin which displays
formatted lyrics, including id3v2xx lyrics.
It consists of the displayer and an integrated editor
which allows one to easily insert time stamps, edit the text,
and export & strip HTML.

%prep
%setup -q

%build
#we don't use libtool 1.5 yet
%define __libtoolize /bin/true
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/xmms/Visualization
%makeinstall libdir=$RPM_BUILD_ROOT/%{_libdir}/xmms/Visualization

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_libdir}/xmms/Visualization/libxmms_singit.so
%{_libdir}/xmms/Visualization/libxmms_singit.la
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/xmms-singit.mo

