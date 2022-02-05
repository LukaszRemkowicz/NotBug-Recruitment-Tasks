import sys
from typing import Tuple, Union

from flask import request, make_response, jsonify, Response
from flask_api import status

import models


@models.app.route('/task', methods=['POST'])
def create_task() -> Response:
    """ create a new task """

    # breakpoint()

    data = request.get_json()
    new_task = models.TodoModel(name=data['name'], content=data['content'], complete=False)

    models.db.session.add(new_task)
    models.db.session.commit()

    return make_response(jsonify('New task has been created'), 200)


@models.app.route('/task', methods=['GET'])
def get_all_tasks() -> Union[Response, Tuple[Response, str]]:
    """ Get all task with given filtes. Result is paginated """

    filters = {
        'all': lambda curr_page, pg_size: models.TodoModel.query.paginate(
            int(curr_page),
            int(pg_size),
            False
        ),
        'completed': lambda curr_page, pg_size: models.TodoModel.query.filter_by(
            complete=True
        ).paginate(int(curr_page), int(page_size), False),
        'not_completed': lambda curr_page, pg_size: models.TodoModel.query.filter_by(
            complete=False,
        ).paginate(int(curr_page), int(page_size), False)
    }

    page_size = request.args.get('page_size', None)
    current_page = request.args.get('current_page', None)
    filter_args = request.args.get('filter', None)

    try:
        task_query = filters[filter_args](current_page, page_size)
    except KeyError:
        return make_response(jsonify('Filter not found'))

    task_items = task_query.items
    total = len(task_items)

    result = []

    for task in task_items:
        task_data = {
            'name': task.name,
            'id': task.id,
            'content': task.content,
            'complete': task.complete
        }
        result.append(task_data)

    response = jsonify(
        {
            'total': total,
            'page_size': int(page_size),
            'current_page': int(current_page),
            'items': result
        }
    )

    return response, status.HTTP_201_CREATED


@models.app.route('/task/<id>', methods=['PUT'])
def update_task(id: int) -> Response:
    """ Update task """

    data = request.get_json()

    name = data.get('name')
    content = data.get('content')
    complete = data.get('complete')

    task = models.TodoModel.query.filter_by(id=id).first()

    if not task:
        return make_response(jsonify("Task not found"), 404)

    task.name = name
    task.content = content
    task.complete = complete

    models.db.session.commit()

    return make_response(jsonify(f'Task with id {id} updated'), 200)


@models.app.route('/task/<id>', methods=['PATCH'])
def update_one_field_task(id: int) -> Response:
    """ Update just one field in task """

    data = request.get_json()

    name = data.get('name')
    content = data.get('content')
    complete = data.get('complete')

    task = models.TodoModel.query.filter_by(id=id).first()

    if not task:
        return make_response(jsonify("Task not found"), 404)

    if name:
        task.name = name
    if content:
        task.content = content
    if complete != task.complete:
        models.app.logger.info('jestem w complete')
        task.complete = complete
        models.app.logger.info(task.complete)

    models.db.session.commit()

    return make_response(jsonify(f'Task with id {id} updated'), 200)


@models.app.route('/task/<id>', methods=['GET'])
def get_one_task(id: int) -> Response:
    """ Get one task """

    task = models.TodoModel.query.filter_by(id=id).first()

    if not task:
        return make_response(jsonify(f'Task with id {id} not found'))

    return make_response(jsonify(
        {
            'id': task.id,
            'name': task.name,
            'content': task.content,
            'complete': task.complete
        }
    ), 200)


@models.app.route('/task/<id>', methods=['DELETE'])
def delete_task(id: int) -> Response:
    """ Delete task """

    task = models.TodoModel.query.filter_by(id=id).first()

    if not task:
        return make_response(jsonify(f'Task with id {id} not found'))

    models.db.session.delete(task)
    models.db.session.commit()

    return make_response(jsonify(f'Task with id {id} has been deleted'))


if __name__ == "__main__":
    models.app.run(debug=True)
