from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project, Build
from .serializers import ProjectSerializer, BuildSerializer

@csrf_exempt
def webhook_receiver(request):
    if request.method == 'POST':
        if 'application/json' in request.content_type:
            try:
                data = json.loads(request.body)
                
                # Check if it's a GitHub webhook payload
                if 'repository' in data and 'pusher' in data:
                    # Process GitHub webhook payload
                    # Example: Extract relevant information such as repository name, pusher username, commit details, etc.
                    # Store relevant information in the database
                    # You may need to adjust this based on the actual structure of GitHub webhook payloads
                
                    return JsonResponse({'message': 'GitHub webhook received and processed successfully'}, status=200)
                elif 'project_id' in data and 'build_status' in data:
                    # Process Discord webhook payload
                    # Example: Extract relevant information such as project ID, build status, etc.
                    # Store relevant information in the database
                    # You may need to adjust this based on the actual structure of Discord webhook payloads
                
                    return JsonResponse({'message': 'Discord webhook received and processed successfully'}, status=200)
                else:
                    return JsonResponse({'error': 'Unsupported webhook payload'}, status=400)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON data in request body'}, status=400)
        else:
            return JsonResponse({'error': 'Content-Type must be application/json'}, status=400)
    else:
        return JsonResponse({'error': 'Unsupported HTTP method'}, status=405)

@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def project_detail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response({'error': 'Project not found'}, status=404)

@api_view(['GET'])
def build_history(request, project_id):
    builds = Build.objects.filter(project_id=project_id)
    serializer = BuildSerializer(builds, many=True)
    return Response(serializer.data)