from voluptuous import Schema, Any, ALLOW_EXTRA, PREVENT_EXTRA

user = Schema({
    'auth': {
        'access_token': str,
        'firebase_token': Any(str, None),
        'expires_at': str,
        'suspended': int
    },
    'user': {
        'id': int,
        'username': Any(str, int),
        'name': Any(str, int),
        'created_at': str,
        'updated_at': str,
        'is_admin': bool,
        'is_lecturer': bool,
        'is_standard_user': bool,
        'is_super_admin': bool,
        'is_teacher': bool,
        'show_terms': bool,
        'pending_terms': bool,
        'notifications': {
            'items': [
                {
                    'id': str,
                    'type': str,
                    'message': str
                }
            ],
            'count': int
        },
        'email': str,
        'phone': Any(None, str),
        'id_passport': None,
        'birthdate': None,
        'is_purchases': bool,
        'email_verified_at': Any(str, dict),
        'email_is_validated': bool,
        'email_validation': {
            'address': str,
            'result': str,
            'reason': [
                str
            ],
            'risk': str,
            'isDisposableAddress': bool,
            'checkDate': str
        },
        'is_document_checked': bool,
        'is_new_popup_used': bool,
        'need_verification_popup': bool
    },
    'isDocumentChecked': None
},
    required=True,
    extra=ALLOW_EXTRA
)

bundles = Schema({
    "data": [
        {
            "id": int,
            "image": Any(None, str),
            "order": int,
            "name": str,
            "slug": str,
            "duration": Any(None, str),
            "prerequisites": Any(None, str),
            "description": Any(None, str),
            "status": Any(None, int),
            "start": Any(None, str),
            "end": Any(None, str),
            "price": Any(None, int, str, float),
            "discount_price": Any(None, int, str, float),
            "courses_count": int,
            "categories": [
                {
                    "id": int,
                    "created_at": str,
                    "updated_at": str,
                    "title": str,
                    "slug": Any(str, int),
                    "deleted_at": None
                }
            ]
        }

    ],
    "total": int,
    "per_page": int,
    "current_page": int,
    "last_page": int,
    "not_found": bool
},
    required=True,
    extra=ALLOW_EXTRA)

courses = Schema({
    "data": [
        {
            "id": int,
            "name": str,
            "is_over": bool,
            "course_enroll_request": None,
            "enrolled": None,
            "slug_id": str,
            "image": Any(None, str),
            "category_name": str,
            "short_description": Any(None, str),
            "price": Any(None, int),
            "discount_price": Any(None, int),
            "begin_date": Any(None, str),
            "has_access": bool,
            "status_purchase": Any(None, dict),
            "is_ministry_controlled": bool,
            "block_video_rewind": bool,
            "show_video_exam": bool,
            "exam_attempts_count": int,
            "is_disabled_all_successful_exam_notifications": bool
        }
    ],
    "total": int,
    "per_page": int,
    "current_page": int,
    "last_page": int,
    "not_found": bool
},
    required=True,
    extra=ALLOW_EXTRA
)

