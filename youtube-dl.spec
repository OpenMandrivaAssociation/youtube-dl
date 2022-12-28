# (mandian) use python module instead of
# one single zipped binary
# - required by youtube-dl-pyqt -
%bcond_without python_module
# enable testss would need a huge amount of downloads
%bcond_with tests

Summary:	Small command-line program to download videos from YouTube
Name:		youtube-dl
Version:	2021.12.17
Release:	2
License:	Public Domain and GPLv2+
Group:		Video
Url:		https://ytdl-org.github.io/youtube-dl/index.html
Source0:	https://yt-dl.org/downloads/%{version}/%{name}-%{version}.tar.gz
Patch0:		youtube-dl-2021.12.17-fix_python_setup.patch
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(nose)
%if %{with python_module}
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)
%endif
# tests
%if %{with tests}
BuildRequires:	ffmpeg
%endif

Requires:	python
Recommends:	ffmpeg

BuildArch:	noarch

%description
Small command-line program to download videos from YouTube and similar sites.

%files
%license LICENSE
%doc README.txt
%{_bindir}/%{name}
%{py_puresitedir}/youtube_dl
%{py_puresitedir}/youtube_dl-*.*-info
%{_mandir}/man1/%{name}.1*
%{_datadir}/zsh/site-functions/_youtube-dl
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%config(noreplace) %{_sysconfdir}/fish/completions/%{name}.fish

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}

%build
%if %{with python_module}
%{py_build}
%else
%make_build
%endif

%install
%if %{with python_module}
%{py_install}

# fix name
mv %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}{.bash-completion,}
mv %{buildroot}%{_datadir}/zsh/site-functions/{youtube-dl.zsh,_youtube-dl}

# remove unwanted
rm -fr %{buildroot}%{_datadir}/doc/youtube_dl/

%else
%make_install \
	DESTDIR=%{buildroot} \
	PREFIX=%{_prefix} \
	MANDIR=%{_mandir}
%endif

%check
%if %{with tests}
make test
%endif

