#!/usr/bin/python3

from application import db
from application.models import Questions, Answers, Employees

db.session.remove()
db.drop_all()
db.create_all()

new_answer = Answers(answer='yes')
db.session.add(new_answer)

new_employee = Employees(employee='Waled')
db.session.add(new_employee)


question1 = Questions(question='When I am working, I think about nothing else.')
question2 = Questions(question='I get carried away by my work.')
question3 = Questions(question='When I am working, I forget everything else around me.')
question4 = Questions(question='I am totally immersed in my work.')
question5 = Questions(question='My work gives me a good feeling.')
question6 = Questions(question='I do my work with a lot of enjoyment.')
question7 = Questions(question='I feel happy during my work.')
question8 = Questions(question='I feel cheerful when I am working.')
question9 = Questions(question='I would still do this work, even if I received less pay.')
question10 = Questions(question='I find that I also want to work in my free time.')
question11 = Questions(question='I work because I enjoy it.')
question12 = Questions(question='When I am working on something, I am doing it for myself.')
question13 = Questions(question='I get my motivation from the work itself, and not from the reward for it.')
db.session.add_all([question1, question2, question3, question4, question5, question6, question7, question8, question9,
                   question10, question11, question12, question13])
db.session.commit()
