from rest_framework import serializers

from .models import Article, ArticleImage



class ArticleSerializer(serializers.ModelSerializer):
    """ Serializer de l'article """
    marketplace = serializers.ReadOnlyField(source='marketplace.name')
    class Meta:
        model = Article
        fields = ['id','main_image', 'name', 'category', 'description', 'price', 'marketplace', 'created_time', 'updated_time', 'active']
        
    
    def create(self, validated_data):
        return Article.objects.create(**validated_data)
    
    
class ArticleImageSerializer(serializers.ModelSerializer):
    """ Serializer for ArticleImage model """
    class Meta:
        model = ArticleImage
        fields = ['id', 'image', 'article']
    
    
    
class ArticleDetailSerializer(serializers.ModelSerializer):
    """ Serializer for Article model with details """
    additional_images = ArticleImageSerializer( many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'name', 'category', 'description', 'price', 'marketplace', 'main_image', 'created_time', 'updated_time', 'active', 'additional_images']


class ArticleUpdateSerializer(serializers.ModelSerializer):
    """ Sérialiseur pour le modèle Article avec des fonctionnalités de mise à jour """
    additional_images = ArticleImageSerializer(many=True)

    class Meta:
        model = Article
        fields = ('id', 'name', 'category', 'description', 'price', 'marketplace', 'main_image', 'active', 'additional_images')

    def update(self, instance, validated_data):

        for field, value in validated_data.items():
            if field == 'additional_images':
                continue
            setattr(instance, field, value)
        instance.save()

        # La mise à jour ou la création d'images supplémentaires est gérée dans la vue

        return instance