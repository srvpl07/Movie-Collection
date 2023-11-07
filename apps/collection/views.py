from rest_framework.response import Response
from rest_framework import status, generics, filters
from django.core.paginator import Paginator
import requests
from rest_framework import status
from rest_framework.views import APIView
from collections import Counter
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, permissions

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serilalizers import RegistrationSerializer, TokenSerializer
from .models import *
from .authentication import CustomAuthentication
# class UserRegistrationView(APIView):

#     def post(self, request, *args, **kwargs):
#         serializer = RegistrationSerializer(data = request.data)
#         if serializer.is_valid():
#             try:
#                 new_user = CustomUser.objects.create(username=request.data['username'], password=request.data['password'])
#             except:
#                 return Response({'error': 'user allready exists'})
#             new_user.save()
#             refresh = RefreshToken.for_user(new_user)
#             return Response({
#                 'access_token': str(refresh.access_token),
#                 'refresh_token':str(refresh),
#             }, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'error': serializer.errors})


# class TokenView(generics.GenericAPIView):
#     serializer_class = TokenSerializer
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         access_token = request.data.get('access_token')
#         return Response({'access_token': access_token})










class UserRegistrationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        # return Response([username,password])
        # Create a new user with the provided username and password
        try:
            user = CustomUser.objects.create_user(username, password)
        except Exception as e:
            return Response({
                'error': str(e),
            }, status=status.HTTP_400_BAD_REQUEST)
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            'access_token': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)





# class MovieList(generics.ListCreateAPIView):        
#     # authentication_classes = [JWTAuthentication]
#     # permission_classes = [IsAuthenticated]
#     def get(self, request):
#         # external_url = 'http://demo.credy.in/api/v1/maya/movies/'  # Replace with the actual URL
#         # auth = ('iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0', 'Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1')
#         # response = requests.get(external_url, auth=auth ,verify=False)
#         # response = requests.get(external_url)
#         response ={"count":45466,"next":"https://demo.credy.in/api/v1/maya/movies/?page=2","previous":None,"results":[{"title":"Queerama","description":"50 years after decriminalisation of homosexuality in the UK, director Daisy Asquith mines the jewels of the BFI archive to take us into the relationships, desires, fears and expressions of gay men and women in the 20th century.","genres":"","uuid":"57baf4f4-c9ef-4197-9e4f-acf04eae5b4d"},{"title":"Satana likuyushchiy","description":"In a small town live two brothers, one a minister and the other one a hunchback painter of the chapel who lives with his wife. One dreadful and stormy night, a stranger knocks at the door asking for shelter. The stranger talks about all the good things of the earthly life the minister is missing because of his puritanical faith. The minister comes to accept the stranger's viewpoint but it is others who will pay the consequences because the minister will discover the human pleasures thanks to, ehem, his sister- in -law… The tormented minister and his cuckolded brother will die in a strange accident in the chapel and later an infant will be born from the minister's adulterous relationship.","genres":"","uuid":"163ce013-03e2-47e9-8afd-e7de7688c151"},{"title":"Betrayal","description":"When one of her hits goes wrong, a professional assassin ends up with a suitcase full of a million dollars belonging to a mob boss ...","genres":"Action,Drama,Thriller","uuid":"720e8796-5397-4e81-9bd7-763789463707"},{"title":"Siglo ng Pagluluwal","description":"An artist struggles to finish his work while a storyline about a cult plays in his head.","genres":"Drama","uuid":"e9548ee7-6a95-4917-893e-1fa1d3a6de40"},{"title":"رگ خواب","description":"Rising and falling between a man and woman.","genres":"Drama,Family","uuid":"9b0a4aa2-9ec7-4a3d-98ab-622275f44ea5"},{"title":"Robin Hood","description":"Yet another version of the classic epic, with enough variation to make it interesting. The story is the same, but some of the characters are quite different from the usual, in particular Uma Thurman's very special maid Marian. The photography is also great, giving the story a somewhat darker tone.","genres":"Drama,Action,Romance","uuid":"73399935-2165-41f0-a6a4-1336ef5e5c20"},{"title":"Caged Heat 3000","description":"It's the year 3000 AD. The world's most dangerous women are banished to a remote asteroid 45 million light years from earth. Kira Murphy doesn't belong; wrongfully accused of a crime she did not commit, she's thrown in this interplanetary prison and left to her own defenses. But Kira's a fighter, and soon she finds herself in the middle of a female gang war; where everyone wants a piece of the action... and a piece of her! \"Caged Heat 3000\" takes the Women-in-Prison genre to a whole new level... and a whole new galaxy!","genres":"Science Fiction","uuid":"129cf5d9-827c-4e42-843e-1f87ef99452f"},{"title":"The Burkittsville 7","description":"A film archivist revisits the story of Rustin Parr, a hermit thought to have murdered seven children while under the possession of the Blair Witch.","genres":"Horror","uuid":"5e904ce8-91b7-42b4-84d9-5b53f4cb8c74"},{"title":"Shadow of the Blair Witch","description":"In this true-crime documentary, we delve into the murder spree that was the inspiration for Joe Berlinger's \"Book of Shadows: Blair Witch 2\".","genres":"Mystery,Horror","uuid":"bcacfa33-a886-4ecb-a62a-6bbcb9d9509d"},{"title":"House of Horrors","description":"An unsuccessful sculptor saves a madman named \"The Creeper\" from drowning. Seeing an opportunity for revenge, he tricks the psycho into murdering his critics.","genres":"Horror,Mystery,Thriller","uuid":"388c99da-0cba-4ff0-a528-faea153b43c3"}]}

