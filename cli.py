import sys
import youtube
import subtitles
from pathlib import Path


def download_subtitles(link,lang='ru'):
    subtitle_file = youtube.download_subtitles(link,lang)
    print('Downloaded', subtitle_file)
    f = open(subtitle_file, "r")
    lines = f.readlines()
    f.close()
    ret = subtitles.get_clear_text(lines)
    ret.insert(0, subtitle_file)
    ret.insert(1, link)
    out_file = Path(subtitle_file)
    out_file = out_file.with_suffix('.txt')
    f = open(out_file, 'w')
    f.writelines(ret)
    f.close()
    print("Saved subtitles in '%s'" % out_file)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: %s <youtube_link>" % (sys.argv[0]))
        print("Example: %s %s" % (sys.argv[0],
                                              'https://www.youtube.com/watch?v=_WC40T3FH88'))
        exit(1)
    try:
        download_subtitles(sys.argv[1],'ru')
        download_subtitles(sys.argv[1],'en')

    except Exception as err:
        print(err)