from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.auth.routes import router as auth_router
from apps.diy_recipes.routes import router as recipes_router
from storage.routes import router as storage_router
from core.config import settings
from core.exceptions import setup_exception_handlers


def create_app() -> FastAPI:
    # Инициализация приложения
    app = FastAPI(
        title="DIY Recipes API",
        description="API для управления DIY",
        version="1.0.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
    )
    
    # Настройка CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Подключение обработчиков ошибок
    setup_exception_handlers(app)
    
    # Подключение роутеров из модулей
    app.include_router(
        auth_router,
        prefix="/api/auth",
        tags=["Authentication"],
    )
    
    app.include_router(
        recipes_router,
        prefix="/api/recipes",
        tags=["Recipes"],
    )
    
    app.include_router(
        storage_router,
        prefix="/api/storage",
        tags=["File Storage"],
    )
    
    return app


# Создание экземпляра приложения
app = create_app()


# Для удобства разработки можно добавить root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to DIY Recipes API",
        "docs": "/api/docs",
        "redoc": "/api/redoc",
    }