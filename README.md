# nakamapy
A partly implemented OOP Python-Wrapper for [Nakama Server](https://github.com/heroiclabs/nakama/)

## Examples

### Client
The Client will be used to connect to the Server
```python
client = Nakama(server_key='defaultkey', server_ip='127.0.0.1', server_port=7350)
```

### Session
Sessions are used to Interact with the Server
```python
session = asyncio.get_event_loop().run_until_complete(client.authenticate_device('exampleDeviceUser'))
print(session.token)
print(session.user_id)
print(session.username)
print(session.expire_date)
print(session.is_expired)
```

### Socket
With the Socket connection you exchange realtime data with the Server
```python
socket = client.create_socket()
asyncio.get_event_loop().run_until_complete(socket.connect())
```

### Account
Use the Account Object to get all informations about the current User.
```python
account = asyncio.get_event_loop().run_until_complete(client.fetch_account(session_token=session.token))
print(account.wallet, account.user)
```
