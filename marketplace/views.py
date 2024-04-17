from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import MarketplaceSerializer
from article.serializers import ArticleSerializer

from .models import Marketplace
from article.models import Article
# Create your views here.


class MarketplaceCreateView(APIView):
    """ Vue de la creation d'une marketplace """
    def post(self, request):
        user = request.user
        serializer = MarketplaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class MarketplaceListView(APIView):
    """ Vue de la liste des marketplaces """
    def get(self, request):
        marketplace = Marketplace.objects.filter(active=True)
        serializer = MarketplaceSerializer(marketplace, many=True)
        return Response(serializer.data)


class MarketplaceUpdateView(APIView):
    """ Vue de la modification d'une marketplace """
    def put(self, request, pk):
        try:
            marketplace = Marketplace.objects.get(pk=pk)
        except Marketplace.DoesNotExist:
            return Response({'error': 'Marketplace introuvable !'}, status=400)
        
        if marketplace.user != request.user:
            return Response({'error': 'Vous ne pouvez modifier que votre propre marketplace'}, status=403)
        
        serializer = MarketplaceSerializer(marketplace, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)



class MarketplaceDeleteView(APIView):
    """ Vue de la suppression d'une marketplace """
    def delete(self, request, pk):
        try:
            marketplace = Marketplace.objects.get(pk=pk)
        except Marketplace.DoesNotExist:
            return Response({'error': 'Marketplace introuvable !'}, status=400)
        
        if marketplace.user != request.user:
            return Response({'error': 'Vous ne pouvez supprimer que votre propre marketplace'}, status=403)
        
        marketplace.delete()
        return Response({'message': 'Marketplace supprimé avec succès !'}, status=204)



class MarketplaceDetailView(APIView):
    """ Vue de la liste des marketplaces """
    
    def get(self, request, pk):
        try:
            marketplace = Marketplace.objects.get(pk=pk)
        except Marketplace.DoesNotExist:
            return Response({'error': 'Marketplace introuvable !'}, status=400)
        
        articles = Article.objects.filter(marketplace=marketplace)
        
        marketplace_serializer = MarketplaceSerializer(marketplace)
        articles_serializer = ArticleSerializer(articles, many=True)
        
        data = {
            'marketplace': marketplace_serializer.data,
            'articles': articles_serializer.data
        }
        
        return Response(data)