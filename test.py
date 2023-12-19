from flask import Flask, jsonify, request

app = Flask(__name__)

exchange_rates = {
    "TWD": {"TWD": 1, "JPY": 3.669, "USD": 0.03281},
    "JPY": {"TWD": 0.26956, "JPY": 1, "USD": 0.00885},
    "USD": {"TWD": 30.444, "JPY": 111.801, "USD": 1},
}

@app.route('/', methods=['GET'])
def convert_currency():
    source = request.args.get('source')
    target = request.args.get('target')
    amount_str = request.args.get('amount')

    if not source or not target or not amount_str:
        return jsonify({'msg': 'Missing required parameters'}), 400

    try:
        amount = float(amount_str.replace('$', '').replace(',', ''))
        print(f"amount是{amount}")
    except ValueError:
        return jsonify({'msg': 'Invalid amount format'}), 400

    if source not in exchange_rates or target not in exchange_rates[source]:
        return jsonify({'msg': 'Invalid currency code'}), 400

    exchange_rate = exchange_rates[source][target]

    converted_amount = round(amount * exchange_rate, 2)
    # print(f"轉換後的金額是: {converted_amount}")

    formatted_amount = "${:,.2f}".format(converted_amount)
    # print(f"格式化後的金額是: {formatted_amount}")
    
    result = {
        'msg': 'success',
        'amount': formatted_amount
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
