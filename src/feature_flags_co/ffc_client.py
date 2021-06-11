import requests
import json


class FfcClient:
    __api_base_rl = 'https://api.feature-flags.co'
    __variation_url_part = '/Variation/GetUserVariationResultInJson'

    def __init__(self, env_secret, user):
        self.env_secret = env_secret
        self.user = user

    def variation(self, feature_flag_key, default_result=True):
        payload = {
            'featureFlagKeyName': feature_flag_key,
            'environmentSecret': self.env_secret,
            'ffUserName': self.user.user_name,
            'ffUserEmail': self.user.email,
            'ffUserCountry': self.user.country,
            'ffUserKeyId': self.user.key,
            'ffUserCustomizedProperties': self.user.customize_properties
        }

        try:
            result = requests.post(self.__api_base_rl + self.__variation_url_part, data=json.dumps(payload))

            if result.status_code == 200:
                return result.json().get('variationResult', default_result)
            else:
                return default_result
        except: # catch *all* exceptions
            return default_result
