Summary:	A frontend to cdrdao, cdrecord, mpg123, ogg123, and normalize
Summary(pl):	Frontend do cdrdao, cdrecord, mpg123, ogg123 i normalize
Name:		burncdda
Version:	1.2.9
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	http://thenktor.bei.t-online.de/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	236271f56fa3e573ad2c5d3b398bff94
URL:		http://thenktor.bei.t-online.de/burncdda/
Requires:	/bin/bash
Requires:	cdrdao
Requires:	cdrecord
Requires:	dialog
Requires:	mp3_check
Requires:	mpg123
Requires:	normalize
Requires:	sox
Requires:	vorbis-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
burnCDDA is a console based frontend to cdrdao, cdrecord, mpg123,
ogg123, normalize and mp3_check written in sh. It can be used to copy
audio CDs or to create audio CDs from a m3u playlist

%description -l pl
burnCDDA jest dzia³aj±c± na terminalu nak³adk± do programów cdrdao,
cdrecord, mpg123, ogg123, normalize i mp3_check, napisan± w sh. Mo¿e
byæ u¿ywana do kopiowania p³yt CD Audio oraz tworzenia ich z playlist
m3u.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1}

sed "s|/bin/sh|/bin/bash|" burncdda > $RPM_BUILD_ROOT%{_bindir}/burncdda
install burncdda.conf $RPM_BUILD_ROOT%{_sysconfdir}
install %{name}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "Please edit %{_sysconfdir}/burncdda.conf now!"

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/burncdda.conf
