# pdf_management
split and merge pdf

## Environment
### Installing python
This project was develop using Linux operating system. You can install python by using this command line.
```shell
sudo apt-get install python3
```
## Virtual environment
- Virtual environments allow you to create isolated environments for yoyrs Python projects, with their own dependencies and versions. it helps avoid conflicts between different projects.
- To create a virtual envirenment, open terminal or command prompt, navigate to yours project directory, and run:
```shell
python3 -m venv venv_pdf_management
```
*venv_pdf_management* is the name give to the virtual environment
- Activate the virtual environment
```shell
source venv_pdf_management/bin/activate
```
- To desactivate just type the command:
```shell
desactivate
```
## Installing packages
First, you need to install PyPDF2. You can do this using pip, Python's package installer:
```shell
pip install PyPDF2
```
## Starting the project
### Split pdf
- 1) Open the PDF file.
- 2) Iterate through each page of the PDF.
- 3) Create a new PDF writer object for each page.
- 4) Add the current page to the new PDF writer.
- 5) Write the new PDF file for each page.

### Merge pdf
To merge multiple PDF files into a single PDF, you can follow these steps:

- 1) Open each PDF file.
- 2) Create a new PDF writer object.
- 3) Iterate through each page of each PDF file.
- 4) Add each page to the new PDF writer.
- 5) Write the new PDF file.


### Extract pages
To extract multiples pages into a single PDF, you can follow these steps

- 1) Open the input PDF file.
- 2) Create a PDF reader object.
- 3) Create a PDF writer object.
- 4) Loop through the specified page range.
- 5) Add the page to the PDF writer object.
- 6) Write the extracted pages to the output PDF file

## Managing Dependencies

- Project dependencies can be manage by creating a *requirements.txt* file where the list of all the required packages along with their versions
```shell 
pip freeze > requirements.txt
```
- Install dependencies : 
```shell 
pip install -r requirements.txt
```