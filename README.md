# pdf_management
split and merge pdf
## Installation
First, you need to install PyPDF2. You can do this using pip, Python's package installer:
```shell
pip install PyPDF2

```
## Split pdf
- 1) Open the PDF file.
- 2) Iterate through each page of the PDF.
- 3) Create a new PDF writer object for each page.
- 4) Add the current page to the new PDF writer.
- 5) Write the new PDF file for each page.

## Merge pdf
To merge multiple PDF files into a single PDF, you can follow these steps:

- 1) Open each PDF file.
- 2) Create a new PDF writer object.
- 3) Iterate through each page of each PDF file.
- 4) Add each page to the new PDF writer.
- 5) Write the new PDF file.


## Extract pages
To extract multiples pages into a single PDF, you can follow these steps

- 1) Open the input PDF file.
- 2) Create a PDF reader object.
- 3) Create a PDF writer object.
- 4) Loop through the specified page range.
- 5) Add the page to the PDF writer object.
- 6) Write the extracted pages to the output PDF file