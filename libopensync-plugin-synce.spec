Name: 	 	libopensync-plugin-synce
Version: 	0.22
Release: 	%{mkrel 2}
Summary: 	Windows Mobile 2003 and earlier plugin for OpenSync
License:	LGPLv2+
Group:		Office
URL:		http://www.opensync.org
Source0:	http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
# Oh look, again. - AdamW 2008/06
Patch0:		libopensync-plugin-synce-0.22-warning.patch
# Better plugin description to differentiate from the other plugin
# that handles newer devices - AdamW 2008/06
Patch1:		libopensync-plugin-synce-0.22-description.patch
# Set a nonsense file sync location by default. If the file sync
# location exists, the plugin seems to try and sync files even when
# this doesn't make any sense, like when syncing with Evolution, which
# breaks the sync. Setting the location as blank just tries to sync
# every file on the device, so let's use a nonsense folder name.
# - AdamW 2008/06
Patch2:		libopensync-plugin-synce-0.22-no_default_file.patch
BuildRequires:	libopensync-devel < 0.30
BuildRequires:	librra-devel
BuildRequires:	libsynce-devel
Requires:	libopensync >= 1:%{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise with
mobile devices based on Windows Mobile 2003 and earlier, via the SynCE
framework. For devices based on Windows Mobile 5 and later, use the
synce-opensync-plugin package.

%prep
%setup -q
%patch0 -p1 -b .warning
%patch1 -p1 -b .description
%patch2 -p1 -b .file
autoreconf -sfi

%build
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*
