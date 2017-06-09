from oauth2_provider.models import AccessToken


class WebSocketMixin(object):
    def __init__(self):
        self.user = None
        self.access_token = None

    def error(self, message='Undefined Error', close=False):
        self.write_message({
            'status': 'error',
            'message': message
        })
        if close:
            self.close()

        return None

    def success(self, data=None, close=False):
        self.write_message({
            'status': 'success',
            'data': data
        })
        if close:
            self.close()

        return None

    def check_auth(self, data):
        if 'access_token' not in data:
            self.error(
                'Request must contain \'access_token\' parameter',
                close=True)

        token = data.get('access_token')

        if token == self.access_token:
            return True

        try:
            self.user = AccessToken.objects.get(token=token).user
            if self.user is not None:
                return self.user
            else:
                self.error(
                    'Authentication failure',
                    close=True)

        except AccessToken.DoesNotExist:
            self.error(
                'Provided access token does not match any users',
                close=True)
