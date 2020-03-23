import asyncio
from django.utils.decorators import sync_and_async_middleware


@sync_and_async_middleware
def nothing_middleware(get_response):
    # One-time configuration and initialization goes here.
    if asyncio.iscoroutinefunction(get_response):
        async def middleware(request):
            # Do something here!
            print("do nothing")
            response = await get_response(request)
            return response

    else:
        def middleware(request):
            # Do something here!
            print("do nothing")
            response = get_response(request)
            return response

    return middleware
