class Bank:

    clients = []

    def __init__(self, name):
        self.name = name

    def add_client(self, client):
        self.clients.append(client)
        print(f'''
Account created successfully! Your account number is: {client.account_number}''')

    def authentication(self, name, account_number):
        for client in self.clients:
            if client.name == name and client.account_number == account_number:
                print('''
Authentication successful!''')
                return client

        print('''
Authentication failed!
Reason: account not found.''')
        return None

        