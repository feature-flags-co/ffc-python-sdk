class FfcUser:

    def __init__(self, user_name, email, key, customize_properties=[], country=''):
        self.user_name = user_name
        self.email = email
        self.country = country
        self.key = key
        self.customize_properties = customize_properties
