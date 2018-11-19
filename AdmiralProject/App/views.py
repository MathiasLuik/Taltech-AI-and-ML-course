from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json 
from App.models import Node

@api_view(["POST"])
def save_categories(jsonData):
    try:
        data=json.loads(jsonData.body)
        nodes = []
        parse_structure(data, None, nodes)              
        for node in nodes:
            node.save()       
        return JsonResponse(str(nodes),safe=False)
    
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def get_categories(request, id):
    try:        
        return JsonResponse(get_tree_by_id(id))
    
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

def get_tree_by_id(id):
    root = Node.objects.get(id=id).to_json()  #http://127.0.0.1:8000/categories/2      {'id': 2, 'name': 'Category 1.1'}
    root['children'] = find_children(root['name']) 
    root['parent'] = find_parent(root['name'])
    root['siblings'] = find_siblings(root['name'])
    root['all family children'] = find_all_children(root['name'])  
    return root


def find_children(name):
    children = Node.objects.filter(parent=name) 
    children_list = list(map(lambda child: child.to_json(), children))
    return children_list   

def find_parent(name):
    parent_dict = Node.objects.get(name=name).get_parent()
    parent_name=parent_dict['parent']
    parents = Node.objects.filter(name=parent_name)
    parent_list = list(map(lambda parent: parent.to_json(), parents))
    return parent_list

def find_siblings(name):
    parent_dict = Node.objects.get(name=name).get_parent()
    parent_name=parent_dict['parent']
    siblings = Node.objects.filter(parent=parent_name)
    sibling_list = list(map(lambda sibling: sibling.to_json(), siblings))
    for sibling in sibling_list:
        if str(name)==str(sibling['name']):
            sibling_list.remove(sibling)
    return sibling_list

def find_all_children(name):
    children = Node.objects.filter(parent=name) 
    children_list = list(map(lambda child: child.to_json(), children)) 
    for child in children_list:
        child['children'] = find_children(child['name'])
    return children_list

def parse_structure(element, parentElement, nodes):
    if (parentElement):
        parent_name = parentElement['name']
    else:
        parent_name = None  
    node = Node(parent=parent_name, name=element['name'])
    nodes.append(node)
    
    if 'children' in element:
       for child in element['children']:
            parse_structure(child, element, nodes)
