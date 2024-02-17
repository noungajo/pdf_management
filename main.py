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

input_folder = '/home/benjojo/Documents/projets/pdf_management'
output_folder = '/home/benjojo/Documents/projets/pdf_management' 