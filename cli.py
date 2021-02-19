import sys
import youtube
import subtitles

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: %s <youtube_link>" % (sys.argv[0]))
        print("Example: %s %s" % (sys.argv[0],
                                              'https://www.youtube.com/watch?v=_WC40T3FH88'))
        exit(1)
    try:
        subtitle_file = youtube.download_subtitles(sys.argv[1])
        print('Downloaded',subtitle_file)
        f = open(subtitle_file, "r")
        lines = f.readlines()
        f.close()
        ret = subtitles.get_clear_text(lines)
        ret.insert(0,subtitle_file)
        ret.insert(1,sys.argv[1])
        for l in ret:
            print(l)

    except Exception as err:
        print(err)