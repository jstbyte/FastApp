import app.config  # Keep It Top of the File;
from fastapi import FastAPI  # FastAPI Class;
from fastapi.responses import HTMLResponse
from app.auth.router import auth_router

app = FastAPI()  # FastAPI instance;

# Add All Routers to the FastAPI instance (app);
app.include_router(auth_router)


@app.get("/", response_class=HTMLResponse)
def read_root() -> str:  # Demo Home Page;
    with open("html/home.html", "r") as file:
        return file.read()


if __name__ == "__main__":
    import uvicorn  # The ASGI Server;

    # Run the FastAPI app using Uvicorn;
    uvicorn.run(app, host="0.0.0.0", port=8000)
