import os
import shutil
from uuid import uuid4

from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    HTTPException
)

from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database import get_db

from app.models.document import Document
from app.models.user import User

from app.schemas.document import DocumentResponse

from app.rag.ingest import ingest_chunks

from app.rag.text_processor import (
    read_text_file,
    chunk_text
)


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post(
    "/upload",
    response_model=DocumentResponse,
    status_code=201
)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    allowed_extensions = [".txt"]

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename missing"
        )

    file_extension = os.path.splitext(
        file.filename
    )[1].lower()

    if file_extension not in allowed_extensions:

        raise HTTPException(
            status_code=400,
            detail="Only .txt files are allowed"
        )

    os.makedirs("uploads", exist_ok=True)

    unique_filename = f"{uuid4()}{file_extension}"

    file_path = os.path.join(
        "uploads",
        unique_filename
    )

    try:

        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        new_document = Document(
            filename=file.filename,
            file_path=file_path,
            owner_id=current_user.id
        )

        db.add(new_document)

        db.commit()

        db.refresh(new_document)

        text = read_text_file(file_path)

        chunks = chunk_text(text)

        ingest_chunks(
            chunks=chunks,
            document_id=new_document.id #type: ignore
        )

        return new_document

    except Exception as e:

        if os.path.exists(file_path):
            os.remove(file_path)

        raise HTTPException(
            status_code=500,
            detail=f"File upload failed: {str(e)}"
        )

    finally:

        file.file.close()