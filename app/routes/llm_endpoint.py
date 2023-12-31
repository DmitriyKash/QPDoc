from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, Depends
from app.database.db import get_db, SessionLocal
from app.database.models import PDFModel, User
from app.services.llm import llm_service
import app.repository.histories as repository_history


load_dotenv()
router = APIRouter(prefix='/llm', tags=['llm'])


@router.post("/chat")
async def llm_endpoint(query: str, user_id: int, file_id: int, db: SessionLocal = Depends(get_db)):
    # Знаходимо всі файли, що належать даному користувачу
    # user_files = db.query(PDFModel).filter(PDFModel.user_id == user_id).all()

    # Перевірка, чи є файли
    # if not user_files:
    #    raise HTTPException(status_code=404, detail="No files uploaded by this user")

    # Збираємо відповіді для кожного файлу

    # for file in user_files:
    # Передаємо ID кожного файлу у функцію чат-бота
    answer = await llm_service.run_llm(query, user_id, file_id, db)
    result = {"code": answer[0], "answer": answer[1]}
    if answer[0] == 200:
        new_record = await repository_history.create_record(user_id, file_id, query, answer[1], db)
        result["qa_id"] = new_record.id
    # answers.append({"file_id": user_id, "answer": answer})

    return result