#         # Check if the request was successful (status code 200)
#         # if response.status_code == 200:
#             # Process the response content as needed

#         return Response(response)
#         # else:
#         #     return JsonResponse({'error': 'Request failed'}, status=500)
        
#         return Response('recipients')

class MovieList(generics.ListCreateAPIView):
    authentication_classes = [CustomAuthentication]
    def get(self, request, *args, **kwargs):
        # external_url = 'http://demo.credy.in/api/v1/maya/movies/'  # Replace with the actual URL
        # Make a GET request to the external URL
        # auth = ('iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0', 'Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1')
        # response = requests.get(external_url, auth=auth ,verify=False)
        # response = requests.get(external_url)
        print(request.user)
        # return Response('hjfdssjafhkjsak')
        response ={"count":45466,"next":"https://demo.credy.in/api/v1/maya/movies/?page=2","previous":None,
                   "results":[{"title":"Queerama","description":"50 years after decriminalisation of homosexuality in the UK,\
                               director Daisy Asquith mines the jewels of the BFI archive to take us into the relationships, desires,\
                                fears and expressions of gay men and women in the 20th century.","genres":"","uuid":"57baf4f4-c9ef-4197-9e4f-acf04eae5b4d"},
                              {"title":"Satana likuyushchiy","description":"In a small town live two brothers, one a minister and the other one a hunchback\
                                painter of the chapel who lives with his wife. One dreadful and stormy night, a stranger knocks at the door asking for shelter.\
                                The stranger talks about all the good things of the earthly life the minister is missing because of his puritanical faith. \
                                The minister comes to accept the stranger's viewpoint but it is others who will pay the consequences because the minister will\
                                discover the human pleasures thanks to, ehem, his sister- in -law… The tormented minister and his cuckolded brother will die in \
                                a strange accident in the chapel and later an infant will be born from the minister's adulterous relationship.","genres":"",
                                "uuid":"163ce013-03e2-47e9-8afd-e7de7688c151"},{"title":"Betrayal","description":"When one of her hits goes wrong, a professional\
                                assassin ends up with a suitcase full of a million dollars belonging to a mob boss ...","genres":"Action,Drama,Thriller",
                                "uuid":"720e8796-5397-4e81-9bd7-763789463707"},{"title":"Siglo ng Pagluluwal","description":"An artist struggles to finish his work\
                                while a storyline about a cult plays in his head.","genres":"Drama","uuid":"e9548ee7-6a95-4917-893e-1fa1d3a6de40"},{"title":"رگ خواب",
                                "description":"Rising and falling between a man and woman.","genres":"Drama,Family","uuid":"9b0a4aa2-9ec7-4a3d-98ab-622275f44ea5"},\
                                {"title":"Robin Hood","description":"Yet another version of the classic epic, with enough variation to make it interesting. The story\
                                is the same, but some of the characters are quite different from the usual, in particular Uma Thurman's very special maid Marian. \
                                The photography is also great, giving the story a somewhat darker tone.","genres":"Drama,Action,Romance","uuid":"73399935-2165-41f0-a6a4-1336ef5e5c20"},
                                {"title":"Caged Heat 3000","description":"It's the year 3000 AD. The world's most dangerous women are banished to a remote asteroid 45 million\
                                light years from earth. Kira Murphy doesn't belong; wrongfully accused of a crime she did not commit, she's thrown in this interplanetary\
                                prison and left to her own defenses. But Kira's a fighter, and soon she finds herself in the middle of a female gang war; where everyone\
                                wants a piece of the action... and a piece of her! \"Caged Heat 3000\" takes the Women-in-Prison genre to a whole new level... \
                                and a whole new galaxy!","genres":"Science Fiction","uuid":"129cf5d9-827c-4e42-843e-1f87ef99452f"},{"title":"The Burkittsville 7",\
                                "description":"A film archivist revisits the story of Rustin Parr, a hermit thought to have murdered seven children while under the \
                                possession of the Blair Witch.","genres":"Horror","uuid":"5e904ce8-91b7-42b4-84d9-5b53f4cb8c74"},{"title":"Shadow of the Blair Witch",
                                "description":"In this true-crime documentary, we delve into the murder spree that was the inspiration for Joe Berlinger's \"Book of Shadows: Blair Witch 2\".",
                                "genres":"Mystery,Horror","uuid":"bcacfa33-a886-4ecb-a62a-6bbcb9d9509d"},{"title":"House of Horrors","description":"An unsuccessful sculptor saves\
                                a madman named \"The Creeper\" from drowning. Seeing an opportunity for revenge, he tricks the psycho into murdering his critics.",
                                "genres":"Horror,Mystery,Thriller","uuid":"388c99da-0cba-4ff0-a528-faea153b43c3"}]}

        # Check if the request was successful (status code 200)
        # if response.status_code == 200:
            # Process the response content as needed

        return Response(response)
        
