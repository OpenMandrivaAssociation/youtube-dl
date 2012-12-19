Name:		youtube-dl
Version:	2012.12.11
Release:	1
Summary:	Small command-line program to download videos from YouTube
License:	Public Domain and GPLv2
Group:		Video
URL:		http://rg3.github.com/youtube-dl/
Source0:	https://github.com/rg3/youtube-dl/raw/%{version}/%{name}
#man page from Debian by Rogerio Brito <rbrito@users.sf.net>, licensed under GPLv2
Source1:	%{name}.1.gz
BuildArch:	noarch
Requires:	python

%description
Small command-line program to download videos from YouTube.

%prep
#nothing

%build
#nothing

%install
%__install -D -p -m 755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}

#man page by Rogerio Brito <rbrito@users.sf.net>, licensed under GPLv2 - from a Debian package
%__install -D -p -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1.gz

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*


