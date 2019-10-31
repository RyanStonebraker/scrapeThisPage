from flask import request, Blueprint, jsonify

from scrapeThisPage import sqlHelpers

blueprint = Blueprint('api_v1', __name__)


@blueprint.route("/search", methods=["GET"])
def search():
    catName = request.args.get('name')
    cats = sqlHelpers.retrieveCats(catName)
    results = []
    for cat in cats:
        results.append({
            "picture": cat[0],
            "price": cat[1],
            "description": cat[2],
            "name": cat[3]
        })

    return jsonify({"results": results})
