import urllib.request
src1="https://www.clipartmax.com/middle/m2H7d3K9H7b1K9d3_python-logo"
src2="https://www.clipartmax.com/png/small/434-4343754_python-logo.png"
src3="https://www.clipartmax.com/png/middle/434-4343754_python-logo.png"

listsrc = [src1,src2,src3]
say = 1
for src in listsrc:
    urllib.request.urlretrieve(src,"İmage"+str(say)+".jpg")
    say += 1
