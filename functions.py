import models
from unidecode import unidecode


def validateSku(skuid):
    '''
    :param skuid: id field in Sku model.
    :return: Boolean value i.e. True if data is available in Sku model else False
    '''
    return True if models.Sku.query.filter_by(id=skuid).first() else False


def createSku(params):
    '''
    :param params: Dictionary of elements to be inserted in sku model
    :return: status code and message
    Status = 200 and message = records created successfully if data will be saved successfully to models
    Status = 200 and message = record already exist if record with same id already exists
    Status = 400 and message = error message if there is any error while inserting record
    '''
    try:
        skuid = int(params['skuid'])
        product_name = params['product_name']
        if validateSku(skuid):
            resp = {
                'payload': {'message': 'Record already exists'},
                'status_code': 200
            }
        else:
            newsku = models.Sku(skuid, product_name)
            models.db.session.add(newsku)
            models.db.session.commit()
            resp = {
                'payload': {'message': 'Record created successfully'},
                'status_code': 200
            }
    except Exception as e:
        resp = {
            'payload': {'message': str(e)},
            'status_code': 400
        }
    return resp


def validateStorage(storageid, skuid):
    '''
    :param storageid: id field in Storage model.
    :param skuid: id field which is foreign Key in Storage model for SKU model
    :return: Boolean value i.e. True if data is available in Sku model and skuid exist is SKu model else False
    '''
    return True if models.Storage.query.filter_by(id=storageid).first() or not models.Sku.query.filter_by(id=skuid).first() else False


def createStorage(params):
    '''
    :param params: Dictionary of elements to be inserted in Storage model
    :return: status code and message
    Status = 200 and message = records created successfully if data will be saved successfully to models
    Status = 200 and message = record already exist if record with same id already exists
    Status = 400 and message = error message if there is any error while inserting record
    '''
    try:
        storageid = int(params['storageid'])
        stock = params['stock']
        skuid = int(params['skuid'])

        if validateStorage(storageid, skuid):
            resp = {
                'payload': {'message': 'Invalid record'},
                'status_code': 200
            }
        else:
            newstorage = models.Storage(storageid, stock, skuid)
            models.db.session.add(newstorage)
            models.db.session.commit()
            resp = {
                'payload': {'message': 'Record created successfully'},
                'status_code': 200
            }
    except Exception as e:
        resp = {
            'payload': {'message': str(e)},
            'status_code': 400
        }
    return resp


def validateOrder(orderid):
    '''
    :param orderid: id field in Order table.
    :return: Boolean value i.e. True if data is available in Order model else False
    '''
    return True if models.Order.query.filter_by(id=orderid).first() else False


def createOrder(params):
    '''
    :param params: Dictionary of elements to be inserted in Order model
    :return: status code and message
    Status = 200 and message = records created successfully if data will be saved successfully to models
    Status = 200 and message = record already exist if record with same id already exists
    Status = 400 and message = error message if there is any error while inserting record
    '''
    try:
        orderid = int(params['orderid'])
        customer_name = params['customer_name']

        if validateOrder(orderid):
            resp = {
                'payload': {'message': 'Record already exists'},
                'status_code': 200
            }
        else:
            neworder= models.Order(orderid, customer_name)
            models.db.session.add(neworder)
            models.db.session.commit()
            resp = {
                'payload': {'message': 'Record created successfully'},
                'status_code': 200
            }
    except Exception as e:
        resp = {
            'payload': {'message': str(e)},
            'status_code': 400
        }
    return resp


def validateOrderLine(orderlineid, skuid):
    '''
    :param orderlineid: id field in OrderLine model.
    :param skuid: id field which is foreign Key in OrderLine model for SKU model
    :return: Boolean value i.e. True if data is available in OrderLine model else False
    '''
    return True if models.OrderLine.query.filter_by(id=orderlineid).first() or not models.Sku.query.filter_by(id=skuid).first() else False


def createOrderLine(params):
    '''
    :param params: Dictionary of elements to be inserted in OrderLine model
    :return: status code and message
    Status = 200 and message = records created successfully if data will be saved successfully to models
    Status = 200 and message = record already exist if record with same id already exists
    Status = 400 and message = error message if there is any error while inserting record
    '''
    try:
        orderlineid = int(params['orderlineid'])
        skuid = int(params['skuid'])
        quantity = int(params['quantity'])

        if validateOrderLine(orderlineid, skuid):
            resp = {
                'payload': {'message': 'Invalid record'},
                'status_code': 200
            }
        else:
            neworder = models.OrderLine(orderlineid, skuid, quantity)
            models.db.session.add(neworder)
            models.db.session.commit()
            resp = {
                'payload': {'message': 'Record created successfully'},
                'status_code': 200
            }
    except Exception as e:
        resp = {
            'payload': {'message': str(e)},
            'status_code': 400
        }
    return resp


