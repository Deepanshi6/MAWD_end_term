from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import sessionLocal
from fastapi import FastAPI , Request , Depends,Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from models import Books

def get_db():
    db=sessionLocal()
    try:
        yield db
    except Exception as e:
        raise e 
    finally:
        db.close() 

app=FastAPI()
templates = Jinja2Templates(directory="../frontend/templates")

# Static files
app.mount("/static", StaticFiles(directory="../Frontend/static"), name="static")


@app.get("/")
def home(request:Request,
         db:Session=Depends(get_db)):
    books_k=db.query(Books).all()
    context={"request":request,"books_h":books_k}
    return templates.TemplateResponse("index.html",context)

@app.get("/view/{b_id}")
def view_b(request:Request,
           b_id:int,
           db:Session=Depends(get_db)):
    book_v=db.query(Books).filter(Books.id==b_id).first()
    context={"request":request,"book_v":book_v}
    return templates.TemplateResponse("view.html",context)

@app.get("/add")
def add_b(request:Request,
           db:Session=Depends(get_db)):
    context={"request":request}
    return templates.TemplateResponse("add.html",context)

@app.post("/add_book")
def create_book(
    title: str = Form(...),
    author: str = Form(...),
    year: int = Form(...),
    db: Session = Depends(get_db)
):
    new_task = Books(title=title, author=author, year=year)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return RedirectResponse("/", status_code=303)

@app.get("/update/{b_id}")
def work_book(request:Request,
              b_id:int,
              db: Session = Depends(get_db)
              ):
    book_u=db.query(Books).filter(Books.id==b_id).first()
    context={"request":request,"book_u":book_u}
    return templates.TemplateResponse("update.html",context)

@app.post("/update_book/{b_id}")
def update_b(
    b_id:int,
    title: str = Form(...),
    author: str = Form(...),
    year: int = Form(...),
    db: Session = Depends(get_db)):
    book_u=db.query(Books).filter(Books.id==b_id).first()
    if not book_u:
        return{"error":"task not found"}
    book_u.title=title
    book_u.author=author
    book_u.year=year
    db.commit()
    db.refresh(book_u)
    return RedirectResponse("/", status_code=303)

@app.get("/delete/{b_id}")
def delete(request:Request,
           b_id=int,
           db:Session=Depends(get_db)
           ):
    books_d=db.query(Books).filter(Books.id==b_id).first()
    db.delete(books_d)
    db.commit()
    return RedirectResponse("/",status_code=303)