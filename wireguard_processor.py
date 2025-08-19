#!/usr/bin/env python3
"""
WireGuard Config Processor for iOS
Processes ProtonVPN .conf files to make them iOS-ready
"""

import sys
import os
import re
import qrcode
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

def process_wireguard_config(file_path):
    """
    Process WireGuard config file for iOS compatibility
    """
    # Read the original config file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return False
    
    # Define the new values
    new_dns = "0.0.0.0/32"
    new_allowed_ips = ("0.0.0.1/32, 0.0.0.2/31, 0.0.0.4/30, 0.0.0.8/29, "
                      "0.0.0.16/28, 0.0.0.32/27, 0.0.0.64/26, 0.0.0.128/25, "
                      "0.0.1.0/24, 0.0.2.0/23, 0.0.4.0/22, 0.0.8.0/21, "
                      "0.0.16.0/20, 0.0.32.0/19, 0.0.64.0/18, 0.0.128.0/17, "
                      "0.1.0.0/16, 0.2.0.0/15, 0.4.0.0/14, 0.8.0.0/13, "
                      "0.16.0.0/12, 0.32.0.0/11, 0.64.0.0/10, 0.128.0.0/9, "
                      "1.0.0.0/8, 2.0.0.0/7, 4.0.0.0/6, 8.0.0.0/5, "
                      "16.0.0.0/4, 32.0.0.0/3, 64.0.0.0/2, 128.0.0.0/1")
    
    # Replace DNS field (case-insensitive)
    content = re.sub(r'^DNS\s*=.*$', f'DNS = {new_dns}', content, flags=re.MULTILINE | re.IGNORECASE)
    
    # Replace AllowedIPs field (case-insensitive)
    content = re.sub(r'^AllowedIPs\s*=.*$', f'AllowedIPs = {new_allowed_ips}', content, flags=re.MULTILINE | re.IGNORECASE)
    
    # Create new filename
    original_path = Path(file_path)
    new_filename = original_path.stem + "-iOSReady" + original_path.suffix
    new_file_path = original_path.parent / new_filename
    
    # Save the modified config
    try:
        with open(new_file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Modified config saved as: {new_file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")
        return False
    
    # Generate QR code
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(content)
        qr.make(fit=True)
        
        # Create QR code image
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_filename = original_path.stem + "-iOSReady-QR.png"
        qr_file_path = original_path.parent / qr_filename
        qr_image.save(qr_file_path)
        print(f"QR code saved as: {qr_file_path}")
        
    except Exception as e:
        print(f"Error generating QR code: {e}")
        return False
    
    print("Processing completed successfully!")
    return True

def show_message(title, message, is_error=False):
    """Show a message box"""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    if is_error:
        messagebox.showerror(title, message)
    else:
        messagebox.showinfo(title, message)
    root.destroy()

def main():
    """
    Main function - handles command line arguments
    """
    if len(sys.argv) != 2:
        show_message("Usage", 
                    "Drag and drop a .conf file onto this executable\n"
                    "Or run: python wireguard_processor.py <config_file.conf>", 
                    is_error=True)
        return
    
    config_file = sys.argv[1]
    
    # Validate file exists and has .conf extension
    if not os.path.exists(config_file):
        show_message("File Not Found", 
                    f"Error: File '{config_file}' does not exist.", 
                    is_error=True)
        return
    
    if not config_file.lower().endswith('.conf'):
        show_message("Invalid File Type", 
                    "Error: File must have .conf extension.", 
                    is_error=True)
        return
    
    success = process_wireguard_config(config_file)
    
    if success:
        show_message("Success!", 
                    "✓ Configuration processed successfully!\n"
                    "✓ iOS-ready config file created\n"
                    "✓ QR code generated for easy import")
    else:
        show_message("Processing Failed", 
                    "✗ Processing failed. Please check the file format.", 
                    is_error=True)

if __name__ == "__main__":
    main()