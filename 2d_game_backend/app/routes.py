from flask import Blueprint, jsonify, request

from .game_logic import transform_list_to_2d_array

main = Blueprint('main', __name__)

@main.route('/transform', methods=['POST'])
def transform():
    data = request.json
    one_d_list = data['list']
    try:
        two_d_array = transform_list_to_2d_array(one_d_list)
        return jsonify(two_d_array), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
