import sys
import os
import os.path

import s3util

s3util.set_conn()


def upload_photos(local_files, s3_basename):

    bucket_name = os.getenv('AWS_S3_BLOG_BUCKET_NAME')
    for fn in local_files:
        with open(fn) as fd:
            content = fd.read()

        fragment = fn.split('/')[-1]
        s3_filename = os.path.join(s3_basename, fragment)
        
        s3util.write_s3_file(bucket_name, s3_filename, content)

if __name__ == '__main__': 
    import ipdb; ipdb.set_trace()
    basename = sys.argv[1]
    fns = sys.argv[2:]

    s3util.set_conn()
    upload_photos(fns, basename)

    print 'done'

