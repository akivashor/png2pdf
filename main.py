
import os
import sys
import zipfile
from files_handler import get_files_list
from convert import convert_png_to_pdf, convert_png_to_pdf_2

SCRIPT_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))


def main():
    zip_folder = sys.argv[1]
    zip_files = get_files_list(zip_folder, extension='.zip', full_path=True)
    for zip_file in zip_files:
        new_folder_name = os.path.basename(zip_file).replace('.zip', '')
        png_path = os.path.join(zip_folder, new_folder_name)
        if not os.path.exists(png_path):
            os.makedirs(png_path)
        with zipfile.ZipFile(zip_file, 'r') as zip:
            zip.extractall(png_path)
            print(f'unzipped to {png_path}')

            files = get_files_list(png_path, extension='.png', full_path=True)
            if files:
                for file in files:
                    out_path = convert_png_to_pdf_2(file)
                    print(out_path)
                print('Saved all converted pdfs to original folder.')


if __name__ == '__main__':
    main()

