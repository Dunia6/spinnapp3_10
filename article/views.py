from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from .serializers import ArticleSerializer, ArticleImageSerializer, ArticleDetailSerializer, ArticleUpdateSerializer
from .models import Article, ArticleImage
from marketplace.models import Marketplace
from marketplace.serializers import MarketplaceSerializer
# Create your views here.


class ArticleCreateView(APIView):
    """ Crée un article dans une marketplace """
    def post(self, request):
        data = request.data
        marketplace = Marketplace.objects.get(pk=data['marketplace'])
        if marketplace.user != request.user:
            return Response({'error': 'Vous n\'êtes pas propriétaire de cette marketplace.'}, status=403)

        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            article = serializer.save(marketplace=marketplace)
            # Gestion des images
            images = request.FILES.getlist('images')  # Récupérez les images
            for image in images:
                ArticleImage.objects.create(article=article, image=image)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleListView(APIView):
    """ Liste des articles """
    def get(self, request):
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticlelistByMarketplace(APIView):
    """ Liste des articles par marketplace """
    def get(self, request, pk=None):
        try:
            marketplace = Marketplace.objects.get(pk=pk)
        except Marketplace.DoesNotExist:
            return Response({'error': 'Marketplace introuvable !'}, status=400)

        articles = Article.objects.filter(marketplace=marketplace)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleUpdateView(APIView):
    """ Modification d'un article """
    def put(self, request, pk=None):
        if pk:
            id = pk
        try:
            article = Article.objects.get(pk=id)
            
        except Article.DoesNotExist:
            return Response({'error' : "Cet article n'existe pas !"}, status=status.HTTP_400_BAD_REQUEST)

        if article.marketplace.user != request.user:
            return Response({'error': 'Vous n\'etes pas propriétaire de cet article.'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = ArticleUpdateSerializer(article, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            # A revoir
            """ for image_data in request.data.getlist('additional_images', []):
                image, created = ArticleImage.objects.get_or_create(pk=image_data.get('id', None), article=article)
                if not created:

                    image.image = image_data.get('image', image.image)
                    image.save() """
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ArticleDetailView(APIView):
    """ Les détails de l'article """
    def get(self, request, pk):
        try:
            article = Article.objects.prefetch_related('additional_images').get(pk=pk)
            marketplace = article.marketplace
            
            location = marketplace.location
            latitude = location.split(',')[0]
            longitude = location.split(',')[1]
            user_location = request.headers.get('X-Forwarded-For', request.META.get('REMOTE_ADDR'))
            print(user_location)
            
        except Article.DoesNotExist:
            return Response({'error': 'Article introuvable !'}, status=status.HTTP_400_BAD_REQUEST)
        
        article_serializer = ArticleDetailSerializer(article)
        marketplace_serializer = MarketplaceSerializer(marketplace)
        
        data = {
            'article': article_serializer.data,
            'marketplace': marketplace_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)


class ArticleDeleteView(APIView):
    """ Suppression d'un article """
    def delete(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response({'error': 'Article introuvable !'}, status=status.HTTP_400_BAD_REQUEST)
        
        if article.marketplace.user != request.user:
            return Response({'error': 'Vous n\'etes pas propriétaire de cet article.'}, status=status.HTTP_403_FORBIDDEN)
        
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

