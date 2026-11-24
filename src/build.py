import re,sys,os
root=os.path.dirname(os.path.abspath(__file__))
s=open(os.path.join(root,'index.template.html')).read()
d=re.search(r'd="([^"]*)"',open(os.path.join(root,'..','assets','sonar-logo.svg')).read()).group(1)
subs=re.findall(r'M[^M]*',d)
out=s.replace('LOGO_D',d).replace('LOGO_O',subs[1]+subs[5])
open(os.path.join(root,'..','index.html'),'w').write(out)
print('index.html', len(out))
