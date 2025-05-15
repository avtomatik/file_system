# FileWorks

**FileWorks** is a Python-based utility suite designed for efficient file system operations, including file synchronization, transformation, and reporting. It provides a set of scripts to automate common file management tasks, making it easier to handle large volumes of files with minimal manual intervention.

## Features

* **File Synchronization**: Keep directories in sync by copying or moving files between them.
* **File Transformation**: Rename files based on custom rules, such as transliteration and cleaning.
* **File Reporting**: Generate reports on file discrepancies and changes.
* **Utility Scripts**: Additional scripts for file system operations and comparisons.

## Folder Structure

The repository is organized as follows:

```

fileworks/
├── core/                        # Core utilities and configurations
│   ├── __init__.py
│   ├── config.py                # Configuration settings
│   └── constants.py             # Constant values and mappings
├── mover/                       # IO-Moving Functionality
├── scripts/                     # Own Legacy
├── tools/                       # Utility functions and transformers
│   ├── __init__.py
│   ├── filters.py               # File name filters
│   ├── logger.py                # Renaming logger
│   ├── transformers.py          # File name transformers
├── utils/                       # Helpers
│   ├── compare.py               # Compare with hashsums
│   ├── date.py                  # Date-time
│   ├── io.py                    # For moving and renaming files
│   ├── name.py                  # From camel to snake case
│   ├── stats.py                 # Files counter
│   └── string.py                # For strings
├── main.py                      # Entry point
├── .env.example                 # Example environment variables
├── .gitignore                   # Git ignore file
├── LICENSE.md                   # License information
├── README.md                    # Project overview and documentation
└── requirements.txt             # Python dependencies
```



## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/avtomatik/fileworks.git
cd fileworks
pip install --no-cache-dir -r requirements.txt
```



## Usage Not Tested

Each script in the `file_system/` directory can be run independently from the command line. For example, to mirror files between two directories:

```bash
python file_system/mirror_files.py /path/to/source /path/to/destination
```



Refer to the individual script files for specific usage instructions and options.

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
