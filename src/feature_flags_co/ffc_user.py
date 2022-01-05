class FfcUser:

    def __init__(self, user_name, email, key, customize_properties=[], country=''):
        if user_name == '' or user_name == None:
            raise Exception("user_name cannot be empty or None")

        if key == '' or key == None:
            raise Exception("key cannot be empty or None")

        self.user_name = user_name
        self.email = email
        self.country = country
        self.key = key
        self.customize_properties = customize_properties
