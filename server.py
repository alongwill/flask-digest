from flask import Flask, request, make_response, jsonify
import hashlib

app = Flask(__name__)

# Dict of messages received by the server
received_messages = {}

@app.route('/messages', methods=['POST'])
def post_handler():    
    data = request.get_json()
    sha256_digest = hashlib.sha256(data['message'].encode('utf-8')).hexdigest()

    # Keep track of messages we've received.
    received_messages[sha256_digest] = data['message']

    return jsonify(digest=sha256_digest), 201
        
@app.route('/messages/<a_digest>', methods=['GET'])
def get_handler(a_digest):
    if a_digest in received_messages:
        return jsonify(message=received_messages[a_digest])
    else:
        return jsonify(err_msg="Message not found"), 404

if __name__ == '__main__':
    context = ('certs/cacert.crt', 'certs/key.pem')
    app.run(debug=True, host='0.0.0.0', ssl_context=context)
