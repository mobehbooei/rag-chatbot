from flask import Flask, jsonify, request

app = Flask(__name__)

# Main route
@app.route('/')
def main():
    return 'You are in the main route!'
    
# ask chatbot endpoint
@app.route('/ask', methods=['POST'])
def ask():
    return 'This is your question: ' + request.get_json().get('question')

# if __name__ == '__main__':
#     app.run(debug=True)