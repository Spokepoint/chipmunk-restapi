from bottle import Bottle, run, request, response
from controller import spreadsheet as ss

app = Bottle()


@app.post('/api/v1/cell')
def post_cell():
    """
    Writes to a spreadsheet cell.

    POST a JSON with 'worksheet', 'row', 'col', and 'value' keys.
    HTTP request header must set Content-Type to application/json.
    """
    data = request.json
    attr = ('worksheetKey', 'row', 'col', 'value')

    if data is not None and all(key in data for key in attr):
        ss.write_cell(data[attr[0]],    # worksheet key
                      data[attr[1]],    # row
                      data[attr[2]],    # col
                      data[attr[3]])    # value
        response.status = '201 Created'
    else:
        response.status = '400 Bad Request'

    return response

if __name__ == "__main__":
    run(app, host='localhost', port=8080, reloader=True, debug=True)
