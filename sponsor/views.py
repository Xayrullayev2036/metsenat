from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from sponsor.models import Sponsor
from sponsor.serializers import SponsorSerializer, SponsorCreateSerializer, SponsorListSerializers, \
    SponsorDetailSerializers, SponsorUpdateSerializer


class SponsorViewSet(ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return SponsorCreateSerializer
        elif self.action in ("update", "partial_update"):
            return SponsorUpdateSerializer
        elif self.action == "list":
            return SponsorListSerializers
        elif self.action == "retrieve":
            return SponsorDetailSerializers
        return SponsorSerializer
