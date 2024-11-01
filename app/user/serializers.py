from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'nombre',
            'primer_apellido',
            'segundo_apellido',
            'imagen',
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8
            }
        }

    def create(self, validated_data):
        """ Create, save and return a user with encrypted password. """

        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """ Update and auth user. """

        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
