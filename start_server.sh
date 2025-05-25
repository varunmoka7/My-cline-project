#!/bin/bash
# SD3 Dashboard Quick Start Script

echo "========================================="
echo "    SD3 - SDG Companies Dashboard"
echo "========================================="
echo ""
echo "Data: 2000+ companies with SDG metrics"
echo "Features: SBTi status, emissions, revenue trends"
echo ""

# Check if Python is available
if ! command -v python &> /dev/null; then
    echo "Python not found. Please install Python to run the server."
    exit 1
fi

# Start server
echo "Starting HTTP server on port 8001..."
cd "$(dirname "$0")"
python -m http.server 8001
