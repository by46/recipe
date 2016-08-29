import os


def _post_generate():
    """ convert CRLF to LF line separator

    Because cookcutter #405 bug

    :param temp_work_dir:
    :param output_project:
    :return:
    """
    post = ["ci/analysis.sh", "ci/deploy.sh", "ci/ut.sh"]
    for post_file_path in post:
        if not os.path.exists(post_file_path):
            continue

        lines = open(post_file_path, 'rb').readlines()
        # convert CRLF to LF
        with open(post_file_path, 'wb') as tmp:
            tmp.writelines([line.strip() + '\n' for line in lines])


_post_generate()
