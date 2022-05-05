import requests
import json

from feature_flags_co.ffc_user import FfcUser

class FfcClient:
    __api_base_rl = 'https://api.feature-flags.co'
    

    def __init__(self, env_secret, user, api_url='https://api.featureflag.co'):
        self.env_secret = env_secret
        self.user = user
        self.__api_base_rl = api_url

    def variation(self, feature_flag_key, default_result='false'):
        payload = {
            'featureFlagKeyName': feature_flag_key,
            'userName': self.user.user_name,
            'email': self.user.email,
            'country': self.user.country,
            'userKeyId': self.user.key,
            'customizedProperties': self.user.customize_properties
        }

        headers = { 'content-type': 'application/json', 'envSecret': self.env_secret }

        try:
            response = requests.post(self.__api_base_rl + '/api/public/feature-flag/variation', data=json.dumps(payload), headers=headers)
             
            if response.status_code == 200:
                result = response.json()
                data = result.get('data')
                if result.get('success') == True and data != None:
                    return result.get('data').get('variation', default_result)
                
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
                return [{'key_name': r['keyName'], 'variation': r['variation'], 'id': r.get('id'), 'name': r.get('name', ''), 'reason': r.get('reason', '')} for r in result.json().get('data', default_result)]
            else:
                return default_result
        except Exception as e: # catch *all* exce@ptions
            return default_result
