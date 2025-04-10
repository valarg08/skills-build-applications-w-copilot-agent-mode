from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.db import connection
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activity': '/api/activity/',
        'leaderboard': '/api/leaderboard/',
        'workouts': '/api/workouts/',
    })

def test_db_connection(request):
    try:
        # Attempt to connect to the database
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({"status": "success", "message": "Database connection is working."})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})