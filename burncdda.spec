Name:		burncdda
Version:	1.1
Release:	1
License:	GPL
Summary:	A frontend to cdrdao, cdrecord, mpg123, ogg123, and normalize.
Group:		Applications/Multimedia
Source0:	http://thenktor.bei.t-online.de/burncdda/%{name}-%{version}.tar.gz
Requires:	cdrdao, cdrecord, mpg123, normalize, vorbis-tools, sox, mp3_check
URL:		http://thenktor.bei.t-online.de/burncdda/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
burnCDDA is a console based frontend to cdrdao, cdrecord, mpg123,
ogg123, normalize and mp3_check written in sh. It can be used to copy
audio CDs or to create audio CDs from a m3u playlist

%description -l pl
burnCDDA jest nank³adk± konsolow± do programów cdrdao cdrecord mpg123
ogg123 umo¿liwia nagranie muzycznej p³yty cd .


%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}
install -m 755 burncdda $RPM_BUILD_ROOT/%{_bindir}

mkdir $RPM_BUILD_ROOT%{_sysconfdir}
install burncdda.conf $RPM_BUILD_ROOT%{_sysconfdir}

install -d $RPM_BUILD_ROOT/%{_mandir}/man1
install %{name}.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/%{name}.1.gz

gzip -9nf  CHANGELOG LICENSE
%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "Please edit /etc/burncdda.conf now!"

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%config(noreplace) /etc/burncdda.conf
