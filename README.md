# WireGuard iOS Config Processor

A simple Windows tool that automatically converts ProtonVPN WireGuard config files to be compatible with iOS devices.

## What it does
This tool automates the manual process described in this [Reddit guide](https://www.reddit.com/r/ProtonVPN/comments/15x7q1q/guide_nextdns_proton_vpn_wireguard_doh3_on_ios/) for using ProtonVPN with NextDNS on iOS devices.

This tool modifies ProtonVPN `.conf` files to work properly on iOS by:
- Setting DNS to `0.0.0.0/32`
- Setting `AllowedIPs` ranges
- Generating a QR code for easy import into the WireGuard iOS app

## Quick Start

1. **Download** the latest `WireGuard-iOS-Processor.exe` from [Releases](../../releases)
2. **Drag and drop** any ProtonVPN `.conf` file onto the executable
3. **Scan** the generated QR code with your iOS WireGuard app

That's it! Your config is now iOS-ready.

## What you get

After processing, you'll have two new files:
- `your-config-iOSReady.conf` - Modified config file
- `your-config-iOSReady-QR.png` - QR code for iOS import

## Building from Source

### Requirements
- Windows 10/11

## Files
- `wireguard_processor.py` - Main program
- `requirements.txt` - Python dependencies

## License

MIT License - Feel free to use and modify as needed.

## Contributing

Issues and pull requests welcome! This is a simple tool, but improvements are always appreciated.
