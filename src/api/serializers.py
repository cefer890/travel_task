from ..models import CustomerInformations, PassportInformations
from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerInformations
        fields = (
            'name',
            'surname',
            'email',
            'phone'
        )


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportInformations
        fields = (
            'customer',
            'scan_file',
            'document_number',
            'first_name',
            'last_name',
            'patronymic',
            'nationality',
            'birth_date',
            'personal_number',
            'gender',
            'issue_date',
            'expire_date',
            'issuing_authority'
        )


class CustomerAndPasportCreateSerializer(serializers.HyperlinkedModelSerializer):
    customer = CustomerSerializer(many=False, required=False)

    class Meta:
        model = PassportInformations
        fields = (
            'customer',
            'scan_file',
            'document_number',
            'first_name',
            'last_name',
            'patronymic',
            'nationality',
            'birth_date',
            'personal_number',
            'gender',
            'issue_date',
            'expire_date',
            'issuing_authority'
        )

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        customer = CustomerInformations.objects.create(**customer_data)
        passport_data = dict()
        passport_data.update(**validated_data)
        passport_data.update({"customer_id":customer.id})
        pasport = PassportInformations.objects.create(**passport_data)
        return pasport
