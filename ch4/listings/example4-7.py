# using Starlette directly
import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def greeting(request):
    return JSONResponse("Hello World!")

app = Starlette(debug=True, routes=[
    Route("/hi", greeting)
])


if __name__ == "__main__":
    uvicorn.run("example4-7:app", reload=True)
