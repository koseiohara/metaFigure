# Metadata Manager for PDF and PNG files
Metadata reader and writer in Python  

## Test Environment
CentOS7  
Python 3.7.7  
PyPDF2 3.0.1  
PIL 9.5.0  
PDF version 1.4  

## Install
Install the source codes from GitHub
```sh
$ git clone https://github.com/koseiohara/metaFigure.git
$ cd metaFigure
$ make install
```
Source files will be copied to the directory specified by `INSTALL` in the `Makefile`.
Add the directory to the environment paths `PATH` and `PYTHONPATH`.  

The `Makefile` can be used for uninstalling the tools
```sh
$ make uninstall
```

## Tools
- [add_figinfo](#add)
- [figinfo](#figinfo)

## add_figinfo<a id="add"></a>
Adding new metadata to a PDF or PNG.
This tool can be used as both a terminal command and a Python function.  

When this is used as a terminal command, `FigureName`, `Key`, and `Description` are needed as arguments
```sh
$ add_figinfo FigureName Key Description
```
`FigureName` is the file name of the target PDF/PNG.
`Key` is the name of metadata.
`Description` is the description identified by `Key`  

Similary, when this is used as a function in Python, `FigureName`, `Key`, and `Description` are needed as arguments
```python
add_figinfo(FigureName, Key, Description)
```
Matadata will be added to the target file.

## figinfo<a id="figinfo"></a>
Extracting and Displaying the metadata from PDF/PNG.
This tool can be used only on the terminal.
```sh
$ figinfo FigureName [Key]
```
If `Key` is omitted, all descriptions will be displaied.
Otherwise, the specified metadata will be displaied.

