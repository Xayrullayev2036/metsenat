from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from sponsor.choices import SponsorTypeChoices
from sponsor.models import Sponsor


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = "__all__"


class SponsorListSerializers(serializers.ModelSerializer):
    # spent_amount = serializers.SerializerMethodField("get_spent_amount", read_only=True)

    class Meta:
        model = Sponsor
        fields = ["id", "fullname", "phone_number", "payment_amount", "created_at", "status"]

    # def get_spend_amount(self):
    #     return 0


class SponsorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ["id", "fullname", "phone_number", "payment_amount", "company_name", "status", "created_at"]


class SponsorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        exclude = ["created_at", "updated_at"]
        # fields = ["id","fullname","payment_type"]
    def validate(self, attrs):
        if attrs.get("type") == SponsorTypeChoices.YURIDIK.value:
            if not attrs.get("company_name"):
                raise ValidationError(f"Organization is required when sponsor type {SponsorTypeChoices.YURIDIK.value}")
        elif attrs.get("type") == SponsorTypeChoices.JISMONIY.value:
            attrs["company_name"] = None
        return attrs


class SponsorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        # fields = ["id","fullname","payment_type"]
        exclude = ["created_at", "updated_at"]

    def validate(self, attrs):
        if attrs.get("type") == SponsorTypeChoices.YURIDIK.value:
            if not attrs.get("company_name"):
                raise ValidationError(f"Organization is required when sponsor type {SponsorTypeChoices.YURIDIK.value}")
        elif attrs.get("type") == SponsorTypeChoices.JISMONIY.value:
            attrs["company_name"] = None
        return attrs