class ColectionView(generics.ListCreateAPIView):
    
    def get(self, request, *args, **kwargs):
        # user = request.user
        user = CustomUser.objects.get(username='abc')  
        collection_obj = Collection.objects.get(user=user)
        if collection_obj:
            movies = collection_obj.movies.all()
        genere_list = []
        for i in movies:
            genere_list += [i['name'] for i in list(i.genere.all().values('name'))]

        top_3_genres = [element for element, _ in Counter(genere_list).most_common(3)]
        return Response({"is_success": True,
                         "data":{"collections":{
                                    "title": collection_obj.title,
                                    "uuid": collection_obj.uuid,
                                    "description": collection_obj.description}},
                        "favourite_genres": top_3_genres})
    
    def post(self, request):
        movie_list = []
        for movie in request.data['movies']:
            gene_list = []
            for i in movie['genres'].split(','):
                gen,c = Genere.objects.get_or_create(name=i)
                gene_list.append(i)
            genere_list = Genere.objects.filter(name__in = gene_list)
            genere_list = [i for i in genere_list]
            
            movie,created = Movies.objects.get_or_create(title=movie['title'],
                                         description=movie['description'],
                                         uuid=movie['uuid'])
            movie.genere.add(*genere_list)
            movie.save()
            movie_list.append(movie)
        # user = request.user
        user = CustomUser.objects.get(username='abc')
        collection = Collection.objects.create(title = request.data['title'],
                                  description = request.data['description'],
                                  user = user)
        collection.movies.add(*movie_list)
        collection.save()
        return Response({'collection_uuid':collection.uuid})


class ColectionUpdateView(generics.ListAPIView):
    def put(self, request, *args, **kwargs):
        movie_list = []
        for movie in request.data['movies']:
            gene_list = []
            for i in movie['genres'].split(','):
                gen,c = Genere.objects.get_or_create(name=i)
                gene_list.append(i)
            genere_list = Genere.objects.filter(name__in = gene_list)
            genere_list = [i for i in genere_list]
            
            movie,created = Movies.objects.get_or_create(title=movie['title'],
                                         description=movie['description'],
                                         uuid=movie['uuid'])
            movie.genere.add(*genere_list)
            movie.save()
            movie_list.append(movie)
        collection_obj = Collection.objects.get(uuid=self.kwargs['id'])
        collection_obj.title = request.data['title']
        collection_obj.description = request.data['description']
        collection_obj.movies.clear()
                                  
        collection_obj.movies.add(*movie_list)
        collection_obj.save()
        movie_details =[]
        for i in movie_list:
            movie_details.append({
                "title":i.title,
                "description":i.description,
                "genre":",".join([j['name'] for j in i.genere.all().values('name') if j['name'] !=''])
            })
        return Response({"title": collection_obj.title,
                        "description": collection_obj.description,
                        "movies":movie_details})
    
    def delete(self, request, *args, **kwargs):
        try:
            collection_obj = Collection.objects.get(uuid=self.kwargs['id'])
            collection_obj.delete()
            return Response({"success":"successfully deleted collection"},status=status.HTTP_200_OK)
        except Collection.DoesNotExist:
            return Response({"Error":"Collection not found"},status=status.HTTP_404_NOT_FOUND)


class CounterView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        if request.GET.get('reset'):
            obj,created = RequestCounter.objects.get_or_create()
            obj.count = 0
            obj.save()
            return Response({"Success" : 'Successsfully reset'})
        else:
            try:
                return Response({"Number of request" : RequestCounter.objects.all()[0].count})
            except RequestCounter.DoesNotExist:
                return Response({"Number of request" : 0})
