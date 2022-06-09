from flask import Flask,jsonify,request

app = Flask(__name__)
contacts = [
    {
        'id':1,
        'name':'Raju',
        'contact':'9987644456',
        'done': False
    },
    {
        'id':2,
        'name':'Rahul',
        'contact':'9876543222',
        'done': False
    }
]

@app.route("/add-data",methods = ["POST"])

def addContact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)

    contact = {
        'id':contacts[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done': False
    }
    contacts.append(contact)
        
    return jsonify({
        "status":"success",
        "message":"Contacts added successfully"
    })

@app.route("/get-data")

def getContact():
    return jsonify({
        "data":contacts
    })

if(__name__ == "__main__"):
    app.run(debug = True)