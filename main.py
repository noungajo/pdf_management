from manage_pdf import split_pdf, merge_pdf, extract_pages

def main():
    split = "Split pdf document"
    merge = "Merge pdf"
    extract = "Extract pages"
    end_while = 0
    input_folder = 'input_folder'
    output_pdf_path = 'merged_output.pdf'
    while end_while == 0:
        print(f"Make a choice\n 1) {split}\n 2) {merge} \n 3) {extract}")
        choix = input()
        try:
            if(int(choix)==1):
                # Appeler les fonctions pour gérer les PDF
                input_pdf_path = input("Enter the input pdf path ")
                output_folder = input("Enter the output folder ")
                split_pdf(input_pdf_path, output_folder)
                end_while = 1
            elif int(choix)==2:
                input_folder = input("Enter the input folder ")
                output_pdf_path = input("Enter the output pdf path ")
                merge_pdf(input_folder, output_pdf_path)
                end_while = 1
            elif int(choix) == 3:
                input_pdf_path = input("Enter the input pdf path ")
                output_pdf_path = input("Enter the output pdf path ")
                start_page = input("Enter the start page ")
                end_page = input("Enter the end page ")
                extract_pages(input_pdf_path, output_pdf_path, start_page, end_page)
                end_while = 1
            else:
                print("Invalid input. Please enter a valid choice.")
        except ValueError:
            if choix.lower() in split.lower() :
                # Appeler les fonctions pour gérer les PDF
                input_pdf_path = input("Enter the input pdf path ")
                output_folder = input("Enter the output folder ")
                split_pdf(input_pdf_path, output_folder)
                end_while = 1
            elif choix.lower() in merge.lower() :
                input_folder = input("Enter the input folder ")
                output_pdf_path = input("Enter the output pdf path ")
                merge_pdf(input_folder, output_pdf_path)
                end_while = 1
            elif choix.lower() in extract.lower():
                input_pdf_path = input("Enter the input pdf path ")
                output_pdf_path = input("Enter the output pdf path ")
                start_page = input("Enter the start page ")
                end_page = input("Enter the end page ")
                extract_pages(input_pdf_path, output_pdf_path, start_page, end_page)
                end_while = 1
            else:
                print("Invalid input. Please enter a valid choice.")
        except Exception as e:
            print("An error occured: ", e)
            end_while = 1

if __name__ == "__main__":
    main()


# Example usage:
input_pdf_path = 'input.pdf'  # Path to the input PDF file
output_pdf_path = 'output.pdf'  # Path to save the output PDF file
start_page = 2  # Start page (1-indexed)
end_page = 4  # End page (1-indexed)

# Extract pages 2 to 4 from the input PDF and save them to the output PDF
extract_pages(input_pdf_path, output_pdf_path, start_page, end_page)

# Example usage:
input_folder = '/home/benjojo/Documents/projets/pdf_management'
output_pdf_path = 'merged_output.pdf'  # Path to the merged output PDF file


# Example usage:
input_pdf_path = 'input.pdf'  # Path to the input PDF file
output_folder = '/home/benjojo/Documents/projets/pdf_management'  # Output folder to save the split PDFs
