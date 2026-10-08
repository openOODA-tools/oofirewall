Name:           oofirewall
Version:        0.2.0
Release:        1%{?dist}
Summary:        Sovereign declarative packet filtering and firewalld coordinator in pure openOODA.
License:        Apache-2.0
URL:            https://github.com/openOODA-tools/oofirewall
Source0:        oofirewall-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oofirewall is a sovereign declarative packet filtering and firewalld coordinator
written in pure openOODA, featuring zero ambient authority, firewalld zone
generation, nftables translation, and a streaming MCP JSON-RPC 2.0 stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oofirewall
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oofirewall-uninstall

%files
/usr/bin/oofirewall
/usr/bin/oofirewall-uninstall

%changelog
* Thu Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevation to v0.2.0 with firewalld zones, nftables rulesets, and streaming MCP
