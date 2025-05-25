# SD3 - SDG Companies Dashboard

This folder contains the SDG-based sustainability dashboard for analyzing 2000+ companies with comprehensive ESG metrics including SBTi status, CDP data, and multi-year sustainability performance.

## Quick Start

1. **Start the Server**: Double-click `start_sdg_server.bat` to launch the HTTP server
2. **Access Dashboard**: Open http://localhost:8001/sdg_dashboard.html in your browser
3. **Explore Data**: Use filters for region, industry, SBTi status, and search functionality

## Features

- **Company Selection**: Browse 2000+ companies from the SDG dataset
- **Advanced Filtering**: Filter by region, industry, SBTi status
- **Search Functionality**: Find companies by name quickly  
- **SDG Metrics**: View SBTi status, Scope 1+2 emissions, revenue, employees
- **Trend Analysis**: Revenue charts (2021-2023) and emissions breakdown
- **Data Export**: Export company data for further analysis
- **Modern UI**: ESG-themed design matching the main Tracable Database

## Data Source

- **File**: `SDG-2000data.csv` (2000+ companies)
- **Metrics**: SBTi status, CDP status, emissions (Scope 1+2+3), revenue, employees
- **Years**: Multi-year data (2021-2023) for trend analysis

## Files

- `sdg_dashboard.html` - Main dashboard interface
- `start_sdg_server.bat` - Quick server startup script
- `process_sdg_data.py` - Data processing utilities (optional)
