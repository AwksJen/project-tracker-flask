"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template
import hackbright

app = Flask(__name__)


@app.route('/search')
def search_student():
    """Display a search form. """

    return render_template('student_search.html')


@app.route('/student')
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    # return f'{github} is the GitHub account for {first} {last}'

    return render_template('student_info.html',
                           first_name=first,
                           last_name=last,
                           github_user=github)


@app.route('/get_info')
def get_student_info():
    """Display form for collecting new student information."""

    return render_template('new_student_info.html')


@app.route('/add_student')
def add_student():
    """Add new student to database. """

    first_name = request.args.get('f_name')

    print(f'first name: {first_name}')


if __name__ == '__main__':
    hackbright.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
