from rest_framework.serializers import ModelSerializer
from citation.models import Citation



class CitationSerializer(ModelSerializer):

    class Meta:
        model = Citation
        fields = '__all__'