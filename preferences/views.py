from rest_framework.views import APIView
from django.core.cache import cache
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from .models import Post, User, Interaction
from .serializers import InteractionSerializer, PreferenceSerializer
from preferences.helpers import adjust_preferences
import logging

logger = logging.getLogger(__name__)

class RecordInteractionView(APIView):
    def post(self, request):
        logger.info("Received interaction request.")
        serializer = InteractionSerializer(data=request.data)
        if not serializer.is_valid():
            logger.warning(f"Invalid data received: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        data = serializer.validated_data 
        logger.info(f"Validated data: {data}")

        try:
            user = User.objects.get(user_id=data['user'])
            post = Post.objects.get(post_id=data['post'])
        except User.DoesNotExist:
            return Response({"status": "error", "message": "Invalid user_id"}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"status": "error", "message": "Invalid post_id"}, status=status.HTTP_400_BAD_REQUEST)
        
        interaction_type = data['interaction_type']
        existing_interaction = Interaction.objects.filter(
            user=user,
            post=post,
            interaction_type=interaction_type
        ).exists()
        
        if existing_interaction:
            logger.info(f"Interaction already exists: {interaction_type} for post {post.post_id} by user {user.user_id}")
            return Response(
                {"status": "error", "message": "Interaction already happened."},
                status=status.HTTP_400_BAD_REQUEST
            )

        interaction_type = data['interaction_type'] 
        interaction_weights = {
            'like': 5,
            'comment': 3,
            'share': 10,
            'report': -5
        }
        
        if interaction_type not in interaction_weights:
            logger.warning(f"Invalid interaction type: {interaction_type}")
            return Response({"status": "error", "message": "Invalid interaction type"}, status=status.HTTP_400_BAD_REQUEST)
        
        weight = interaction_weights[interaction_type]
        logger.info(f"Adjusting preferences for user_id: {user.user_id}.Current preferences: {user.preferences}")
        logger.info(f"Post tags: {post.tags.all()}, Interaction weight: {weight}, user_tags:{user.tags}")
        
        preferences, tags = adjust_preferences(user.preferences, post.tags.all(), weight, user.tags)
         
        try:
            user.preferences = preferences
            user.tags = tags
            user.save()
            logger.info(f"User preferences and tags saved: {user.preferences}")
        except Exception as e:
            logger.error(f"Error saving preferences to user: {e}")
            return Response({"status": "error", "message": "Error saving preferences."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)            

        Interaction.objects.create(
            user=user,
            post=post,
            interaction_type=interaction_type,
        )
        logger.info(f"Interaction recorded: {interaction_type} for post {post.post_id} by user {user.user_id}")
        return Response({"status": "success", "message": "User preferences updated."}, status=status.HTTP_200_OK)
    

class FetchPreferencesView(APIView):
    def get(self, request):
        logger.info("Received GET request to fetch user preferences.") 
        user_id = request.query_params.get('user_id')
        if not user_id:
            logger.warning("user_id parameter is missing in the request.")
            return Response({"status": "error", "message": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        logger.info(f"Fetching preferences for user_id: {user_id}")
        
        cache_key = f"user_preferences_{user_id}"
        
        cached_preferences = cache.get(cache_key)
        if cached_preferences:
            logger.info(f"Cache hit for user_id: {user_id}. Returning cached data.")
            return Response(cached_preferences, status=status.HTTP_200_OK)
        
        logger.info(f"Cache miss for user_id: {user_id}. Fetching preferences from the database.")

        try:
            user = User.objects.get(user_id=user_id)
            logger.info(f"User found: {user.user_id}. Proceeding to serialize preferences.")
        except User.DoesNotExist:
            logger.error(f"User with ID {user_id} not found in the database.")
            return Response({"status": "error", "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PreferenceSerializer(user)
        preferences_data = serializer.data
        logger.info(f"Preferences data serialized for user_id: {user_id}.")

        cache.set(cache_key, preferences_data, timeout=settings.CACHE_TTL)
        logger.info(f"Preferences cached for user_id: {user_id} with TTL: {settings.CACHE_TTL}")
        
        logger.info(f"Returning preferences data for user_id: {user_id}.")
        return Response(preferences_data, status=status.HTTP_200_OK)


# without using cache mechanism
# class FetchPreferencesView(APIView):
#     def get(self, request):
#         user_id = request.query_params.get('user_id')
#         try:
#             user = User.objects.get(user_id=user_id)
#         except User.DoesNotExist:
#             return Response({"status": "error", "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = PreferenceSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)
