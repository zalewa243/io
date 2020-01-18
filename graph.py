import os
import random

import networkx as nx
import matplotlib.pyplot as plt
from os import listdir

import sys
import re

current_file_name = sys.argv[0].split('/')[-1] #zwraca nazwę aktualnego pliku - jak ? sami obczajcie co robi sys.argv, powiem wam tylko że jest -1 bo graph.py jest ostatnim plikiem

full_file_names = {} 
"""
# ######## Historyjka 1. #########
def extract_filename(file):
    return file.split(".")[0]  # cut extension .py


def get_file_size(file_path):
    file_path = file_path if file_path.endswith('.py') else './'+file_path+'.py'
    return os.path.getsize(file_path)


def createGraph(path="./"):
    g = nx.DiGraph()  # create direct graph
    files_to_parse = list(filter(lambda f: f.endswith(".py"), listdir(path))) # only python files
    files_to_parse.pop(files_to_parse.index(current_file_name))  # without current file

    for file_path in files_to_parse:
        g.add_node(extract_filename(file_path)+str(get_file_size(file_path)))
        find_edges_in_file(file_path, g)
    return g

def drawGraph(graph):
    edge_labels = nx.get_edge_attributes(g, "weight")
    pos = nx.spring_layout(g)
    nx.draw(graph, pos=pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(g, pos=pos, edge_labels = edge_labels)
    plt.show()


def count_calls(path, module_name):
    pattern = re.compile(r'{}\.'.format(module_name))
    with open(path, 'r') as f:
        calls = re.findall(pattern, f.read())
        return len(calls)

def find_edges_in_file(file, g):
    with open(file, 'r') as fr:
        for line in fr: #iteruje po liniach
            if ("import" in line):
                tab = line.split()
                print(tab)
                g.add_edge(
                    extract_filename(file)+str(get_file_size(file)),
                    tab[1]+str(get_file_size(tab[1])),
                    weight=count_calls(file,tab[1])
                )

#g = createGraph()
#drawGraph(g)
# ###############################################
"""
# #### Historyjka nr2 ###########################
def rtrn_python_files(path): #zwraca listę plików .py
    return list(filter(lambda f: f.endswith(".py"), listdir(path)))


def drawGraph_func(graph):
    edge_labels = nx.get_edge_attributes(g, "weight")
    #node_labels = nx.get_node_attributes(g, "weight")

    pos = nx.spring_layout(g)

    nx.draw(graph,pos=pos, with_labels=True, font_weight='bold') 
    nx.draw_networkx_edge_labels(g, pos=pos, edge_labels = edge_labels)

    plt.show()

def count_call_1(path, func_name):
    pattern = re.compile(r'{}\(\)[^:]'.format(func_name))
    with open(path, 'r') as f:
        calls = re.findall(pattern, f.read())
        return len(calls)

def get_node_name(path, name):
    return name+" "+str(count_call_1(path,name))

def createGraphFunctions(path="./HIS_II/"):
    g = nx.DiGraph()  # create direct graph
    files_to_parse = rtrn_python_files(path)
    #files_to_parse.pop(files_to_parse.index(current_file_name))  # without current file
    funkcje=[]
    t_funkcje=[]
    #node'y
    for plik in files_to_parse:
        fs = get_function_names(path+"/"+plik)
        funkcje += fs
        t_funkcje = fs
        for name in t_funkcje:
            g.add_node(get_node_name(path+"/"+plik,name))
    
    #edge
    for plik in files_to_parse:
        for name in funkcje:
            for othername in funkcje:
                if name == othername:
                    continue
                methodCount = count_method(path+"/"+plik, name, othername)
                if (methodCount > 0):
                    name = get_node_name(path+"/"+plik, name)
                    othername = get_node_name(path+"/"+plik, othername)
                    g.add_edge(name, othername, weight=methodCount)
    return g

def get_function_names(path): #function names from file
    names = []
    with open(path, 'r') as fr:
        for line in fr:
            if re.match(r"^\s*?def", line):
                n = line.split(" ")[1].split("(")[0] 
                names.append(n)
    print(names)
    return names


def count_method(path, names, othernames):
    count = 0
    t = 0
    str = 'def ' + names
    f = open(path,"r")
    for x in f:
        if t == 1:
            if 'def ' in x:
                t = 0
                f.close()
                return count
            if othernames in x:
                count=count+1
        elif str in x:
            t = 1
    f.close()
    return count

g = createGraphFunctions()
drawGraph_func(g)
"""
# ##########################################
# #### HISTORIA NR 3 FINITO KUHWA JEGO MAC #####

def rtrn_python_files(path): #zwraca listę plików .py
    return list(filter(lambda f: f.endswith(".py"), listdir(path)))


def drawGraph_func(graph):
    edge_labels = nx.get_edge_attributes(g, "weight")
    l = []
    for u,v,d in g.edges(data=True):
        if "weight" not in d:
            l.append(((u,v), ''))
        else:
            l.append(((u,v), d['weight']))
    edge_labels = dict(l)
    pos = nx.spring_layout(g)

    nx.draw(graph,pos=pos, with_labels=True, font_weight='bold') 
    nx.draw_networkx_edge_labels(g, pos=pos, edge_labels = edge_labels, label_pos=0.3)
    plt.show()

def count_call_1(path, func_name):
    pattern = re.compile(r'{}\(\)[^:]'.format(func_name))
    with open(path, 'r') as f:
        calls = re.findall(pattern, f.read())
        return len(calls)

def get_node_name(path, name):
    return name+" "+str(count_call_1(path,name))

def createGraphFunctions(path="./HIS_III/"):
    g = nx.MultiDiGraph()  # create direct graph
    # files_to_parse = rtrn_python_files(path)
    #files_to_parse.pop(files_to_parse.index(current_file_name))  # without current file
    module_list = []
    for file_ in listdir(path):
        if os.path.isdir(path+"/"+file_):  # sprawdzamy czy jest folderem
            if "__init__.py" in listdir(path+"/"+file_+"/"):  # sprawdzamy czy jest modulem
                module_list.append(file_)
   
    print(module_list)
    for module in module_list:
        g.add_node(module)
        for file_ in listdir(path+"/"+module+"/"):
            for fun in get_function_names(path+"/"+module+"/"+file_):
                g.add_node(fun)
                g.add_edge(fun, module)

    for module_1 in module_list:
        for module_2 in module_list:
            if module_1 == module_2:
                continue
            count = 0
            for file_ in listdir(path+"/"+module_1+"/"):
                functions_in_module_1 = get_function_names(path+"/"+module_1+"/"+file_)
                for fun in functions_in_module_1:
                    for plik in rtrn_python_files(path+module_2+"/"):
                        count += count_call_1(path+"/"+module_2+"/"+plik, fun)
            g.add_edge(module_1, module_2, weight=count, label=module_1+module)
    return g

def get_function_names(path): #function names from file
    names = []
    with open(path, 'r') as fr:
        for line in fr:
            if re.match(r"^\s*?def", line):
                n = line.split(" ")[1].split("(")[0] 
                names.append(n)
    print(names)
    return names


def count_method(path, names, othernames):
    count = 0
    t = 0
    str = 'def ' + names
    f = open(path,"r")
    for x in f:
        if t == 1:
            if 'def ' in x:
                t = 0
                f.close()
                return count
            if othernames in x:
                count=count+1
        elif str in x:
            t = 1
    f.close()
    return count


g = createGraphFunctions()
drawGraph_func(g)
"""