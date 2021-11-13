from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movie.models import Movie
from .serializers import MovieSerializer


@api_view(['GET'])
def hello(request, **kwargs):
    data_msg = {'msg': 'Hello from Api is {}'.format(kwargs.get('key'))}
    if kwargs.get('key') == 'yes':
        return Response(data=data_msg, status=status.HTTP_200_OK)
    return Response(data=data_msg, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serialized_movies = MovieSerializer(instance=movies, many=True)

    return Response(data=serialized_movies.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def movie_create(request):
    serialized_movie = MovieSerializer(data=request.data)
    if serialized_movie.is_valid():
        serialized_movie.save()
    else:
        return Response(data=serialized_movie.errors, status=status.HTTP_400_BAD_REQUEST)
    data = {
        'message': 'Success',
        'Data': {'id': serialized_movie.data.get("id")}
    }
    return Response(data=data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_details(request,pk):
    try:
        movie_obj = Movie.objects.get(pk=pk)
    except Exception as e:
        return Response(data={'msg': 'Failed'}, status=status.HTTP_400_BAD_REQUEST)

    serialized_movie = MovieSerializer(instance=movie_obj)

    return Response(data=serialized_movie.data)


@api_view(['DELETE'])
def movie_delete(request,pk):
    response = {}
    try:
        movie_obj = Movie.objects.get(pk=pk)
        movie_obj.delete()
        response['data'] = {'msg': 'Deleted Successfully'}
        response['status'] = status.HTTP_200_OK

    except Exception as e:
        response['data'] = {'msg': 'Cannot Delete'}
        response['status'] = status.HTTP_400_BAD_REQUEST

    return Response(**response)


@api_view(['PUT', 'PATCH'])
def movie_update(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)

    except Exception as e:
        return Response(data={'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        movie_serialized = MovieSerializer(instance=movie, data=request.data)
    elif request.method == 'PATCH':
        movie_serialized = MovieSerializer(instance=movie, data=request.data, partial=True)

    if movie_serialized.is_valid():
        movie_serialized.save()
        return Response(data=movie_serialized.data, status= status.HTTP_200_OK)

    return Response(data=movie_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
