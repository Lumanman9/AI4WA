from datetime import timedelta
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class HasuraTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add Hasura claims
        token['https://hasura.io/jwt/claims'] = {
            # 'x-hasura-default-role': 'user',  # default role for user
            'x-hasura-allowed-roles': ['user', 'admin'] if user.is_staff else ['user'],
            'x-hasura-default-role': 'admin' if user.is_staff else 'user',
            'x-hasura-user-id': str(user.id),
            # Add any custom claims you want
            # 'x-hasura-org-id': str(user.organization_id),
            # 'x-hasura-custom': 'custom-value'
        }

        return token
