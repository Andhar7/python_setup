#!/usr/bin/env python3
"""Verify development environment setup."""

import sys
import subprocess


def check_python():
    """Check Python a version."""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    if version.major == 3 and version.minor >= 11:
        print("✓ Python version is good!")
    else:
        print("✗ Please install Python 3.11 or higher")
    return version.major == 3 and version.minor >= 11


def check_pip():
    """Check pip installation."""
    try:
        import pip
        print(f"pip version: {pip.__version__}")
        print("✓ pip is installed!")
        return True
    except ImportError:
        print("✗ pip is not installed")
        return False


def check_git():
    """Check Git installation."""
    try:
        result = subprocess.run(['git', '--version'],
                                capture_output=True, text=True)
        print(result.stdout.strip())
        print("✓ Git is installed!")
        return True
    except FileNotFoundError:
        print("✗ Git is not installed")
        return False


def check_postgresql_inside_project():
    """Check Postgres installation."""
    try:
        result = subprocess.run(['psql', '--version'],
                                capture_output=True, text=True)
        print(result.stdout.strip())
        print("✓ Postgres is installed inside the project!")
        return True
    except FileNotFoundError:
        print("✗ Postgres is not installed inside the project")
        return False


def check_postgresql():
    """Check Postgres installation."""
    try:
        # Try multiple possible commands for Postgres
        commands = [
            ['psql', '--version'],
            ['/usr/local/bin/psql', '--version'],
            ['/opt/homebrew/bin/psql', '--version'],
            ['postgres', '--version']
        ]

        for cmd in commands:
            try:
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode == 0:
                    print(result.stdout.strip())
                    print("✓ Postgres is installed!")
                    return True
            except FileNotFoundError:
                continue

        # If we can try to connect to the running instance
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        if 'postgres' in result.stdout:
            print("✓ Postgres process is running!")
            return True

        print("✗ Postgres is not installed or not in PATH")
        return False
    except Exception as e:
        print(f"✗ Error checking Postgres: {e}")
        return False


def check_venv():
    """Check if running in a virtual environment."""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✓ Running in virtual environment!")
        return True
    else:
        print("✗ Not running in virtual environment")
        print("  Create one with: python -m venv venv")
        print("  Activate with: source venv/bin/activate (Unix) or venv\\Scripts\\activate (Windows)")
        return False


def check_out():
    """Run all checks."""
    print("Development Environment Verification")
    print("=" * 40)

    checks = [
        ("Python", check_python),
        ("pip", check_pip),
        ("Git", check_git),
        ("Postgres inside app", check_postgresql_inside_project),
        ("Postgres", check_postgresql),
        ("Virtual Environment", check_venv),
    ]

    results = []
    for name, check_func in checks:
        print(f"\nChecking {name}...")
        results.append(check_func())

    print("\n" + "=" * 40)
    if all(results):
        print("✓ All checks passed! Your environment is ready!")
    else:
        print("✗ Some checks failed. Please install missing components.")


if __name__ == "__check_out__":
    check_out()