def fetchdata(table):
    '''
    :param table: table name from where the data needs to be fetched
    :return: status code and records
    Status = 200 and all records available in model
    Status = 400 and error message if there is any error fetching records
    '''
    try:
        data = []
        if table == 'sku':
            records = models.Sku.query.all()
            for record in records:
                datadict = {}
                datadict['id'] = record.id
                datadict['ProductName'] = record.product_name
                data.append(datadict)
        elif table == 'storage':
            records = models.Storage.query.all()
            for record in records:
                datadict = {}
                datadict['id'] = record.id
                datadict['stock'] = record.stock
                x = models.Sku.query.filter_by(id=record.sku).first()
                datadict['sku'] = x.product_name
                data.append(datadict)
        elif table == 'order':
            records = models.Order.query.all()
            for record in records:
                datadict = {}
                datadict['id'] = record.id
                datadict['CustomerName'] = record.customer_name
                data.append(datadict)
        elif table == 'orderline':
            records = models.OrderLine.query.all()
            for record in records:
                datadict = {}
                datadict['id'] = record.id
                datadict['quantity'] = record.quantity
                x = models.Sku.query.filter_by(id=record.sku).first()
                datadict['sku'] = x.product_name
                data.append(datadict)
        resp = {
            'payload': data,
            'status_code': 200
        }
    except Exception as e:
        resp = {
            'payload': {'message': str(e)},
            'status_code': 400
        }
    return resp


def updateSku(params):
    '''
    :param params: Dictionary of elements to be updated in sku model
    :return: status code and message
    Status = 200 and message = records updated successfully if data will be saved successfully to models
    Status = 400 and message = error message if there is any error while inserting record
    '''
    try:
        skuid = int(params['skuid'])
        product_name = params['product_name']
        record = models.Sku.query.filter_by(id=skuid).first()
        if record and product_name:
            record.product_name = product_name
            models.db.session.commit()
            resp = {
                'payload': {'message': 'Record updated successfully'},
                'status_code': 200
            }
        else:
            resp = {
                'payload': {'message': 'Invalid data'},
                'status_code': 200
            }
    except Exception as e:
        resp = {
            'payload': {'message': str(e)},
            'status_code': 400
        }
    return resp


def updateStorage(params):
    '''
    :param params: Dictionary of elements to be updated in Storage model
    :return: status code and message
    Status = 200 and message = record created successfully if data will be saved successfully to model
    Status = 400 and message = error message if there is any error while inserting record
    '''
    try:
        storageid = int(params['storageid'])
        stock = params['stock']
        skuid = int(params['skuid'])
        record = models.Storage.query.filter_by(id=storageid).first()
        if record:
            record.stock = stock if stock else record.stock
            record.sku = skuid if skuid and models.Sku.query.filter_by(id=skuid).first() else record.sku
            models.db.session.commit()
            resp = {
                'payload': {'message': 'Record updated successfully'},
                'status_code': 200
            }

        else:
            resp = {
                'payload': {'message': 'Invalid data'},
                'status_code': 200
            }
    except Exception as e:
        resp = {
            'payload': {'message': str(e)},
            'status_code': 400
        }
    return resp



def updateOrder(params):
    '''
    :param params: Dictionary of elements to be updated in Order model
    :return: status code and message
    Status = 200 and message = record updated successfully if data will be saved successfully to models
    Status = 400 and message = error message if there is any error while inserting record
    '''
    try:
        orderid = int(params['orderid'])
        customer_name = params['customer_name']
        record = models.Order.query.filter_by(id=orderid).first()
        if record and customer_name:
            record.customer_name = customer_name
            models.db.session.commit()
            resp = {
                'payload': {'message': 'Record updated successfully'},
                'status_code': 200
            }

        else:
            resp = {
                'payload': {'message': 'Invalid data'},
                'status_code': 200
            }
    except Exception as e:
        resp = {
            'payload': {'message': str(e)},
            'status_code': 400
        }
    return resp


