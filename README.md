# Insert tables with svg images into HTML page

This script allows you to insert tables into HTML page 
with anchors like "$small_table" just in the HTML code.

## Installation

```console
# clone the repo
$ git clone https://github.com/

# change the working directory
$ cd insert_tables
```

## Usage

```console
$ python3 insert_tables.py --help
usage: insert_tables.py [-h] [-i ICONS_DIR] [-t TEMPLATE] [-o OUTPUT]
                        [--cover] [--small] [--medium] [--large]

Create html page with tables

optional arguments:
  -h, --help            show this help message and exit
  -i ICONS_DIR, --icons_dir ICONS_DIR
                        Path to directory with icons
  -t TEMPLATE, --template TEMPLATE
                        Path to HTML template file
  -o OUTPUT, --output OUTPUT
                        Path to output HTML file
  --cover               Generate table with icons with prefix "icon-cover"
  --small               Generate table with icons with prefix "icon-s"
  --medium              Generate table with icons with prefix "icon-m"
  --large               Generate table with icons with prefix "icon-l"


```

### Example

Render HTML page with default HTML template template.html and output file rendered.html with 
icons in the folder ./icons with all prefixes: "icon-cover", "icon-s", "icon-m", "icon-l"
as default.

```console
$ python3 insert_tables.py
```

To render HTML file with specific template, output file and icons folder use flags: -t, -o and -i:

```console
$ python3 insert_tables.py -t template.html -o rendered.html -i icons
```

To render specific prefixes use flags: --cover, --small, --medium and --large.

```console
$ python3 insert_tables.py -t template.html -o rendered.html -i icons --cover
```
