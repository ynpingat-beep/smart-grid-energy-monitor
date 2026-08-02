from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(tags=["WebSocket"])

connected_clients = []


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    connected_clients.append(websocket)

    print("Client Connected")

    try:
        while True:
            message = await websocket.receive_text()
            print("Received:", message)

            for client in connected_clients:
                try:
                    await client.send_text("🟢 Dashboard updated successfully")
                except Exception:
                    # ignore send errors for individual clients
                    pass
    except WebSocketDisconnect:
        if websocket in connected_clients:
            connected_clients.remove(websocket)
        print("Client Disconnected")