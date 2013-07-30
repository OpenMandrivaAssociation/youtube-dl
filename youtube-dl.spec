Summary:	Small command-line program to download videos from YouTube
Name:		youtube-dl
Version:	2013.07.25.2
Release:	1
License:	Public Domain and GPLv2
Group:		Video
Url:		http://rg3.github.com/youtube-dl/
Source0:	http://youtube-dl.org/downloads/%{version}/youtube-dl
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
install -D -p -m 755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}

#man page by Rogerio Brito <rbrito@users.sf.net>, licensed under GPLv2 - from a Debian package
install -D -p -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1.gz

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
