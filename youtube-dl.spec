Summary:	Small command-line program to download videos from YouTube
Name:		youtube-dl
Version:	2014.09.25
Release:	1
License:	Public Domain and GPLv2+
Group:		Video
Url:		http://rg3.github.com/youtube-dl/
Source0:	https://yt-dl.org/downloads/%{version}/youtube-dl-%{version}.tar.gz

BuildRequires:  pythonegg(nose)
BuildRequires:	pythonegg(setuptools)
Requires:	python
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
%doc LICENSE README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%config(noreplace) %{_sysconfdir}/fish/completions/%{name}.fish