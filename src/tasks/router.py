from fastapi import APIRouter, BackgroundTasks, Depends

from src.auth.base_config import current_user

from src.tasks.tasks import send_email_report_dashboard

router = APIRouter(prefix="/report")


@router.get("/dashboard")
def get_dashboard_report(background_tasks: BackgroundTasks, user=Depends(current_user)):
    send_email_report_dashboard(user.username)
    background_tasks.add_task(send_email_report_dashboard, user.username)
    send_email_report_dashboard.delay(user.username)
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }