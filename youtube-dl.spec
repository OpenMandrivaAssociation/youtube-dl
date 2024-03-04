# (mandian) use python module instead of
# one single zipped binary
# - required by youtube-dl-pyqt -
%bcond_without python_module
# enable testss would need a huge amount of downloads
%bcond_with tests

Summary:	Small command-line program to download videos from YouTube
Name:		youtube-dl
# youtube-dl stopped making releases in 2021 -- the latest release
# can't even talk to youtube as of February 2023.
# So we either package a git snapshot or force people onto the
# yt-dlp fork...
Version:	2024.03.04
Release:	1
License:	Public Domain and GPLv2+
Group:		Video
Url:		https://ytdl-org.github.io/youtube-dl/index.html
Source0:	https://github.com/ytdl-org/youtube-dl/archive/refs/heads/master.tar.gz
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
%doc README.md
%{_bindir}/%{name}
%{py_puresitedir}/youtube_dl
%{py_puresitedir}/youtube_dl-*.*-info
%optional %{_mandir}/man1/%{name}.1*
%optional %{_datadir}/zsh/site-functions/_youtube-dl
%optional %config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%optional %config(noreplace) %{_sysconfdir}/fish/completions/%{name}.fish

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-master
# We currently don't have pandoc, so let's work around it,
# missing docs is a nuisance, but not a showstopper given
# the information can be found on the net
sed -i -e 's,pandoc,true,g' Makefile
sed -i -e '/install -m.*youtube-dl\.1/d' Makefile

%build
%if %{with python_module}
%{py_build}
%else
%make_build
%endif

%install
%if %{with python_module}
%{py_install}

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
