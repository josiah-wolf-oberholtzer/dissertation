#! /usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import print_function
import armilla
import os
import zaira


def collect_score_paths(score_module):
    paths = []
    root_path = score_module.__path__[0]
    print(root_path)
    makers_path = os.path.join(root_path, 'makers')
    materials_path = os.path.join(root_path, 'materials')
    segments_path = os.path.join(root_path, 'segments')
    for name in os.listdir(makers_path):
        if name.endswith('.py') and name[0].isalpha():
            file_path = os.path.join(makers_path, name)
            print(file_path)
            paths.append(file_path)
    for name in os.listdir(materials_path):
        directory_path = os.path.join(materials_path, name)
        if not os.path.isdir(directory_path):
            continue
        file_path = os.path.join(directory_path, 'definition.py')
        if not os.path.exists(file_path):
            continue
        print(file_path)
        paths.append(file_path)
    for name in os.listdir(segments_path):
        directory_path = os.path.join(materials_path, name)
        if not os.path.isdir(directory_path):
            continue
        file_path = os.path.join(directory_path, 'definition.py')
        if not os.path.exists(file_path):
            continue
        print(file_path)
        paths.append(file_path)
    paths = [(score_module.__name__, path) for path in paths]
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
    paths = [('consort', path) for path in paths]
    return paths


def source_path_to_title(module_name, source_path):
    path = source_path.partition(module_name)[-1]
    path = path.strip('/')
    path = path.strip('.py')
    path = path.replace(os.path.sep, '.')
    return path


def source_path_to_tex_path(module_name, source_path):
    import dissertation
    root_path = dissertation.__path__[0]
    file_name = source_path_to_title(module_name, source_path)
    file_name = file_name.replace('.', '__')
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
    result = []
    result.append(r'\subsubsection{{{}}}'.format(title))
    result.append('')
    result.append(r'\begin{lstlisting}')
    result.extend(lines)
    result.append(r'\end{lstlisting}')
    result = '\n'.join(result)
    return result


def write_module_index(module_name, tex_paths):
    import dissertation
    result = []
    result.append(r'\subsection{{{}}}'.format(module_name))
    result.append('')
    for tex_path in tex_paths:
        _, tex_path = os.path.split(tex_path)
        result.append(r'\input{{{}}}'.format(tex_path))
    result = '\n'.join(result)
    root_path = dissertation.__path__[0]
    index_path = os.path.join(
        root_path,
        'appendices',
        module_name,
        'index.tex'
        )
    with open(index_path, 'w') as file_pointer:
        file_pointer.write(result)


if __name__ == '__main__':
    armilla_paths = []
    for module_name, source_path in collect_score_paths(armilla):
        latex = source_path_to_latex(module_name, source_path)
        tex_path = source_path_to_tex_path(module_name, source_path)
        with open(tex_path, 'w') as file_pointer:
            file_pointer.write(latex)
        armilla_paths.append(tex_path)
    write_module_index('armilla', armilla_paths)

    zaira_paths = []
    for module_name, source_path in collect_score_paths(zaira):
        latex = source_path_to_latex(module_name, source_path)
        tex_path = source_path_to_tex_path(module_name, source_path)
        with open(tex_path, 'w') as file_pointer:
            file_pointer.write(latex)
        zaira_paths.append(tex_path)
    write_module_index('zaira', zaira_paths)

    consort_paths = []
    for module_name, source_path in collect_consort_paths():
        latex = source_path_to_latex(module_name, source_path)
        tex_path = source_path_to_tex_path(module_name, source_path)
        with open(tex_path, 'w') as file_pointer:
            file_pointer.write(latex)
        consort_paths.append(tex_path)
    write_module_index('consort', consort_paths)