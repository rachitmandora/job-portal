from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Job, Application
from .serializers import JobSerializer, RegisterSerializer, ApplicationSerializer

def index_view(request):
    return render(request, "index.html")

@api_view(["GET"])
def job_list(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    serializer = JobSerializer(job)
    return Response(serializer.data)

@api_view(["POST"])
def create_job(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(["PUT", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def update_delete_job(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if request.method == "DELETE":
        job.delete()
        return Response({"message": "Job deleted successfully"})

    serializer = JobSerializer(job, data=request.data, partial=(request.method == "PATCH"))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(["GET"])
def search_jobs(request):
    query = request.GET.get("search", "")
    location = request.GET.get("location", "")

    jobs = Job.objects.all()
    if query:
        jobs = jobs.filter(title__icontains=query)
    if location:
        jobs = jobs.filter(location__icontains=location)

    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def apply_to_job(request, pk):
    job = get_object_or_404(Job, pk=pk)

    data = request.data.copy()
    data["job"] = job.id

    serializer = ApplicationSerializer(data=data)
    if serializer.is_valid():
        serializer.save(applicant=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def view_job_applications(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if not request.user.is_staff:
        try:
            if request.user.profile.role != "recruiter":
                return Response({"error": "Only recruiters can view applications."}, status=403)
        except ObjectDoesNotExist:
            return Response({"error": "Profile not found."}, status=404)

    applications = Application.objects.filter(job=job)
    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data)