course = Schema({
    "id": int,
    "name": str,
    "is_over": bool,
    "enroll_request": None,
    "enrolled": None,
    "slug_id": str,
    "meta_title": Any(None, str),
    "meta_description": Any(None, str),
    "meta_author": Any(None, str),
    "image": Any(None, str),
    "category_name": str,
    "display_forum": bool,
    "price": Any(None, int),
    "has_access": bool,
    "discount_price": Any(None, int),
    "begin_date": Any(None, str),
    "duration": Any(None, str),
    "prerequisites": Any(None, str),
    "step_by_step": bool,
    "progress": {
        "progress": int,
        "lessons_learned_count": int,
        "sections_count": int
    },
    "lecturers": list,
    "description": Any(None, str),
    "files": [
        {
            "id": int,
            "name": str,
            "url": Any(None, str),
            "protected": bool
        }
    ],
    "vimeo": None,
    "about": Any(None, str),
    "sections": list,
    "syllabus_items": [
        {
            "id": int,
            "title": str,
            "files": [
                {
                    "id": int,
                    "url": str,
                    "name": str,
                    "size": str,
                    "type": str
                }
            ],
            "subitems": list
        },
        {
            "id": int,
            "title": str,
            "files": list,
            "subitems": list
        },
    ],
    "quotes": list,
    "calendars_without_group": list,
    "calendars_groups": list,
    "image_poster": None,
    "status_purchase": Any(None, dict),
    "statistics": {
        "lessons_count": int,
        "lessons_part_count": int,
        "exams_count": int,
        "practices_count": int,
        "surveys_count": int,
        "sections_count": int
    },
    "seo": {
        "title": Any(None, str),
        "description": Any(None, str),
        "author": Any(None, str)
    },
    "is_ministry_controlled": bool,
    "block_video_rewind": bool,
    "show_video_exam": bool,
    "exam_attempts_count": int,
    "is_disabled_all_successful_exam_notifications": bool
},
    required=True,
    extra=ALLOW_EXTRA
)

teachers = Schema(
    [
        {
            "about": Any(None, str),
            "access_level": int,
            "city": Any(None, str),
            "college_id": int,
            "email": None,
            "email_verified_at": Any(None, str),
            "full_name": str,
            "href": str,
            "image": Any(None, str),
            "id": int,
            "deleted_at": None,
            "is_approved": bool,
            "is_visible": bool,
            "last_seen": Any(None, str),
            "name": str,
            "phone_number": None,
            "positions": Any(None, str),
            "reg": str,
            "short_descr": Any(None, str),
            "show_cv": int,
            "status": int,
            "status_text": str,
            "username": str,
            "files": list,
            "teaches_courses": {
                "data": [
                    {
                        "id": int,
                        "name": str,
                        "is_over": bool,
                        "course_enroll_request": None,
                        "enrolled": None,
                        "slug_id": str,
                        "image": Any(None, str),
                        "category_name": str,
                        "short_description": Any(None, str),
                        "price": Any(None, int),
                        "discount_price": Any(None, int),
                        "begin_date": Any(None, str),
                        "has_access": bool,
                        "status_purchase": Any(None, dict),
                        "is_ministry_controlled": bool,
                        "block_video_rewind": bool,
                        "show_video_exam": bool,
                        "exam_attempts_count": int,
                        "is_disabled_all_successful_exam_notifications": bool

                    }
                ],
                "total": int,
                "per_page": int,
                "current_page": int,
                "last_page": int,
                "not_found": bool
            },
            "rating": {
                "rate": Any(None, int, float),
                "reviews_count": int
            }
        }

    ],
    required=True,
    extra=ALLOW_EXTRA
)

teacher = Schema(
    {
        "about": Any(None, str),
        "access_level": int,
        "city": Any(None, str),
        "college_id": int,
        "email": Any(None, str),
        "email_verified_at": str,
        "full_name": str,
        "href": str,
        "image": Any(None, str),
        "id": int,
        "created_at": str,
        "deleted_at": None,
        "is_approved": bool,
        "is_visible": bool,
        "last_seen": str,
        "name": str,
        "phone_number": Any(None, str),
        "positions": Any(None, str),
        "reg": str,
        "short_descr": Any(None, str),
        "show_cv": int,
        "status": int,
        "status_text": str,
        "username": str,
        "files": [
            {
                "id": int,
                "url": Any(None, str),
                "name": Any(None, str),
                "size": str,
                "type": int,
                "views": int
            }
        ],
        "teaches_courses": {
            "data": [
                {
                    "id": int,
                    "name": str,
                    "is_over": bool,
                    "course_enroll_request": None,
                    "enrolled": None,
                    "slug_id": str,
                    "image": Any(None, str),
                    "category_name": str,
                    "short_description": Any(None, str),
                    "price": Any(None, int),
                    "discount_price": Any(None, int),
                    "begin_date": Any(None, str),
                    "has_access": bool,
                    "status_purchase": Any(None, dict),
                    "is_ministry_controlled": bool,
                    "block_video_rewind": bool,
                    "show_video_exam": bool,
                    "exam_attempts_count": int,
                    "is_disabled_all_successful_exam_notifications": bool
                }
            ],
            "total": int,
            "per_page": int,
            "current_page": int,
            "last_page": int,
            "not_found": bool
        },
        "threads": {
            "data": list,
            "total": int,
            "per_page": int,
            "current_page": int,
            "last_page": int,
            "not_found": bool
        },
        "seo": {
            "title": Any(None, str),
            "description": Any(None, str)
        }
    },
    required=True,
    extra=ALLOW_EXTRA
)

