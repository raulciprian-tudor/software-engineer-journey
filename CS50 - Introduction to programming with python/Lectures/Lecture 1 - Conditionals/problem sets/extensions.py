file_name = input('File name: ')
file_pieces = file_name.rpartition('.')

match file_pieces[1] + file_pieces[2]:
    case '.gif':
        print('image/gif')
    case '.jpg':
        print('image/jpeg')
    case '.jpeg':
        print('image/jpeg')
    case '.png':
        print('image/png')
    case '.pdf':
        print('application/pdf')
    case '.txt':
        print('text/plain')
    case '.zip':
        print('application/zip')
    case _:
        print('application/octet-stream')
