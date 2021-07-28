from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from rest_framework import serializers


class ReadOnlyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_active', 'last_login', 'is_superuser',)


class WriteOnlyUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'is_active',)
        extra_kwargs = {
            'username': {
                'required': True,
                'validators': [
                    RegexValidator(
                        r'^[\w.@+-]+$', 'Letters, digits and @/./+/-/_ only.'
                    ),
                ],
            },
            'password': {
                'required': True,
                'validators': [
                    RegexValidator(
                        r'^(?=.*[A-Z])(?=.*\d).{8,}$', 'Minimum eight characters, at least one letter and one number.'
                    ),
                ],
            },
            'is_active': {'required': True},
        }

    def to_representation(self, instance: str) -> dict[str, str]:
        user: User = User.objects.get(username=instance)
        return ReadOnlyUserSerializer(user).data

    def validate(self, data):
        if not data:
            raise serializers.ValidationError("Must include at least one field")
        return data

    def validate_username(self, value: str) -> str:
        check_query = User.objects.filter(username=value)
        if self.instance:
            check_query = check_query.exclude(pk=self.instance.pk)

        if check_query.exists():
            raise serializers.ValidationError('A User with this username exists')
        return value
