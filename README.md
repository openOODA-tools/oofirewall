# oofirewall: Sovereign Firewall & Packet Filter Coordinator

<div align="center">

```
================================================================================
                               oofirewall
            Sovereign openOODA Firewall & Packet Filter
================================================================================
```

**Sovereign Firewall & Packet Filter Coordinator**  
*Declarative packet filtering coordinator backed by Linux nftables and firewalld.*  
*Two Faces, One Engine:* Modern POSIX terminal ergonomics • Streaming JSON-RPC 2.0 MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()
[![Release: v0.2.0](https://img.shields.io/badge/Release-v0.2.0-blue.svg)](https://github.com/openOODA-tools/oofirewall/releases/tag/v0.2.0)

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oofirewall/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oofirewall-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oofirewall/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oofirewall/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oofirewall-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oofirewall/uninstall.sh | bash -s -- --uninstall
```

---

## 2. CLI Usage

```
usage: oofirewall [options] [--zone ZONE]

Declarative packet filtering coordinator backed by Linux nftables and firewalld.

POSIX & firewalld Options:
  -z, --zone ZONE       target firewall zone (default: public)
      --list-all        list all allowed interfaces, services, and ports for zone
      --generate-xml    generate firewalld XML zone definition
      --generate-nft    compile declarative Linux nftables ruleset
      --audit           audit firewall configuration against Fedora Server standards
      --add-port P/PR   plan port opening mutation (e.g. 8080/tcp)
      --add-service SVC plan service opening mutation (e.g. cockpit, http)
  -j, --json            output structured records as JSON
  -D, --demo            interactive multi-zone firewall showcase
      --test            execute internal subsystem verification suite
      --mcp             run as Model Context Protocol JSON-RPC stdio server
  -v, --version         output version information and exit
      --help            display this help and exit
```

### Examples
```bash
# Inspect default public zone configuration
oofirewall

# Inspect trusted zone
oofirewall --zone trusted

# Generate firewalld XML zone configuration
oofirewall --generate-xml

# Compile declarative Linux nftables ruleset
oofirewall --generate-nft

# Audit system against Fedora Server conventions (cockpit, firewalld, SSH)
oofirewall --audit

# Output structured zone configuration as JSON
oofirewall -j
```

---

## 3. Model Context Protocol (MCP)

When invoked with `--mcp`, `oofirewall` runs a JSON-RPC 2.0 stdio server providing streaming structured tools for AI coding agents:

```bash
oofirewall --mcp
```

### Registered Tools
| Tool Name | Parameters | Description |
|---|---|---|
| `firewall_inspect_rules` | `zone` (string) | Inspects active ports, services, and policies for a target zone |
| `firewall_ruleset` | `format` (string: "nftables" or "xml") | Compiles declarative ruleset into Linux nftables or firewalld XML format |
| `firewall_plan_change` | `zone` (string), `action` (string), `target` (string) | Plans a declarative mutation to open/close ports or services |
| `firewall_zones` | *(none)* | Lists all configured firewall zones and basic summaries |
| `firewall_audit` | *(none)* | Audits current firewall configuration against Fedora Server security standards |
| `firewall_demo` | *(none)* | Runs interactive multi-zone firewall configuration showcase |

---

## 4. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`, `&NetCap`). Physical absence of ambient disk or network leakage.
* **Fedora Server Conventions:** Seamless integration with `firewalld` XML zones, Linux `nftables` tables, and Cockpit web console port (9090).
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 5. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
