Summary:	Small command-line program to download videos from YouTube
Name:		youtube-dl
Version:	2015.01.16
Release:	2
License:	Public Domain and GPLv2+
Group:		Video
Url:		http://rg3.github.com/youtube-dl/
Source0:	https://yt-dl.org/downloads/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pythonegg(nose)
BuildRequires:	pythonegg(setuptools)
#for tests
BuildRequires:	ffmpeg

Requires:	python2
Suggests:	ffmpeg

BuildArch:	noarch

%description
Small command-line program to download videos from YouTube.


%prep
%setup -qn %{name}

%build
%make


%install
%makeinstall DESTDIR=%{buildroot} \
             PREFIX=%{_prefix} \
             MANDIR=%{_mandir} 
            

%check
#make test

%files
%doc LICENSE README.txt 
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/zsh/site-functions/_youtube-dl
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%config(noreplace) %{_sysconfdir}/fish/completions/%{name}.fish