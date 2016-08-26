1. Add in a proper AuthManager instead of the list version that was being used.
Added support for all Auth types that python supports


edfdef23963ab1c5a0424f16f97cdc39dccae34a


core 中 81 - 84 行

        if isinstance(auth, (list, tuple)):
            auth = AuthObject(*auth)
        if not auth:
            auth = auth_manager.get_auth(self.url)
是不需要的
