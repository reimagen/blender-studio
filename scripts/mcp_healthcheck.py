#!/usr/bin/env python3
"""Basic connectivity check for local Blender MCP bridge."""

import socket
import sys


HOST = "127.0.0.1"
PORT = 9876
TIMEOUT_SEC = 2.0


def main() -> int:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT_SEC)

    try:
        sock.connect((HOST, PORT))
    except OSError as exc:
        print(f"[FAIL] Could not connect to Blender MCP at {HOST}:{PORT}")
        print(f"Reason: {exc}")
        print("Tip: Start Blender and enable your MCP bridge/add-on first.")
        return 1
    finally:
        sock.close()

    print(f"[OK] Blender MCP is reachable at {HOST}:{PORT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
