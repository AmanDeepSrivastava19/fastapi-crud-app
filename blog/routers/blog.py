from typing import List
from fastapi import APIRouter,Depends,status,Response,HTTPException
from ..import schemas,database,models,oauth2
from sqlalchemy.orm import Session
router=APIRouter(
    tags=['Blogs']
)


@router.get('/blog',response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    blogs=db.query(models.Blog).all()
    return blogs

@router.post('/blog')
def create(request:schemas.Blog, db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.post('/blog')
def create(request:schemas.Blog, db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return 'Blog is deleted successfully.'

@router.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    #if you want to update a single field in a db
    # db.query(models.Blog).filter(models.Blog.id==id).update({'title':'updated title'})

    #if you want to update the entire fields
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            details=f"Blog with id {id} not found")

    blog.update(request)
    db.commit()
    return "Blog data is updated."

@router.get('/blog/{id}',status_code=200, response_model=List[schemas.ShowBlog])
def show(id,response:Response,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    return blog