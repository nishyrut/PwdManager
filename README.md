# PwdManager
A simple password manager using python alongside cryptocode and pwinput modules

> [!CAUTION]
> This is a password manager made for educational purpose. This password manager does encrypt and decrypt, but is not audited regularly and lacks many security features as mentioned below. For a reliable password manager consider using regularly audited password managers like [bitwarden](https://bitwarden.com/) or [keepass](https://keepassxc.org/)

# Features
* Secure password input using pwinput module
* Flexible CLI based password manager
* Encrypts and Decrypts thanks to cryptocode
* Multi-User Password managing capability
* Allows addition of custom columns
* Uses additional command to view password preventing accidental shoulder attacks
* A single file that stores all information, meaning it is highly portable as long as the single file exists

# Drawbacks
* Does not include hashing and salting
* Does not provide a way to store additional security features like TOTP
* Does not provide a secure way to copy, a malicious program that has access to clipboard can see the password
* Does not mitigate advanced attacks by clearing out memory of passwords, which can be retrieved using cold boot
* Stores in pickle format, any malicious attacker gaining access that replaces the pickle file can execute arbitrary commands
