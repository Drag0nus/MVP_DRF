import json

from django.views.decorators.debug import sensitive_post_parameters
from oauth2_provider.views import RevokeTokenView, TokenView
from rest_framework import parsers
from rest_framework.decorators import api_view, parser_classes, \
    permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.drf.permissions import NotAuthenticated


class MyTokenView(TokenView):
    def post(self, request, *args, **kwargs):
        url, headers, body, status = self.create_token_response(request)
        response = Response(data=json.loads(body), status=status)

        for k, v in headers.items():
            response[k] = v
        return response


@sensitive_post_parameters('password')
@api_view(['POST'])
@parser_classes([parsers.FormParser])
@permission_classes([NotAuthenticated])
def token(request):
    """
    Retrieves or refreshes access token

    The endpoint is used in the following flows: authorization code,
    password, client credentials.

    Get token:
    curl -X POST -d "client_id={client_id}&client_secret={
    client_secret}&grant_type=password&username={user_name}&password={
    password}" http://project.local/v1/auth/oauth2/token

    Refresh your token:
    curl -X POST -d "grant_type=refresh_token&client_id={
    client_id}&client_secret={client_secret}&refresh_token={
    your_refresh_token}" http://project.local/v1/auth/oauth2/token
    ---
    POST:
        serializer: ..serializers.RequestTokenSerializer
    OPTIONS:
        serializer: ..serializers.TokenSerializer
    """
    return MyTokenView().dispatch(request)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def revoke_token(request):
    """
    Revokes access token

    Sample:
    curl -X POST -d "client_id={client_id}&client_secret={
    client_secret}&token={your_token}"
    http://project.local/v1/auth/oauth2/revoke_token
    ---
    POST:
        serializer: ..serializers.RequestRevokeTokenSerializer
    """
    return RevokeTokenView().dispatch(request)
