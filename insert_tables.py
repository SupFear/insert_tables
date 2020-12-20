import os
import argparse
from string import Template


prefix_cover = 'icon-cover'
prefix_small = 'icon-s'
prefix_medium = 'icon-m'
prefix_large = 'icon-l'

file_format = '.svg'


def parse_arguments():
    """
    Parse arguments from command line
    :return: argparse.Namespace
    """
    get_cwd = os.getcwd()

    parser = argparse.ArgumentParser(description='Create html page with tables')
    parser.add_argument('-i', '--icons_dir', type=str, default=os.path.join(get_cwd, 'icons'),
                        help='Path to directory with icons')
    parser.add_argument('-t', '--template', type=str, default=os.path.join(get_cwd, 'template.html'),
                        help='Path to HTML template file')
    parser.add_argument('-o', '--output', type=str, default=os.path.join(get_cwd, 'rendered.html'),
                        help='Path to output HTML file')
    parser.add_argument('--cover', action='store_true', dest='generate_cover',
                        help='Generate table with icons with prefix "{}"'.format(prefix_cover))
    parser.add_argument('--small', action='store_true', dest='generate_small',
                        help='Generate table with icons with prefix "{}"'.format(prefix_small))
    parser.add_argument('--medium', action='store_true', dest='generate_medium',
                        help='Generate table with icons with prefix "{}"'.format(prefix_medium))
    parser.add_argument('--large', action='store_true', dest='generate_large',
                        help='Generate table with icons with prefix "{}"'.format(prefix_large))

    return parser.parse_args()


def create_table_with_files(file_paths, indent=0, img_class=None, columns=1):
    """
    Creates a simple table with indent and columns with 2 cells:
    first cell - name of the file
    second cell - img tag with class img_class
    :param file_paths: list
    :param indent: int
    :param img_class: str
    :param columns: int
    :return: str
    """
    table_tag = '<table>\n{}' + ' ' * indent + '</table>'
    row_tag = ' ' * indent + '    <tr>{}</tr>\n'
    cell_tag = '<td>{}</td>'
    if img_class:
        img_tag = '<img src="{}" class="' + img_class + '">'
    else:
        img_tag = '<img src="{}">'

    counter_columns = 0
    rows = ''
    cells = ''
    for file_path in file_paths:
        filename = os.path.basename(file_path)

        name_cell = cell_tag.format(filename.strip(file_format))

        img_cell = img_tag.format(file_path)
        image_cell = cell_tag.format(img_cell)

        cells += name_cell + image_cell

        counter_columns += 1

        if counter_columns >= columns:
            rows += row_tag.format(cells)
            counter_columns = 0
            cells = ''

    return table_tag.format(rows)


def count_indent(text, template):
    """
    Count indent before template in the text and returns count of spaces
    :param text: str
    :param template: str
    :return: int
    """
    template_index = text.find(template)
    indent = 0
    while text[template_index - 1 - indent] == ' ':
        indent += 1

    return indent


if __name__ == '__main__':
    arguments = parse_arguments()

    with open(arguments.template, 'r') as f:
        html_template = f.read()

    # Default - if no one argument of prefix is set, all prefixes will be shown in the table,
    # otherwise - only prefix that is set will be shown in the table
    if (arguments.generate_cover or arguments.generate_small or
       arguments.generate_medium or arguments.generate_large) is False:
        arguments.generate_cover = arguments.generate_small = True
        arguments.generate_medium = arguments.generate_large = True

    listdir = os.listdir(arguments.icons_dir)
    svg_files = [item for item in listdir if item.endswith(file_format)]

    if arguments.generate_cover:
        svg_files_cover = [os.path.join(arguments.icons_dir, item) for item in svg_files if item.startswith(prefix_cover)]
        cover_indent = count_indent(html_template, '$cover_table')
        table_cover = create_table_with_files(svg_files_cover, indent=cover_indent, img_class='cover', columns=4)
        html_template = Template(html_template).safe_substitute(cover_table=table_cover)

    if arguments.generate_small:
        svg_files_small = [os.path.join(arguments.icons_dir, item) for item in svg_files if item.startswith(prefix_small)]
        small_indent = count_indent(html_template, '$small_table')
        table_small = create_table_with_files(svg_files_small, indent=small_indent, img_class='small', columns=3)
        html_template = Template(html_template).safe_substitute(small_table=table_small)

    if arguments.generate_medium:
        svg_files_medium = [os.path.join(arguments.icons_dir, item) for item in svg_files if item.startswith(prefix_medium)]
        medium_indent = count_indent(html_template, '$medium_table')
        table_medium = create_table_with_files(svg_files_medium, indent=medium_indent, img_class='medium', columns=2)
        html_template = Template(html_template).safe_substitute(medium_table=table_medium)

    if arguments.generate_large:
        svg_files_large = [os.path.join(arguments.icons_dir, item) for item in svg_files if item.startswith(prefix_large)]
        large_indent = count_indent(html_template, '$large_table')
        table_large = create_table_with_files(svg_files_large, indent=large_indent, img_class='large', columns=2)
        html_template = Template(html_template).safe_substitute(large_table=table_large)

    with open(arguments.output, 'w') as f:
        f.write(html_template)
