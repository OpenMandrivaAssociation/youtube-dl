Summary:	Small command-line program to download videos from YouTube
Name:		youtube-dl
Version:	2019.07.30
Release:	1
License:	Public Domain and GPLv2+
Group:		Video
Url:		http://rg3.github.com/youtube-dl/
Source0:	https://yt-dl.org/downloads/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	python3egg(nose)
BuildRequires:	python3egg(setuptools)
#for tests
BuildRequires:	ffmpeg

Requires:	python
Suggests:	ffmpeg

BuildArch:	noarch

%description
Small command-line program to download videos from YouTube and similar sites.

%files
%doc LICENSE README.txt 
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/zsh/site-functions/_youtube-dl
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%config(noreplace) %{_sysconfdir}/fish/completions/%{name}.fish

#-----------------------------------------------------------------------------

%prep
%setup -qn %{name}

%build
#python ./setup.py
%make_build


%install
%make_install DESTDIR=%{buildroot} \
	     PREFIX=%{_prefix} \
	     MANDIR=%{_mandir} 
            

%check
# This would need a huge amount of downloads.
#make test
