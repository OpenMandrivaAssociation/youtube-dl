# (mandian)
# use python module instead of one single zipped binary
# - required by youtube-dl-pyqt -
%bcond python_module	1
# enable tests would need a huge amount of downloads
%bcond tests		0
# youtube-dl stopped making releases in 2021 -- the latest release
# can't even talk to youtube as of February 2023.
# so use the nightly releases
%bcond use_nightly	1

Summary:	Small command-line program to download videos from YouTube
Name:		youtube-dl
Version:	2025.03.11
Release:	1
License:	Public Domain and GPLv2+
Group:		Video
Url:		https://ytdl-org.github.io/youtube-dl/index.html
%if %{with use_nightly}
Source0:	https://github.com/ytdl-org/ytdl-nightly/archive/%{version}/ytdl-nightly-%{version}.tar.gz
%else
Source0:	https://github.com/ytdl-org/youtube-dl/archive/refs/heads/master/%{name}-%{version}.tar.gz
%endif
Patch0:		youtube-dl-2021.12.17-fix_python_setup.patch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(nose)
%if %{with python_module}
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
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
%if %{with python_module}
%{py_puresitedir}/youtube_dl-*.*-info
%endif
#optional %{_mandir}/man1/%{name}.1*
%optional %{_datadir}/zsh/site-functions/%{name}.zsh
%optional %config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}.bash-completion
%optional %config(noreplace) %{_sysconfdir}/fish/completions/%{name}.fish

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 %{?with_use_nightly:-n ytdl-nightly-%{version}}
# We currently don't have pandoc, so let's work around it,
# missing docs is a nuisance, but not a showstopper given
# the information can be found on the net
sed -i -e 's,pandoc,true,g' Makefile
sed -i -e '/install -m.*youtube-dl\.1/d' Makefile

%build
%if %{with python_module}
%make_build supportedsites youtube-dl.1 youtube-dl.bash-completion youtube-dl.zsh youtube-dl.fish
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

