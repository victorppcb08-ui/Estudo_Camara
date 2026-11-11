import sys
frag = open(sys.argv[1], encoding='utf-8').read()
doc = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       '<style>:root{color-scheme:light}body{margin:0;font-size:14px}img{max-width:100%}[hidden]{display:none!important}</style>\n'
       '</head>\n<body>\n' + frag + '\n</body>\n</html>\n')
open(sys.argv[2], 'w', encoding='utf-8').write(doc)