bundle = Schema(
    {
        "id": int,
        "image": Any(None, str),
        "order": int,
        "name": str,
        "slug": str,
        "duration": Any(None, str),
        "prerequisites": Any(None, str),
        "description": Any(None, str),
        "content": Any(None, str),
        "status": None,
        "start": Any(None, str),
        "end": Any(None, str),
        "price": Any(None, str, int),
        "discount_price": Any(None, str, int),
        "video": Any(None, str),
        "vimeo_id": Any(None, int),
        "courses": [
            {
                "id": int,
                "name": str,
                "is_over": bool,
                "course_enroll_request": None,
                "enrolled": None,
                "slug_id": str,
                "image": Any(None, str),
                "category_name": str,
                "short_description": Any(None, str),
                "price": Any(None, str, int),
                "discount_price": Any(None, str, int),
                "begin_date": Any(None, str),
                "has_access": bool,
                "status_purchase": Any(None, dict)
            }
        ],
        "courses_count": int,
        "categories": [
            {
                "id": int,
                "created_at": str,
                "updated_at": str,
                "title": str,
                "slug": str,
                "deleted_at": None,
                "pivot": {
                    "bundle_id": str,
                    "category_id": int,
                    "created_at": str,
                    "updated_at": str
                }
            }
        ],
        "files": [
            {
                "id": int,
                "url": str,
                "name": str,
                "size": str,
                "type": str
            }
        ],
        "seo": {
            "title": Any(None, str),
            "description": Any(None, str)
        },
        "enroll_request": None,
        "status_purchase": Any(None, dict),
        "is_over": bool
    },
    required=True,
    extra=ALLOW_EXTRA
)

status_register_course = Schema(
    {
        "id": int,
        "status": int,
        "student_read_status_change": Any(None, bool),
        "is_accepted": bool,
        "is_dissolved": bool,
        "is_pending": bool,
        "is_rejected": bool,
        "is_will_open_later": bool,
        "user_id": int
    },
    required=True,
    extra=ALLOW_EXTRA
)

message_forum = Schema(
    {
        "id": int,
        "created_at": str,
        "updated_at": str,
        "course": {
            "slug": str,
            "id": int,
            "name": str,
            "has_access": bool,
            "category": {
                "id": int,
                "slug": int,
                "title": str
            }
        },
        "subject": str,
        "text": str,
        "slug": str,
        "flags_show_editor": bool,
        "replies_count": int,
        "root_thread_id": None,
        "user_id": int,
        "children": [

        ],
        "user": {
            "id": int,
            "username": str,
            "name": str,
            "teacher": bool,
            "lecturer": bool,
            "student": bool,
            "role": str,
            "image": Any(None, str),
            "about": Any(None, str),
            "rating": int,
            "reviews_count": int,
            "description": Any(None, str)
        },
        "thread_id": int,
        "is_my": bool,
        "updated": None,
        "seo": {
            "title": Any(None, str),
            "description": Any(None, str)
        }
    },
    required=True,
    extra=ALLOW_EXTRA
)
