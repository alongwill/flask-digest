# flask-digest
Simple Flask server with REST endpoints

## Running

```
docker-compose up
```

## Testing

Add a message and retrieve it's digest
```bash
curl --cacert certs/cacert.crt -X POST -H "Content-Type: application/json" -d '{"message": "foo"}' https://localhost:5000/messages
{
  "digest": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"
}
```

Lookup a message from it's digest
```bash
curl --cacert certs/cacert.crt https://localhost:5000/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae
{
  "message": "foo"
}
```


## Versions
Tested with:
* Docker Engine CE 18.09.1
* Docker Compose 1.23.2
