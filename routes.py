import json
import logging
from flask import Blueprint, jsonify, request, jsonify

logger = logging.getLogger(__name__)

template_app = Blueprint('template_app', __name__)


@template_app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'GET':
        logger.info("calling method: home")
        return "success"
        # user_id_to_enroll=request.json['user_id']
        # image_format = request.json['format']
        # image_for_enrollment = request.json['enrollment_images']
        # data_dir = base64_to_image(user_id_to_enroll, image_for_enrollment, 'train', image_format)
        # print(data_dir)
        #
        # return jsonify(resultJson)

if __name__ == '__main__':
    template_app.run(host='0.0.0.0', port=7319, debug=True)
