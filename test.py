from fkzjooc.api import API

user = API('19533941201', 'Abcd1234')

course_list = user.get_user_course_list(1)
for course in course_list['data']:
    for chapter in user.get_course_chapter_list(course['id'])['data']:
        chapter_id = chapter['id']
        for child in chapter['children']:
            child_id = child['id']
            for clz in child['children']:
                clz_id = clz['id']
                video_progress = user.get_user_video_progress(course['id'], clz_id)