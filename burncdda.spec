Summary:	A frontend to cdrdao, cdrecord, mpg123, ogg123, and normalize
Summary(pl):	Frontend do cdrdao, cdrecord, mpg123, ogg123 i normalize
Name:		burncdda
Version:	1.2.6
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://thenktor.bei.t-online.de/burncdda/%{name}-%{version}.tar.gz
# Source0-md5:	7568bf8b4e2dc6b3067aca9968a20f13
URL:		http://thenktor.bei.t-online.de/burncdda/
Requires:	cdrdao
Requires:	cdrecord
Requires:	mpg123
Requires:	normalize
Requires:	vorbis-tools
Requires:	sox
Requires:	mp3_check
Requires:	/bin/bash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
burnCDDA is a console based frontend to cdrdao, cdrecord, mpg123,
ogg123, normalize and mp3_check written in sh. It can be used to copy
audio CDs or to create audio CDs from a m3u playlist

%description -l pl
burnCDDA jest dzia�aj�c� na terminalu nak�adk� do program�w cdrdao,
cdrecord, mpg123, ogg123, normalize i mp3_check, napisan� w sh. Mo�e
by� u�ywana do kopiowania p�yt CD Audio oraz tworzenia ich z playlist
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
