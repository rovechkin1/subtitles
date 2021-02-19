from subprocess import Popen, PIPE

def download_subtitles(youtube_link, lang='ru'):
    process = Popen(['youtube-dl',
                     '--write-auto-sub',
                     '--sub-lang',lang,
                     '--skip-download',
                     youtube_link],
                    stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    if len(stderr) > 0:
        raise Exception(str(stderr))
    else:
        #print(stdout)
        decoded = stdout.decode('utf-8').strip(" \t\n")
        out_file = str(decoded).split("Writing video subtitles to:")
        if len(out_file) < 2:
            print("No subtitles found")
            return ""
        else:
            return ""+out_file[1].strip(" \t\n")+""

if __name__ == "__main__":
    file='https://www.youtube.com/watch?v=_WC40T3FH88'
    ret=download_subtitles(file,'en')
    print(ret)