import os
import csv
from pathlib import Path

def process_data_folder():
    # Define paths
    data_folder = Path('data')
    output_csv = 'course_info.csv'
    
    # Prepare CSV file
    with open(output_csv, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Course Code', 'Professor Name', 'Academic Year', 'Term'])
        
        # Iterate through folders in data directory
        for folder in data_folder.iterdir():
            if folder.is_dir():
                # Extract academic year and term from folder name
                folder_parts = folder.name.split()
                if len(folder_parts) >= 2:
                    academic_year = folder_parts[0]  # AY23-24
                    term = folder_parts[1]           # T1
                    
                    # Process PDF files in the folder
                    for pdf_file in folder.glob('*.pdf'):
                        # Extract course code and professor name from filename
                        filename_parts = pdf_file.stem.split('_')
                        if len(filename_parts) >= 2:
                            course_code = filename_parts[0]        # COMM102
                            professor_name = ' '.join(filename_parts[1:])  # YEO SU LIN
                            
                            # Write to CSV
                            writer.writerow([course_code, professor_name, academic_year, term])

if __name__ == '__main__':
    process_data_folder()