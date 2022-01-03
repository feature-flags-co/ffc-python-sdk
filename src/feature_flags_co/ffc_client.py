import requests
import json

class FfcClient:
    __api_base_rl = 'https://api.feature-flags.co'
    

    def __init__(self, env_secret, user, api_url='https://api.feature-flags.co'):
        self.env_secret = env_secret
        self.user = user
        self.__api_base_rl = api_url

    def variation(self, feature_flag_key, default_result='false'):
        payload = {
            'featureFlagKeyName': feature_flag_key,
            'environmentSecret': self.env_secret,
            'ffUserName': self.user.user_name,
            'ffUserEmail': self.user.email,
            'ffUserCountry': self.user.country,
            'ffUserKeyId': self.user.key,
            'ffUserCustomizedProperties': self.user.customize_properties
        }

        headers = {'content-type': 'application/json'}

        try:
            result = requests.post(self.__api_base_rl + '/Variation/GetMultiOptionVariation', data=json.dumps(payload), headers=headers)

            if result.status_code == 200:
                return result.json().get('variationValue', default_result)
            else:
                return default_result
        except: # catch *all* exceptions
            return default_result

    def variations(self):
        payload = {
            'userName': self.user.user_name,
            'email': self.user.email,
            'country': self.user.country,
            'userKeyId': self.user.key,
            'customizedProperties': self.user.customize_properties
        }

        headers = { 'content-type': 'application/json', 'envSecret': self.env_secret }
        default_result = []

        try:
            result = requests.post(self.__api_base_rl + '/api/public/feature-flag/variations', data=json.dumps(payload), headers=headers)

            if result.status_code == 200:
                return [{'key_name': r['keyName'], 'variation': r['variation']} for r in result.json().get('data', default_result)]
            else:
                return default_result
        except Exception as e: # catch *all* exce@ptions
            return default_result