def updateOrderLine(params):
    '''
    :param params: Dictionary of elements to be updated in OrderLine model
    :return: status code and message
    Status = 200 and message = record updated successfully if data will be saved successfully to models
    Status = 400 and message = error message if there is any error while inserting record
    '''
    try:
        orderlineid = int(params['orderlineid'])
        skuid = int(params['skuid'])
        quantity = int(params['quantity'])
        record = models.OrderLine.query.filter_by(id=orderlineid).first()
        if record:
            record.sku = skuid if skuid and models.Sku.query.filter_by(id=skuid).first()  else record.sku
            record.quantity = quantity if quantity else record.quantity
            models.db.session.commit()
            resp = {
                'payload': {'message': 'Record updated successfully'},
                'status_code': 200
            }

        else:
            resp = {
                'payload': {'message': 'Invalid data'},
                'status_code': 200
            }
    except Exception as e:
        resp = {
            'payload': {'message': str(e)},
            'status_code': 400
        }
    return resp



def deletedata(table, id):
    '''
    :param table: table name from where the data needs to be deleted
    :return: status code and records
    Status = 200 and message= records deleted successfully if records is deleted from model
    Status = 400 and error message if there is any error in deleting records
    '''
    try:
        if table == 'sku':
            record = models.Sku.query.filter_by(id=id).first()
            if record:
                models.db.session.delete(record)
                models.db.session.commit()
                resp = {
                    'payload': {'message': 'Record deleted successfully'},
                    'status_code': 200
                }
            else:
                resp = {
                    'payload': {'message': 'Record with id does not exist'},
                    'status_code': 200
                }
        elif table == 'storage':
            record = models.Storage.query.filter_by(id=id).first()
            if record:
                models.db.session.delete(record)
                models.db.session.commit()
                resp = {
                    'payload': {'message': 'Record deleted successfully'},
                    'status_code': 200
                }
            else:
                resp = {
                    'payload': {'message': 'Record with id does not exist'},
                    'status_code': 200
                }

        elif table == 'order':
            record = models.Order.query.filter_by(id=id).first()
            if record:
                models.db.session.delete(record)
                models.db.session.commit()
                resp = {
                    'payload': {'message': 'Record deleted successfully'},
                    'status_code': 200
                }
            else:
                resp = {
                    'payload': {'message': 'Record with id does not exist'},
                    'status_code': 200
                }
        elif table == 'orderline':
            record = models.OrderLine.query.filter_by(id=id).first()
            if record:
                models.db.session.delete(record)
                models.db.session.commit()
                resp = {
                    'payload': {'message': 'Record deleted successfully'},
                    'status_code': 200
                }
            else:
                resp = {
                    'payload': {'message': 'Record with id does not exist'},
                    'status_code': 200
                }
        else:
            resp = {
                'payload': {'message': 'Invalid data'},
                'status_code': 200
            }
    except Exception as e:
        resp = {
            'payload': {'message': str(e)},
            'status_code': 400
        }
    return resp


def fetchorderdetails(params):
    '''
    :param params: data passed on from API
    :return: status code and records
    Status = 200 and all records available in model
    Status = 400 and error message if there is any error fetching records
    '''
    try:
        data = []
        for x in params:
            quantity = int(x['quantity'])
            records = models.Sku.query.filter_by(product_name=x['sku'])
            for record in records:
                skuid = record.id
                stocks = models.OrderLine.query.filter_by(sku=skuid).order_by(models.OrderLine.quantity.asc())
                for stock in stocks:
                    datadict = {}
                    datadict['id'] = stock.id
                    if int(stock.quantity) >= quantity:
                        datadict['quantity'] = quantity
                        data.append(datadict)
                        break
                    else:
                        datadict['quantity'] = int(stock.quantity)
                        quantity = quantity - int(stock.quantity)
                        data.append(datadict)
        resp = {
            'payload': data,
            'status_code': 200
        }
    except Exception as e:
        resp = {
            'payload': {'message': str(e)},
            'status_code': 400
        }
    return resp


def getcustomerdetails(params):
    '''
    :param params: customer name passed in query string  
    :return: details from order table matching customer name
    '''
    try:
        params = unidecode(params)
        records = models.Order.query.filter(models.Order.customer_name.contains(params)).all()
        data = []
        if records:
            for record in records:
                datadict = {}
                datadict['id'] = record.id
                datadict['CustomerName'] = record.customer_name
                data.append(datadict)
        else:
            data = [{'message': 'No records found'}]
        resp = {
            'payload': data,
            'status_code': 200
        }
    except Exception as e:
        resp = {
            'payload': {'message': str(e)},
            'status_code': 400
        }
    return resp