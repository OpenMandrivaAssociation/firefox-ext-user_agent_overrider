Summary: Firefox extension
Name: firefox-ext-user_agent_overrider
Version: 0.4.1
Release: 1
License: MPL
Group:	Networking/WWW
URL: https://addons.mozilla.org/pl/firefox/addon/user-agent-overrider/
Source: user_agent_overrider-%{version}-fx.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox >= %{firefox_version}
BuildRequires: firefox-devel
Buildarch: noarch

%description
Extension for firefox.

%prep
%setup -q -c -n %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{firefox_extdir}/"
mkdir -p "%{buildroot}$extdir"
cp -af %SOURCE0 "%{buildroot}$extdir/$hash.xpi"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{firefox_extdir}


