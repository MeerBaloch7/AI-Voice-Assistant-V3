from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.lifecycle import ApplicationLifecycle

lifecycle = ApplicationLifecycle()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await lifecycle.startup()
    yield
    await lifecycle.shutdown()


app = FastAPI(
    title="AI Assistant V3",
    version="3.0.0",
    lifespan=lifespan,
)

# Register routes