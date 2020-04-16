from ldap3 import Server, Connection, ALL

LDAP_URL = '10.103.52.129'


def get_LDAP_user(username, password):
    try:
        server = Server(LDAP_URL, get_info=ALL)
        connection = Connection(server,
                                'uid={username},ou=cjkk,dc=cjkk,dc=com'.format(
                                    username=username),
                                password, auto_bind=True)

        connection.search('ou=cjkk,dc=cjkk,dc=com', '({attr}={login})'.format(
            attr='uid', login=username), attributes=['cn'])

        if len(connection.response) == 0:
            return None

        return connection.response[0]
    except:
        return None