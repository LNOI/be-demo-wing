from src.models import models
from src.db.base import DBContext
from sqlalchemy.orm import Session
from src.services.llm_s import suggestion

# async def create_user(user,db:Session)-> models.User:
#     db_user = models.User(name=user.name, fullname=user.fullname)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# async def init_course(db:Session)-> models.Courses:
#     level = [0,1]
#     topic = [1,2,3,4,5,6]

#     # db_course = models.Courses(topic=course.topic,level = course.level,vocabulary=course.vocabulary)
#     db.add(db_course)
#     db.commit()
#     db.refresh(db_course)
#     return db_course

async def create_essay(essay,db:Session)-> models.Essay:
    db_essay = models.Essay(essay=essay.essay,output=essay.output,user_id = essay.user_id)
    db.add(db_essay)
    db.commit()
    db.refresh(db_essay)
    return db_essay


async def essay(essay,db:Session):
    data = db.query(models.Courses).all()
    # vocabulary = [i["vocabulary"] for i in data if i["topic"]==essay.topic]
    for i in data:
        if essay.topic in i.topic:
            gramary = i.gram
            vocalbulary = i.vocabulary
            break

    data1 = db.query(models.Essay).all()
    # vocabulary = [ i["vocabulary"] for i in data if i["topic"]==essay.topic ]
    for i in data1:
        if essay.essay_id == i.id:
            essay_data = i.essay
            break
    res =suggestion(essay=essay_data,topic=essay.topic,level=essay.level,vol=vocalbulary,gram=gramary)
    print(res)
    return res



# async def save_essay(easy)-> models.User:
#     db_user = models.User(name=user.name, fullname=user.fullname)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user