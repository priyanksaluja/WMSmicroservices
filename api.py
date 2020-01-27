from flask import Flask, jsonify, request
import functions
app = Flask(__name__)


@app.route("/")
def hello():
    '''
    :return: text defined below
    '''
    return "Welcome to Flask home page"


@app.route("/getcustomer")
def querystring():
    '''
    :return: records with matching customer name
    '''
    params = request.args['q']
    data = functions.getcustomerdetails(params)
    return jsonify(data['payload']), data['status_code']


@app.route("/api/<table>", methods=["POST", "GET", "PUT"])
def cruapi_models(table):
    '''
    :param table: model name on which the operation needs to be performed
    :return: status code in case of post and put .. status code and data from tables in case of get call
    Description: call the respective function as per table name and pass the json data to it
    '''
    if table is None or table not in ['sku', 'storage', 'order', 'orderline']:
        data = { 'payload': { 'message': 'Undefined id or Table name' },
                'status_code': 300  # Indicates that the client must take some additional action in order to complete their request
            }
        return jsonify(data['payload']), data['status_code']
    else:
        if request.method == 'POST':
            datadict = {
                'skuid': request.json.get('skuid', None),
                'product_name': request.json.get('product_name', None),
                'storageid': request.json.get('storageid', None),
                'stock': request.json.get('stock', None),
                'customer_name': request.json.get('customer_name', None),
                'orderid': request.json.get('orderid', None),
                'orderlineid': request.json.get('orderlineid', None),
                'quantity': request.json.get('quantity', None)
            }
            if table == 'sku':
                data = functions.createSku(datadict)
            elif table == 'storage':
                data = functions.createStorage(datadict)
            elif table == 'order':
                data = functions.createOrder(datadict)
            elif table == 'orderline':
                data = functions.createOrderLine(datadict)
            else:
                data = {
                    'payload': {'message': 'Invalid table name'},
                    'status_code': 500
                }
            return jsonify(data['payload']), data['status_code']

        if request.method == 'GET':
            data = functions.fetchdata(table)
            return jsonify(data['payload']), data['status_code']

        if request.method == 'PUT':
            datadict = {
                'skuid': request.json.get('skuid', None),
                'product_name': request.json.get('product_name', None),
                'storageid': request.json.get('storageid', None),
                'stock': request.json.get('stock', None),
                'customer_name': request.json.get('customer_name', None),
                'orderid': request.json.get('orderid', None),
                'orderlineid': request.json.get('orderlineid', None),
                'quantity': request.json.get('quantity', None)
            }
            if table == 'sku':
                data = functions.updateSku(datadict)
            elif table == 'storage':
                data = functions.updateStorage(datadict)
            elif table == 'order':
                data = functions.updateOrder(datadict)
            elif table == 'orderline':
                data = functions.updateOrderLine(datadict)
            else:
                data = {
                    'payload': {'message': 'Invalid table name'},
                    'status_code': 500
                }
            return jsonify(data['payload']), data['status_code']


@app.route('/api/<table>/<id>', methods=['DELETE'])
def dapi_models(table, id):
    if table is None or table not in ['sku', 'storage', 'order', 'orderline']:
        data = { 'payload': { 'message': 'Undefined id or Table name' },
                'status_code': 300  # Indicates that the client must take some additional action in order to complete their request
            }
        return jsonify(data['payload']), data['status_code']
    else:
        if request.method == 'DELETE':
            data = functions.deletedata(table, id)
            return jsonify(data['payload']), data['status_code']


@app.route("/api/placeorder", methods=["GET"])
def placeorder():
    '''
    :input: data containing order details
    :return: status code and a list of the "picks" required, and from storage
    '''
    if request.method == 'GET':
        params = request.json['lines']
        data = functions.fetchorderdetails(params)
        return jsonify(data['payload']), data['status_code']


if __name__ == "__main__":
    app.run()