# utils.py
def get_direct_download_link(url):
    # For Google Drive share links
    if 'drive.google.com' in url:
        if '/d/' in url:
            file_id = url.split('/d/')[1].split('/')[0]
        elif 'id=' in url:
            file_id = url.split('id=')[1]
        else:
            return url
        return f'https://drive.google.com/uc?export=download&id={file_id}'
    return url
