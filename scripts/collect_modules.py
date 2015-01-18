#! /usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import print_function
import os
import armilla
import ersilia
import zaira


def collect_score_paths(score_module):
    paths = {
        'makers': [],
        'materials': [],
        'segments': [],
        'stylesheet': None,
        }
    root_path = score_module.__path__[0]
    print(root_path)
    makers_path = os.path.join(root_path, 'makers')
    materials_path = os.path.join(root_path, 'materials')
    segments_path = os.path.join(root_path, 'segments')
    for name in os.listdir(makers_path):
        if name.endswith('.py') and name[0].isalpha():
            file_path = os.path.join(makers_path, name)
            print(file_path)
            paths['makers'].append(file_path)
    for name in os.listdir(materials_path):
        directory_path = os.path.join(materials_path, name)
        if not os.path.isdir(directory_path):
            continue
        file_path = os.path.join(directory_path, 'definition.py')
        if not os.path.exists(file_path):
            continue
        print(file_path)
        paths['materials'].append(file_path)
    for name in os.listdir(segments_path):
        directory_path = os.path.join(segments_path, name)
        if not os.path.isdir(directory_path):
            continue
        file_path = os.path.join(directory_path, 'definition.py')
        if not os.path.exists(file_path):
            continue
        print(file_path)
        paths['segments'].append(file_path)
    stylesheet_path = os.path.join(root_path, 'stylesheets', 'stylesheet.ily')
    paths['stylesheet'] = stylesheet_path
    return paths


def collect_consort_paths():
    import consort
    paths = []
    root_path = consort.__path__[0]
    print(root_path)
    tools_path = os.path.join(root_path, 'tools')
    for name in os.listdir(tools_path):
        if name.endswith('.py') and name[0].isalpha():
            file_path = os.path.join(tools_path, name)
            print(file_path)
            paths.append(file_path)
    return paths


def source_path_to_title(module_name, source_path):
    path = source_path.partition(module_name)[-1]
    path = path.strip('/')
    path = path.strip('.py')
    path = path.replace(os.path.sep, '.')
    if path.endswith('.definition'):
        path = path.replace('.definition', '')
    return path


def source_path_to_tex_path(module_name, source_path):
    import dissertation
    root_path = dissertation.__path__[0]
    file_name = source_path_to_title(module_name, source_path)
    file_name = file_name.replace('.', '--')
    file_name = file_name.replace('_', '-')
    file_name = file_name + '.tex'
    path = os.path.join(
        root_path,
        'appendices',
        module_name,
        file_name,
        )
    return path


def source_path_to_latex(module_name, source_path):
    with open(source_path, 'r') as file_pointer:
        lines = file_pointer.read().splitlines()
    title = source_path_to_title(module_name, source_path)
    title = title.replace('_', '\_')
    result = []
    result.append(r'\subsection{{{}}}'.format(title))
    result.append('')
    result.append(r'\begin{lstlisting}')
    result.extend(lines)
    result.append(r'\end{lstlisting}')
    result = '\n'.join(result)
    return result


def write_consort_source_index(source_paths):
    import dissertation
    result = [r'\section{\emph{consort} source}', '']
    for source_path in source_paths:
        tex_path = source_path_to_tex_path('consort', source_path)
        tex_path = tex_path.partition('dissertation/')[-1]
        result.append(r'\input{{{}}}'.format(tex_path))
    result = '\n'.join(result)
    root_path = dissertation.__path__[0]
    index_path = os.path.join(root_path, 'appendices', 'consort', 'index.tex')
    with open(index_path, 'w') as file_pointer:
        file_pointer.write(result)


def write_score_source_index(score_name, path_dictionary):
    import dissertation
    result = []

    string = r'\section{{\emph{{{}}} makers source}}'
    string = string.format(score_name)
    result.append(string)
    result.append('')

    source_paths = path_dictionary['makers']
    for source_path in source_paths:
        tex_path = source_path_to_tex_path(score_name, source_path)
        tex_path = tex_path.partition('dissertation/')[-1]
        result.append(r'\input{{{}}}'.format(tex_path))

    result.append('')
    string = r'\section{{\emph{{{}}} materials source}}'
    string = string.format(score_name)
    result.append(string)
    result.append('')

    source_paths = path_dictionary['materials']
    for source_path in source_paths:
        tex_path = source_path_to_tex_path(score_name, source_path)
        tex_path = tex_path.partition('dissertation/')[-1]
        result.append(r'\input{{{}}}'.format(tex_path))

    result.append('')
    string = r'\section{{\emph{{{}}} segments source}}'
    string = string.format(score_name)
    result.append(string)
    result.append('')

    source_paths = path_dictionary['segments']
    for source_path in source_paths:
        tex_path = source_path_to_tex_path(score_name, source_path)
        tex_path = tex_path.partition('dissertation/')[-1]
        result.append(r'\input{{{}}}'.format(tex_path))

    result.append('')
    string = r'\section{{\emph{{{}}} stylesheet source}}'
    string = string.format(score_name)
    result.append(string)
    result.append('')

    source_paths = [path_dictionary['stylesheet']]
    for source_path in source_paths:
        tex_path = source_path_to_tex_path(score_name, source_path)
        tex_path = tex_path.partition('dissertation/')[-1]
        result.append(r'\input{{{}}}'.format(tex_path))

    result = '\n'.join(result)
    root_path = dissertation.__path__[0]
    index_path = os.path.join(
        root_path,
        'appendices',
        score_name,
        'index.tex'
        )

    with open(index_path, 'w') as file_pointer:
        file_pointer.write(result)


def path_dictionary_to_list(path_dictionary):
    paths = []
    paths.extend(path_dictionary['makers'])
    paths.extend(path_dictionary['materials'])
    paths.extend(path_dictionary['segments'])
    paths.append(path_dictionary['stylesheet'])
    return paths


def write_source_listings(module_name, source_paths):
    for source_path in source_paths:
        latex = source_path_to_latex(module_name, source_path)
        tex_path = source_path_to_tex_path(module_name, source_path)
        with open(tex_path, 'w') as file_pointer:
            file_pointer.write(latex)


if __name__ == '__main__':
    zaira_path_dictionary = collect_score_paths(zaira)
    zaira_paths = path_dictionary_to_list(zaira_path_dictionary)
    write_source_listings('zaira', zaira_paths)
    write_score_source_index('zaira', zaira_path_dictionary)

    armilla_path_dictionary = collect_score_paths(armilla)
    armilla_paths = path_dictionary_to_list(armilla_path_dictionary)
    write_source_listings('armilla', armilla_paths)
    write_score_source_index('armilla', armilla_path_dictionary)

    ersilia_path_dictionary = collect_score_paths(ersilia)
    ersilia_paths = path_dictionary_to_list(ersilia_path_dictionary)
    write_source_listings('ersilia', ersilia_paths)
    write_score_source_index('ersilia', ersilia_path_dictionary)

    consort_paths = collect_consort_paths()
    write_source_listings('consort', consort_paths)
    write_consort_source_index(consort_paths)