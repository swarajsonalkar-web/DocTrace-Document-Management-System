from fastapi import FastAPI,UploadFile,File,HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import sqlite3,pathlib,uuid
ROOT=pathlib.Path(__file__).parent;STORE=ROOT/'uploads';STORE.mkdir(exist_ok=True);DB=ROOT/'doctrace.db'
ALLOWED={'.pdf','.txt','.md','.docx','.png','.jpg','.jpeg'}
def db():
 c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;return c
with db() as c:c.execute('CREATE TABLE IF NOT EXISTS docs(id TEXT PRIMARY KEY,name TEXT,size INTEGER,created_at TEXT DEFAULT CURRENT_TIMESTAMP)')
app=FastAPI(title='DocTrace')
@app.get('/api/docs')
def docs():
 with db() as c:return [dict(r) for r in c.execute('SELECT * FROM docs ORDER BY created_at DESC')]
@app.post('/api/upload')
async def upload(file:UploadFile=File(...)):
 name=pathlib.Path(file.filename or 'file').name;ext=pathlib.Path(name).suffix.lower()
 if ext not in ALLOWED:raise HTTPException(400,'File type not allowed')
 data=await file.read()
 if len(data)>10*1024*1024:raise HTTPException(413,'Maximum size is 10 MB')
 ident=uuid.uuid4().hex;(STORE/(ident+ext)).write_bytes(data)
 with db() as c:c.execute('INSERT INTO docs(id,name,size) VALUES(?,?,?)',(ident,name,len(data)))
 return {'id':ident}
@app.get('/api/download/{ident}')
def download(ident:str):
 with db() as c:r=c.execute('SELECT * FROM docs WHERE id=?',(ident,)).fetchone()
 if not r:raise HTTPException(404,'Not found')
 p=next(STORE.glob(ident+'.*'),None)
 if not p:raise HTTPException(404,'File missing')
 return FileResponse(p,filename=r['name'])
@app.post('/api/convert')
async def convert(file:UploadFile=File(...)):
 name=pathlib.Path(file.filename or 'text.txt').name
 if pathlib.Path(name).suffix.lower() not in {'.txt','.md'}:raise HTTPException(400,'Only TXT and MD supported')
 raw=await file.read()
 if len(raw)>2*1024*1024:raise HTTPException(413,'Maximum size is 2 MB')
 ident=uuid.uuid4().hex;p=STORE/(ident+'.pdf');c=canvas.Canvas(str(p),pagesize=A4);w,h=A4;y=h-45
 for line in raw.decode('utf-8',errors='replace').splitlines():
  if y<45:c.showPage();y=h-45
  c.drawString(40,y,line[:115]);y-=15
 c.save();out=pathlib.Path(name).stem+'.pdf'
 with db() as con:con.execute('INSERT INTO docs(id,name,size) VALUES(?,?,?)',(ident,out,p.stat().st_size))
 return {'id':ident}
app.mount('/',StaticFiles(directory='static',html=True),name='static')
