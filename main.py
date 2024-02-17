from manage_pdf import split_pdf, merge_pdf

def main():
    split = "Split pdf document"
    merge = "Merge pdf"
    end_while = 0
    input_folder = 'input_folder'
    output_pdf_path = 'merged_output.pdf'
    input_pdf_path = 'input.pdf'
    output_folder = 'output_folder'
    while end_while == 0:
        print(f"Make a choice\n 1) {split}\n 2) {merge} \n")
        choix = input()
        try:
            if(int(choix)==1):
                # Appeler les fonctions pour gérer les PDF
                split_pdf(input_pdf_path, output_folder)
                end_while = 1
            elif int(choix)==2:
                  merge_pdf(input_folder, output_pdf_path)
                  end_while = 1
            else:
                print("Invalid input. Please enter a valid choice.")
        except ValueError:
            if choix.lower() in split.lower() :
                # Appeler les fonctions pour gérer les PDF
                split_pdf(input_pdf_path, output_folder)
                end_while = 1
            elif choix.lower() in merge.lower() :
                merge_pdf(input_folder, output_pdf_path)
                end_while = 1

            else:
                print("Invalid input. Please enter a valid choice.")
        except Exception as e:
            print("An error occured: ", e)
            end_while = 1

if __name__ == "__main__":
    main()
