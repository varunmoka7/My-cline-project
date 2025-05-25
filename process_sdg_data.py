import pandas as pd
import json
import os

def process_sdg_csv():
    try:
        # Load the SDG CSV (corrected path)
        csv_path = r'..\..\data\external\DATA_GoCarbonTracker\DATA GoCarbonTracker\Origin database\SDG-2000data.csv'
        print(f"Loading CSV from: {csv_path}")
        
        df = pd.read_csv(csv_path)
        print(f"Loaded {len(df)} rows and {len(df.columns)} columns")
        
        # Print column names for debugging
        print("Columns found:", list(df.columns[:10]))  # First 10 columns
        
        # Clean and standardize column names
        df.columns = [c.strip().replace(' ', '_').replace('"', '').lower() for c in df.columns]
        
        # Use 'Company' as the main company identifier
        company_col = 'company'
        if company_col not in df.columns:
            print("Available columns:", df.columns.tolist())
            return
            
        # Get unique companies
        companies = df[company_col].dropna().unique()
        print(f"Found {len(companies)} unique companies")
        
        company_data = {}
        
        for i, company in enumerate(companies):
            if i % 100 == 0:
                print(f"Processing company {i+1}/{len(companies)}: {company}")
                
            company_df = df[df[company_col] == company]
            
            # Extract metadata from the first row
            first_row = company_df.iloc[0]
            
            # Define meta fields based on actual column names
            meta_fields = {
                'headquarters': 'headquarters',
                'region': 'region', 
                'income_group': 'income_group',
                'ownership': 'ownership',
                'industry': 'wba_industry',
                'sbti_2024': 'sbti_2024',
                'sbti_2023': 'sbti_2023',
                'isin': 'isin',
                'ticker': 'ticker',
                'website': 'website'
            }
            
            meta = {}
            for key, col in meta_fields.items():
                meta[key] = str(first_row[col]) if col in company_df.columns and pd.notna(first_row[col]) else 'N/A'
            
            # Convert all records to dict
            records = company_df.to_dict(orient='records')
            
            company_data[company] = {
                'name': company,
                **meta,
                'records': records,
                'record_count': len(records)
            }
        
        # Save to JSON
        output_file = 'sdg_companies_data.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(company_data, f, indent=2, default=str)
        
        print(f"Successfully exported {len(company_data)} companies to {output_file}")
        print(f"Sample company: {list(company_data.keys())[0]}")
        
    except Exception as e:
        print(f"Error processing SDG data: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    process_sdg_csv()
